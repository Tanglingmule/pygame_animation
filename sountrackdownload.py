from pytube import YouTube

url = 'https://youtu.be/MXDF0wVcWfA?si=yzMTyQJnm80o9DRn'
YouTube(url).streams.get_highest_resolution().download('.//assets//music')