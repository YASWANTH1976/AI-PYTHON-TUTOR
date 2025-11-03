import sys
from io import StringIO
import time
from typing import Tuple, Dict

class CodeVisualizer:
    """Executes and visualizes Python code safely"""

    def __init__(self):
        self.execution_history = []

    def execute_code(self, code: str, timeout: int = 5) -> Tuple[bool, str, Dict]:
        """
        Execute Python code safely and return results
        
        Returns:
            success (bool): Whether code executed without errors
            output (str): Print output or error message
            info (dict): Execution info (time, variables, etc.)
        """
        old_stdout = sys.stdout
        sys.stdout = StringIO()
        
        start_time = time.time()
        success = False
        output = ""
        variables = {}
        error_msg = ""
        
        try:
            exec_globals = {
                '__builtins__': __builtins__,
                'print': print,
            }
            exec_locals = {}
            exec(code, exec_globals, exec_locals)
            output = sys.stdout.getvalue()
            variables = {k: v for k, v in exec_locals.items() if not k.startswith('_')}
            success = True
        except SyntaxError as e:
            error_msg = f"Syntax Error: {str(e)}\nLine {e.lineno}: {e.text}"
            output = error_msg
        except NameError as e:
            error_msg = f"Name Error: {str(e)}\nHint: Did you forget to define a variable?"
            output = error_msg
        except TypeError as e:
            error_msg = f"Type Error: {str(e)}\nHint: Check your data types!"
            output = error_msg
        except ZeroDivisionError:
            error_msg = "Math Error: Cannot divide by zero!"
            output = error_msg
        except Exception as e:
            error_msg = f"Error: {type(e).__name__}: {str(e)}"
            output = error_msg
        finally:
            sys.stdout = old_stdout
        
        execution_time = time.time() - start_time
        
        info = {
            "execution_time": round(execution_time, 3),
            "variables_created": variables,
            "lines_of_code": len(code.split('\n')),
            "error": error_msg if not success else None
        }
        
        self.execution_history.append({
            "code": code,
            "success": success,
            "output": output,
            "info": info,
            "timestamp": time.time()
        })
        
        return success, output, info

    def analyze_code_complexity(self, code: str) -> Dict:
        """Analyze code complexity and provide feedback"""
        lines = code.split('\n')
        analysis = {
            "total_lines": len(lines),
            "blank_lines": sum(1 for line in lines if not line.strip()),
            "comment_lines": sum(1 for line in lines if line.strip().startswith('#')),
            "code_lines": 0,
            "indentation_levels": 0,
            "loops_found": 0,
            "functions_found": 0,
            "conditionals_found": 0
        }
        
        max_indent = 0
        for line in lines:
            stripped = line.strip()
            if stripped and not stripped.startswith('#'):
                analysis["code_lines"] += 1
                
                # Check indentation
                indent = len(line) - len(line.lstrip())
                max_indent = max(max_indent, indent)
                
                # Check for structures
                if any(keyword in stripped for keyword in ['for ', 'while ']):
                    analysis["loops_found"] += 1
                if stripped.startswith('def '):
                    analysis["functions_found"] += 1
                if any(keyword in stripped for keyword in ['if ', 'elif ', 'else:']):
                    analysis["conditionals_found"] += 1
        
        analysis["indentation_levels"] = max_indent // 4 + 1 if max_indent > 0 else 0
        
        # Complexity rating
        complexity_score = (
            analysis["loops_found"] * 2 +
            analysis["functions_found"] * 3 +
            analysis["conditionals_found"] +
            analysis["indentation_levels"]
        )
        
        if complexity_score <= 3:
            analysis["complexity"] = "Beginner"
        elif complexity_score <= 8:
            analysis["complexity"] = "Intermediate"
        else:
            analysis["complexity"] = "Advanced"
        
        return analysis

    def get_code_suggestions(self, code: str) -> list:
        """Provide suggestions to improve code"""
        suggestions = []
        lines = code.split('\n')
        
        # Check for common issues
        if not any(line.strip().startswith('#') for line in lines):
            suggestions.append("💡 Add comments to explain your code")
        
        if any('print(' in line for line in lines) and len(lines) > 10:
            suggestions.append("💡 Consider using logging instead of print for larger programs")
        
        # Check for long lines
        long_lines = [i+1 for i, line in enumerate(lines) if len(line) > 79]
        if long_lines:
            suggestions.append(f"💡 Lines {long_lines} are too long (>79 chars). Consider breaking them up")
        
        # Check for variable naming
        if any(var in code for var in ['a =', 'b =', 'x =', 'y =']) and len(lines) > 5:
            suggestions.append("💡 Use descriptive variable names instead of single letters")
        
        # Check for functions
        if len(lines) > 15 and 'def ' not in code:
            suggestions.append("💡 Consider breaking your code into functions for better organization")
        
        return suggestions

    def visualize_execution_flow(self, code: str) -> str:
        """Create a simple text-based visualization of code flow"""
        lines = code.split('\n')
        flow = []
        
        for line in lines:
            stripped = line.strip()
            if not stripped or stripped.startswith('#'):
                continue
            
            # Calculate indent
            current_indent = (len(line) - len(line.lstrip())) // 4
            
            # Create flow representation
            prefix = "  " * current_indent + "→ "
            
            if stripped.startswith('def '):
                flow.append(f"{prefix}📦 Function Definition: {stripped}")
            elif any(stripped.startswith(kw) for kw in ['if ', 'elif ', 'else']):
                flow.append(f"{prefix}🔀 Decision: {stripped}")
            elif any(kw in stripped for kw in ['for ', 'while ']):
                flow.append(f"{prefix}🔄 Loop: {stripped}")
            elif 'return' in stripped:
                flow.append(f"{prefix}↩️ Return: {stripped}")
            elif 'print' in stripped:
                flow.append(f"{prefix}📤 Output: {stripped}")
            else:
                flow.append(f"{prefix}⚙️ Execute: {stripped}")
        
        return "\n".join(flow) if flow else "No executable code found"

    def get_execution_history(self) -> list:
        """Return execution history"""
        return self.execution_history

    def clear_history(self):
        """Clear execution history"""
        self.execution_history = []


# Global visualizer instance for use
visualizer = CodeVisualizer()

# Convenience wrapper functions
def execute_code(code: str, timeout: int = 5) -> Tuple[bool, str, Dict]:
    return visualizer.execute_code(code, timeout)

def analyze_code_complexity(code: str) -> Dict:
    return visualizer.analyze_code_complexity(code)

def get_code_suggestions(code: str) -> list:
    return visualizer.get_code_suggestions(code)

def visualize_execution_flow(code: str) -> str:
    return visualizer.visualize_execution_flow(code)

def get_execution_history() -> list:
    return visualizer.get_execution_history()

def clear_history():
    visualizer.clear_history()