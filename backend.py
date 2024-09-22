import base64
import mimetypes

# Function to process input data
def process_request(request):
    # Extract data
    data = request.get("data", [])
    
    # Separate numbers and alphabets
    numbers = [x for x in data if x.isdigit()]
    alphabets = [x for x in data if x.isalpha()]

    # Find the highest lowercase alphabet
    lowercase_alphabets = [x for x in alphabets if x.islower()]
    highest_lowercase_alphabet = max(lowercase_alphabets) if lowercase_alphabets else None

    # Decode and validate file (assuming base64 image)
    file_b64 = request.get("file_b64")
    file_valid, file_mime_type, file_size_kb = validate_file(file_b64)

    # Construct response
    response = {
        "is_success": True,
        "user_id": "yashi4",
        "email": "yr9190@srmist.edu.in",
        "roll_number": "RA2111031010058",
        "numbers": numbers,
        "alphabets": alphabets,
        "highest_lowercase_alphabet": [highest_lowercase_alphabet] if highest_lowercase_alphabet else [],
        "file_valid": file_valid,
        "file_mime_type": file_mime_type,
        "file_size_kb": file_size_kb
    }

    return response

# Function to validate base64 encoded file
def validate_file(file_b64):
    try:
        # Decode the base64 string
        file_data = base64.b64decode(file_b64)
        file_size_kb = len(file_data) / 1024  # Convert to KB
        mime_type = mimetypes.guess_type("file.png")[0]  # Assume a PNG file for now

        return True, mime_type, f"{file_size_kb:.2f}"
    except Exception as e:
        return False, None, None

# Example request input
request = {
    "data": ["Y","A","S","H","I", "1", "3", "4","5","8" ,"9","R", "0", "y","r"],
    "file_b64": "BASE_64_STRING"
}

# Call the function and print the response
response = process_request(request)
print(response)
