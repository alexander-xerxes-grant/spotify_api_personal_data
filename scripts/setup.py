# Script that asks the user for their SPOTIFY_CLIENT_SECRET and
# SPOTIFY_CLIENT_ID, creates a .env file and populates it with them

def get_input():
    spotify_client_id = input('Please input your SPOTIFY_CLIENT_ID (32 character string): ')
    spotify_client_secret = input('Please input your SPOTIFY_CLIENT_SECRET (32 character string): ')
    return spotify_client_id, spotify_client_secret

def write_to_env(spotify_client_id, spotify_client_secret):
    with open('.env','w') as f:
        f.write("SPOTIFY_CLIENT_ID=" + '"' + spotify_client_id + '"' + "\n")
        f.write("SPOTIFY_CLIENT_SECRET=" + '"' + spotify_client_secret + '"')
    
    

if __name__ == "__main__":
    spotify_client_id, spotify_client_secret = get_input()
    write_to_env(spotify_client_id, spotify_client_secret)
    