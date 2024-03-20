from SymbolTableManager import SymbolTableManager
from cparser import Parser
import sys
import argparse
import os

def compile(input_path):
    SymbolTableManager.init()
    parser = Parser(input_path)
    parser.parse()
    parser.save_parse_tree()
    parser.save_syntax_errors()
    parser.lexer.save_lexical_errors()
    parser.lexer.save_symbol_table()
    parser.lexer.save_tokens()
    parser.semantic_analyzer.save_semantic_errors()


# compile("C:\\Users\\91904\\Documents\\UniC\\input\\input.c")

if __name__ == "__main__":
    if len(sys.argv) < 3 or sys.argv[1] != "-n":
        print("Usage: python main.py -n <input_path>")
        sys.exit(1)  
    input_path = sys.argv[2]
    
    current_path = os.getcwd()
    parser = argparse.ArgumentParser(description='UniC Compiler')
    parser.add_argument('-n', '--input', type=str, help='input file path', required=True)
    args = parser.parse_args()
    input_path = args.input
    
    # Check if input_path is a complete actual path
    if not os.path.isabs(input_path):  input = current_path+'/'+input_path
    else:                              input = input_path

    input = input.replace("\\", "/")
    # print(f'current path :: {input}')

    # Check if the file exists
    if not os.path.isfile(input):
        print("File not found")
        sys.exit(1)
    
    try:
        compile(input_path)
        # Print the contents of all the files in the errors folder
        script_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))+'\\UniC'
        errors_folder = os.path.join(script_dir,"errors")
        for filename in os.listdir(errors_folder):
            if filename.endswith(".txt"):
                file_path = os.path.join(errors_folder, filename)
                with open(file_path, "r") as file:
                    print(file.read())

        # Print the contents of the output.txt file in the output folder
        # output_folder = "output"
        # for filename in os.listdir(output_folder):
        #     if filename.endswith(".txt"):
        #         file_path = os.path.join(output_folder, filename)
        #         with open(file_path, "r") as file:
        #             print(file.read())

    except Exception as e:
        print(e)
        sys.exit(1)


    
