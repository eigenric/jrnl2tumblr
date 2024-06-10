# jrnl2tumblr

## Description
`jrnl2tumblr` is a tool that allows you to import journal entries from [jrnl](https://jrnl.sh/) to your Tumblr blog.

## Features
- Imports journal entries from a JSON file exported by jrnl.
- Posts entries to a specified Tumblr blog.
- Ensures privacy and security by requiring OAuth authentication.

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/jrnl2tumblr.git
   ```

2. Navigate to the `jrnl2tumblr` directory:
   ```bash
   cd jrnl2tumblr
   ```

3. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the tool:
   ```bash
   python __main__.py path_to_jrnl_json_file.json your_tumblr_blog_name
   ```

## Usage
1. Export your journal entries from jrnl to a JSON file:
   ```bash
   jrnl --export json > path_to_jrnl_json_file.json
   ```

2. Run `jrnl2tumblr` and provide the path to the JSON file and your Tumblr blog name.

3. Follow the prompts to enter your Tumblr OAuth credentials.

4. Your journal entries will be imported and posted to your Tumblr blog.

## Requirements
- Python 3.x
- [jrnl](https://jrnl.sh/)
- A Tumblr account

## Contributing
Contributions are welcome! Please feel free to submit a pull request or open an issue if you encounter any bugs or have suggestions for improvements.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
```
