
import os
import re

# Directories to process
directories = ["_talks", "_publications"]

def extract_front_matter_and_rest(content):
    match = re.search(r'^---\n(.*?)\n---(.*)', content, re.DOTALL)
    if match:
        return match.group(1), match.group(2)
    return None, None

def get_field(front_matter, field_name):
    # Matches "field: value" or "field:\n  value..."
    # This regex is simple and might miss some edge cases but works for standard Jekyll FM
    pattern = re.compile(r'^' + field_name + r':\s*(.*)', re.MULTILINE)
    match = pattern.search(front_matter)
    if match:
        val = match.group(1).strip()
        if val:
            return val
        # If empty, might be multiline
        # Find start position
        start = match.end()
        # Find next key starting line to limit scope
        # Look for a line that starts with a word char and a colon
        next_key = re.search(r'^\w+:', front_matter[start:], re.MULTILINE)
        if next_key:
            block = front_matter[start : start + next_key.start()]
        else:
            block = front_matter[start:]
        
        # Clean up block (remove newlines and indentations)
        return re.sub(r'\s+', ' ', block).strip()
    return None

def main():
    fixed_count = 0
    skipped_count = 0
    
    for directory in directories:
        if not os.path.exists(directory):
            print(f"Directory {directory} does not exist.")
            continue
            
        for filename in os.listdir(directory):
            if not filename.endswith(".md"):
                continue
                
            filepath = os.path.join(directory, filename)
            
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Check if file has carousel include
            if "include carousels/" not in content and "include carousel.html" not in content:
                continue

            fm, rest = extract_front_matter_and_rest(content)
            if not fm:
                print(f"Skipping {filename}: No front matter found.")
                continue
                
            # Check for excerpt
            if re.search(r'^excerpt:', fm, re.MULTILINE):
                skipped_count += 1
                print(f"Skipping {filename}: Already has excerpt.")
                continue
            
            # Get abstract
            abstract = get_field(fm, 'abstract')
            excerpt_text = ""
            if abstract:
                excerpt_text = abstract
                # Handle double quotes for YAML string safety if we were just dumping text
                # But here we will simple replace invalid chars if needed options
                # Truncate
                if len(excerpt_text) > 300:
                    excerpt_text = excerpt_text[:300] + "..."
            else:
                excerpt_text = "See full paper for details."
            
            # Sanitize for single-line YAML
            # Remove existing quotes if wrapping entire string? 
            # Safest is to just escape double quotes and wrap in double quotes
            safe_excerpt = excerpt_text.replace('"', '\\"')
            excerpt_line = f'excerpt: "{safe_excerpt}"'
            
            # Append to front matter
            # Check if fm ends with newline
            if not fm.endswith('\n'):
                fm += '\n'
            fm += excerpt_line + "\n"
            
            new_content = "---\n" + fm + "---" + rest
            
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            
            print(f"Fixed {filename}")
            fixed_count += 1

    print(f"Finished. Fixed: {fixed_count}, Skipped: {skipped_count}")

if __name__ == "__main__":
    main()
