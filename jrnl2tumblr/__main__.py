import argparse
from jrnl2tumblr.importer import read_jrnl_file
from jrnl2tumblr.tumblr import create_tumblr_client, post_entries_to_tumblr

def main():
    parser = argparse.ArgumentParser(description='Importa entradas de jrnl a Tumblr.')
    parser.add_argument('jrnl_file', help='Ruta al archivo JSON exportado por jrnl')
    parser.add_argument('blog_name', help='Nombre del blog de Tumblr')
    parser.add_argument('consumer_key', help='Consumer key de la API de Tumblr')
    parser.add_argument('consumer_secret', help='Consumer secret de la API de Tumblr')
    parser.add_argument('oauth_token', help='OAuth token de la API de Tumblr')
    parser.add_argument('oauth_secret', help='OAuth secret de la API de Tumblr')

    args = parser.parse_args()

    entries = read_jrnl_file(args.jrnl_file)
    client = create_tumblr_client(
        args.consumer_key,
        args.consumer_secret,
        args.oauth_token,
        args.oauth_secret
    )
    post_entries_to_tumblr(entries, client, args.blog_name)

if __name__ == '__main__':
    main()
