import subprocess
import chardet


# Function to detect encoding and decode console output
def decode_console_output(output_bytes):
    # Detect encoding
    detected_encoding = chardet.detect(output_bytes)['encoding']
    if detected_encoding:
        # Decode output using detected encoding
        decoded_output = output_bytes.decode(detected_encoding, errors='replace')
        return decoded_output
    else:
        return None


# Function to capture and display console output
def capture_console_output(command):
    # Run the command in the Windows console
    process = subprocess.Popen(["powershell", "-Command", command], stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                               shell=True)
    output, error = process.communicate()

    # Check if there is any output
    if output:
        print("Console Output:")
        decoded_output = decode_console_output(output)
        if decoded_output:
            print(decoded_output)
        else:
            print("Unable to decode output.")
    # Check if there is any error
    if error:
        print("Error Output:")
        print(error.decode('utf-8', errors='replace'))


# Main function to get input from the user and call the capture_console_output function
def main():
    # Define the PowerShell command
    powershell_command = "Get-Process | Where-Object {$_.mainWindowTitle} | Format-Table Id, Name, mainWindowtitle -AutoSize"

    # Call the capture_console_output function with the PowerShell command
    capture_console_output(powershell_command)


if __name__ == "__main__":
    main()
