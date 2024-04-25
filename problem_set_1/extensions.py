def main():
    file_name = input('File name: ')
    print(extension_type(file_name))

def extension_type(file):
    # Normalize file name
    file = file.strip().lower()

    if file.endswith('.gif'):
            return 'image/gif'
    elif file.endswith(('.jpg', '.jpeg')):
            return 'image/jpeg'
    elif file.endswith('png'):
            return 'image/png'
    elif file.endswith('pdf'):
            return 'application/pdf'
    elif file.endswith( 'txt'):
            return 'text/plain'
    elif file.endswith('zip'):
            return 'application/zip'
    else:
        return 'application/octet-stream'

main()
