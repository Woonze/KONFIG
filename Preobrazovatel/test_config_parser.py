import unittest
import os
import yaml
from main import parse_globals, parse_dict, remove_comments

class TestConfigParser(unittest.TestCase):
    def test_global_variables(self):
        input_data = """
        var test_var = 42;
        var string_var = "hello";
        var bool_var = true;
        """
        globals_dict = parse_globals(input_data)
        self.assertEqual(globals_dict["test_var"], 42)
        self.assertEqual(globals_dict["string_var"], "hello")
        self.assertEqual(globals_dict["bool_var"], True)

    def test_array_syntax(self):
        input_data = """
        var num = 42;
        data: ({ name: @"John", age: 30, value: $(num) })
        """
        globals_dict = parse_globals(input_data)
        result = parse_dict(input_data, globals_dict)
        self.assertEqual(result["data"]["name"], "John")
        self.assertEqual(result["data"]["age"], 30)
        self.assertEqual(result["data"]["value"], 42)

    def test_nested_objects(self):
        input_data = """
        settings: ({ 
            database: { host: @"localhost", port: 5432 },
            cache: { enabled: true, ttl: 3600 }
        })
        """
        result = parse_dict(input_data, {})
        self.assertEqual(result["settings"]["database"]["host"], "localhost")
        self.assertEqual(result["settings"]["database"]["port"], 5432)
        self.assertEqual(result["settings"]["cache"]["enabled"], True)
        self.assertEqual(result["settings"]["cache"]["ttl"], 3600)

    def test_comments(self):
        input_data = """
        {- This is a comment -}
        data: ({ value: 42 })
        {- Another comment -}
        """
        cleaned_data = remove_comments(input_data)
        result = parse_dict(cleaned_data, {})
        self.assertEqual(result["data"]["value"], 42)

    def test_invalid_array_syntax(self):
        input_data = "data: [invalid_syntax]"
        with self.assertRaises(SyntaxError) as context:
            parse_dict(input_data, {})
        self.assertTrue("Arrays must be in the format" in str(context.exception))

    def test_invalid_string_syntax(self):
        input_data = 'data: ({ value: "missing_at_symbol" })'
        with self.assertRaises(SyntaxError) as context:
            parse_dict(input_data, {})
        self.assertTrue("String values must start with @" in str(context.exception))

    def test_invalid_variable_reference(self):
        input_data = """
        data: ({ value: $(undefined_var) })
        """
        with self.assertRaises(SyntaxError) as context:
            parse_dict(input_data, {})
        self.assertTrue("Undefined variable" in str(context.exception))

if __name__ == '__main__':
    unittest.main()
