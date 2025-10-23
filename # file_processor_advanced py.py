# file_processor_advanced.py

import os

class FileProcessor:
    """Advanced file processor with multiple modification options"""
    
    def __init__(self):
        self.operations = {
            '1': ('Convert to UPPERCASE', self._to_uppercase),
            '2': ('Convert to lowercase', self._to_lowercase),
            '3': ('Add line numbers', self._add_line_numbers),
            '4': ('Reverse content', self._reverse_content)
        }
    
    def process_file(self):
        """Main method to process files with comprehensive error handling"""
        try:
            filename = input("Enter the filename to process: ")
            
            # Check if file exists and is readable
            if not os.path.exists(filename):
                raise FileNotFoundError(f"File '{filename}' does not exist")
            
            if not os.access(filename, os.R_OK):
                raise PermissionError(f"Cannot read file '{filename}'")
            
            # Read file content
            with open(filename, 'r', encoding='utf-8') as file:
                content = file.read()
            
            if not content.strip():
                raise ValueError("File is empty")
            
            # Show available operations
            print("\nAvailable modification operations:")
            for key, (description, _) in self.operations.items():
                print(f"{key}. {description}")
            
            # Get user choice
            choice = input("\nChoose an operation (1-4): ")
            if choice not in self.operations:
                raise ValueError("Invalid operation choice")
            
            # Perform the selected operation
            operation_name, operation_func = self.operations[choice]
            modified_content = operation_func(content)
            
            # Generate new filename
            name, ext = os.path.splitext(filename)
            new_filename = f"{name}_modified{ext}"
            
            # Write modified content
            with open(new_filename, 'w', encoding='utf-8') as new_file:
                new_file.write(modified_content)
            
            print(f"\n✅ Success!")
            print(f"Operation: {operation_name}")
            print(f"Original file: {filename}")
            print(f"Modified file: {new_filename}")
            print(f"Original size: {len(content)} characters")
            print(f"Modified size: {len(modified_content)} characters")
            
        except FileNotFoundError as e:
            print(f"❌ File Error: {e}")
        except PermissionError as e:
            print(f"❌ Permission Error: {e}")
        except ValueError as e:
            print(f"❌ Input Error: {e}")
        except UnicodeDecodeError:
            print(f"❌ Encoding Error: Cannot read file with default encoding")
        except Exception as e:
            print(f"❌ Unexpected Error: {e}")
    
    def _to_uppercase(self, content):
        return content.upper()
    
    def _to_lowercase(self, content):
        return content.lower()
    
    def _add_line_numbers(self, content):
        lines = content.split('\n')
        numbered_lines = [f"{i+1}: {line}" for i, line in enumerate(lines)]
        return '\n'.join(numbered_lines)
    
    def _reverse_content(self, content):
        return content[::-1]

# Run the program
if __name__ == "__main__":
    processor = FileProcessor()
    processor.process_file()