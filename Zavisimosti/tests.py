import unittest
from unittest.mock import patch, MagicMock
from main import read_config, get_dependencies, create_graph


class TestDependencyVisualizer(unittest.TestCase):

    def test_read_config(self):
        config = read_config('test_config.csv')
        self.assertIn('Graphviz Path', config)
        self.assertIn('Package Name', config)

    @patch('subprocess.run')
    def test_get_dependencies(self, mock_run):
        mock_run.return_value = MagicMock(stdout="Requires: dep1, dep2\n")
        dependencies = get_dependencies('package', max_depth=1)
        self.assertIn('package', dependencies)
        self.assertEqual(dependencies['package'], ['dep1', 'dep2'])

    @patch('visualizer.Digraph')
    def test_create_graph(self, mock_digraph):
        dependencies = {'pkg1': ['pkg2', 'pkg3']}
        create_graph(dependencies, 'test_output')
        mock_digraph().edge.assert_any_call('pkg1', 'pkg2')
        mock_digraph().edge.assert_any_call('pkg1', 'pkg3')


if __name__ == '__main__':
    unittest.main()
