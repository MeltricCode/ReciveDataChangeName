from bs4 import BeautifulSoup
import requests
import os
# server
response = requests.get('https://toplearn.com/courses/operating-system/%D8%A2%D9%85%D9%88%D8%B2%D8%B4-%D8%AC%D8%A7%D9%85%D8%B9-%D9%84%DB%8C%D9%86%D9%88%DA%A9%D8%B3-Essentials-')
directory = 'D:\Linux-Essential'
#files inside my directory
videos = os.listdir(directory)

html = response.content
soup = BeautifulSoup(html, 'html.parser')
video_dev = soup.find_all(class_='video-item cursor-pointer')

#appending directory files in list
my_old_videos = []
for video in videos:
    old_name = (os.path.join(directory, video))
    my_old_videos.append(old_name)

if response.status_code == 200:
    # fo on all dev with class_='video-item cursor-pointer'
    for i, item in enumerate(video_dev):
        class_number = item.find('span').text
        class_name = item.find('h2', class_='view-Live').text
        new_n = os.path.join(directory, f'{class_number}-{class_name}.mp4')
        # print(my_old_videos[i],'----------------->',new_n)
        os.rename(my_old_videos[i], new_n)

else:
    print(response.status_code, 'CannotConnect')
