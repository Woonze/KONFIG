import argparse
import re
import sys
import yaml


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("input_file_path", type=str, help="Path to the input file with configuration text")
    parser.add_argument("output_file_path", type=str, help="Path to the output YAML file")
    return parser.parse_args()


def read_input_file(input_file_path):
    with open(input_file_path, "r", encoding="utf-8") as file:
        return file.read()


def remove_comments(input_data):
    return re.sub(r'\{\-\s*.*?\s*\-\}', '', input_data, flags=re.DOTALL)


def parse_globals(input_data):
    globals_dict = {}
    matches = re.findall(r'var\s+([a-zA-Z][_a-zA-Z0-9]*)\s*=\s*("[^"]*"|\d+|true|false)', input_data)
    for name, value in matches:
        if value.isdigit():
            globals_dict[name] = int(value)
        elif value == "true":
            globals_dict[name] = True
        elif value == "false":
            globals_dict[name] = False
        else:
            globals_dict[name] = value.strip('"')
    return globals_dict


def evaluate_expression(expression, globals_dict):
    """Evaluate expressions like $(var_name)."""
    if expression.startswith("$(") and expression.endswith(")"):
        var_name = expression[2:-1]
        if var_name not in globals_dict:
            raise SyntaxError(f"Undefined variable: {var_name}")
        return globals_dict[var_name]
    return expression


def process_value(value, globals_dict):
    """Process a single value according to the configuration language rules."""
    value = value.strip()
    
    if value.startswith('$('):
        return evaluate_expression(value, globals_dict)
    elif value.startswith('@"') and value.endswith('"'):
        content = value[2:-1]  # Remove @" and "
        # Check if the string contains any variable references
        if '$(' in content:
            # Find all variable references
            var_refs = re.findall(r'\$\(([a-zA-Z][a-zA-Z0-9_]*)\)', content)
            for var_name in var_refs:
                if var_name not in globals_dict:
                    raise SyntaxError(f"Undefined variable: {var_name}")
                content = content.replace(f'$({var_name})', str(globals_dict[var_name]))
        return content
    elif value == 'true':
        return True
    elif value == 'false':
        return False
    elif value.isdigit():
        return int(value)
    elif not value.startswith('@"') and '"' in value:
        raise SyntaxError("String values must start with @")
    else:
        raise SyntaxError(f"Invalid value format: {value}")


def parse_object(content, globals_dict):
    """Parse an object with key-value pairs."""
    result = {}
    # Remove curly braces
    content = content.strip().strip('{}').strip()
    
    # Split by commas, but not within nested structures
    pairs = []
    current = ''
    nesting_level = 0
    in_quotes = False
    
    for char in content:
        if char == '"' and not in_quotes and current.endswith('@'):
            in_quotes = True
            current += char
        elif char == '"' and in_quotes:
            in_quotes = False
            current += char
        elif char == '{' and not in_quotes:
            nesting_level += 1
            current += char
        elif char == '}' and not in_quotes:
            nesting_level -= 1
            current += char
        elif char == ',' and nesting_level == 0 and not in_quotes:
            if current.strip():
                pairs.append(current.strip())
            current = ''
        else:
            current += char
    
    if current.strip():
        pairs.append(current.strip())
    
    # Process each key-value pair
    for pair in pairs:
        if ':' not in pair:
            raise SyntaxError(f"Invalid key-value pair: {pair}")
        
        key, value = [x.strip() for x in pair.split(':', 1)]
        key = key.strip('"')
        
        # Handle nested objects
        if value.strip().startswith('{'):
            result[key] = parse_object(value, globals_dict)
        else:
            result[key] = process_value(value, globals_dict)
    
    return result


def parse_array(content, globals_dict):
    """Parse an array of values."""
    if not (content.strip().startswith('({') and content.strip().endswith('})')):
        raise SyntaxError("Arrays must be in the format ({ value1, value2, ... })")
    
    # Remove outer ({ and })
    content = content.strip()[2:-2].strip()
    
    # If it's an object-like structure, parse it as an object
    if ':' in content and not content.startswith('@"'):
        return parse_object('{' + content + '}', globals_dict)
    
    # Otherwise, split by commas and parse each value
    values = []
    current = ''
    nesting_level = 0
    in_quotes = False
    
    for char in content:
        if char == '"' and not in_quotes and current.endswith('@'):
            in_quotes = True
            current += char
        elif char == '"' and in_quotes:
            in_quotes = False
            current += char
        elif char == '{' and not in_quotes:
            nesting_level += 1
            current += char
        elif char == '}' and not in_quotes:
            nesting_level -= 1
            current += char
        elif char == ',' and nesting_level == 0 and not in_quotes:
            if current.strip():
                try:
                    value = current.strip()
                    # Если это число
                    if value.isdigit():
                        values.append(int(value))
                    # Если это строка
                    elif value.startswith('@"') and value.endswith('"'):
                        values.append(process_value(value, globals_dict))
                    # Если это переменная
                    elif value.startswith('$('):
                        values.append(process_value(value, globals_dict))
                    # Если это булево значение
                    elif value in ['true', 'false']:
                        values.append(value == 'true')
                    else:
                        raise SyntaxError(f"Invalid value in array: {value}")
                except Exception as e:
                    raise SyntaxError(f"Error processing array value '{value}': {str(e)}")
            current = ''
        else:
            current += char
    
    if current.strip():
        try:
            value = current.strip()
            # Если это число
            if value.isdigit():
                values.append(int(value))
            # Если это строка
            elif value.startswith('@"') and value.endswith('"'):
                values.append(process_value(value, globals_dict))
            # Если это переменная
            elif value.startswith('$('):
                values.append(process_value(value, globals_dict))
            # Если это булево значение
            elif value in ['true', 'false']:
                values.append(value == 'true')
            else:
                raise SyntaxError(f"Invalid value in array: {value}")
        except Exception as e:
            raise SyntaxError(f"Error processing array value '{value}': {str(e)}")
    
    return values


def parse_dict(input_data, globals_dict):
    """Parse the entire configuration file."""
    output = {}
    
    try:
        # Find all sections with their content
        sections = []
        current_section = ''
        current_content = ''
        nesting_level = 0
        in_quotes = False
        
        lines = input_data.split('\n')
        for line in lines:
            line = line.strip()
            if not line or line.startswith('var '):
                continue
                
            if ':' in line and nesting_level == 0 and not in_quotes:
                if current_section and current_content:
                    sections.append((current_section, current_content))
                current_section = line.split(':')[0].strip()
                current_content = line.split(':', 1)[1].strip()
            else:
                current_content += ' ' + line
                
            for char in line:
                if char == '"' and not in_quotes and current_content.endswith('@'):
                    in_quotes = True
                elif char == '"' and in_quotes:
                    in_quotes = False
                elif char == '(' and not in_quotes:
                    nesting_level += 1
                elif char == ')' and not in_quotes:
                    nesting_level -= 1
        
        if current_section and current_content:
            sections.append((current_section, current_content))
            
        if not sections:
            raise SyntaxError("No valid sections found")
            
        # Process each section
        for section, content in sections:
            if not re.match(r'^[a-z]+$', section):
                raise SyntaxError(f"Invalid identifier '{section}'. Names must contain only lowercase letters.")
            
            # Parse the content as an array
            output[section] = parse_array(content, globals_dict)
            
    except Exception as e:
        raise SyntaxError(f"Error parsing configuration: {str(e)}")
    
    return output


def main():
    args = parse_args()
    try:
        input_data = read_input_file(args.input_file_path)
        input_data = remove_comments(input_data)

        try:
            globals_dict = parse_globals(input_data)
        except Exception as e:
            print(f"Error parsing global variables: {str(e)}", file=sys.stderr)
            sys.exit(1)

        try:
            yaml_data = parse_dict(input_data, globals_dict)
        except SyntaxError as e:
            print(f"Syntax error: {str(e)}", file=sys.stderr)
            sys.exit(1)
        except Exception as e:
            print(f"Error: {str(e)}", file=sys.stderr)
            sys.exit(1)

        with open(args.output_file_path, "w", encoding="utf-8") as output_file:
            yaml.dump(yaml_data, output_file, allow_unicode=True, default_flow_style=False)

        print(f"YAML data written to {args.output_file_path}")

    except FileNotFoundError:
        print(f"Error: Input file '{args.input_file_path}' not found", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Error: {str(e)}", file=sys.stderr)
        sys.exit(1)


if __name__ == '__main__':
    main()
