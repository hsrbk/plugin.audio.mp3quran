import sys
import os
import urllib
import xbmc
import xbmcgui
import xbmcplugin
import xbmcaddon
import logging
from operator import itemgetter

fanart = xbmc.translatePath(os.path.join('special://home/addons/plugin.audio.mp3quran',  'fanart.jpg'))
iconart = xbmc.translatePath(os.path.join('special://home/addons/plugin.audio.mp3quran',  'icon.png'))


def show_tags():
  tag_handle = int(sys.argv[1])
  xbmcplugin.setContent(tag_handle, 'tags')

  for tag in tags:
    iconPath = os.path.join(home, 'logos', tag['icon'])
    li = xbmcgui.ListItem(tag['name'], iconImage=iconPath)
    url = sys.argv[0] + '?tag=' + str(tag['id'])
    xbmcplugin.addDirectoryItem(handle=tag_handle, url=url, listitem=li, isFolder=True)

  xbmcplugin.endOfDirectory(tag_handle)


def show_streams(tag):
  stream_handle = int(sys.argv[1])
  xbmcplugin.setContent(stream_handle, 'streams')
  logging.warning('TAG show_streams!!!! %s', tag)
  for stream in streams[str(tag)]:
    logging.debug('STREAM HERE!!! %s', stream['name'])
    iconPath = os.path.join(home, 'logos', stream['icon'])
    li = xbmcgui.ListItem(stream['name'], iconImage=iconPath)
    xbmcplugin.addDirectoryItem(handle=stream_handle, url=stream['url'], listitem=li)

  xbmcplugin.endOfDirectory(stream_handle)


def get_params():
  """
  Retrieves the current existing parameters from XBMC.
  """
  param = []
  paramstring = sys.argv[2]
  if len(paramstring) >= 2:
    params = sys.argv[2]
    cleanedparams = params.replace('?', '')
    if params[len(params) - 1] == '/':
      params = params[0:len(params) - 2]
    pairsofparams = cleanedparams.split('&')
    param = {}
    for i in range(len(pairsofparams)):
      splitparams = {}
      splitparams = pairsofparams[i].split('=')
      if (len(splitparams)) == 2:
        param[splitparams[0]] = splitparams[1]
  return param


def lower_getter(field):
  def _getter(obj):
    return obj[field].lower()

  return _getter


addon = xbmcaddon.Addon()
home = xbmc.translatePath(addon.getAddonInfo('path'))


tags = [
  {
    'name': 'Quran Reciters',
    'id': 'rctr',
    'icon': 'icon.png'
  }, {
    'name': 'Radio Stations 24/7',
    'id': 'rdio',
    'icon': 'icon.png'
  }
]



rctr = [{
  'name': '001 Abdelbari Al-Toubayti | Rewayat Hafs An Assem',
  'url': 'special://home/addons/plugin.audio.mp3quran/playlists/001.m3u',
  'icon': 'icon.png',
  'disabled': False
  
}, {
  'name': '002 Abdul Aziz Al-Ahmad | Rewayat Hafs An Assem',
  'url': 'special://home/addons/plugin.audio.mp3quran/playlists/002.m3u',
  'icon': 'icon.png',
  'disabled': False
}, {
  'name': '003 Abdulaziz Az-Zahrani | Rewayat Hafs An Assem',
  'url': 'special://home/addons/plugin.audio.mp3quran/playlists/003.m3u',
  'icon': 'icon.png',
  'disabled': False
}, {
  'name': '004 Abdulbari Mohammad | Almusshaf Al Molim',
  'url': 'special://home/addons/plugin.audio.mp3quran/playlists/004.m3u',
  'icon': 'icon.png',
  'disabled': False
}, {
  'name': '005 Abdulbari Mohammad | Rewayat Hafs An Assem',
  'url': 'special://home/addons/plugin.audio.mp3quran/playlists/005.m3u',
  'icon': 'icon.png',
  'disabled': False
}, {
  'name': '006 Abdulbasit Abdulsamad | Rewayat Hafs An Assem',
  'url': 'special://home/addons/plugin.audio.mp3quran/playlists/006.m3u',
  'icon': 'icon.png',
  'disabled': False
}, {
  'name': '007 Abdulbasit Abdulsamad | Rewayat Warsh An Nafi',
  'url': 'special://home/addons/plugin.audio.mp3quran/playlists/007.m3u',
  'icon': 'icon.png',
  'disabled': False
}, {
  'name': '008 Abdulbasit Abdulsamad | Almusshaf Al Mojawwad',
  'url': 'special://home/addons/plugin.audio.mp3quran/playlists/008.m3u',
  'icon': 'icon.png',
  'disabled': False
}, {
  'name': '009 Abdulghani Abdullah (From Malaysia) | Rewayat Hafs An Assem',
  'url': 'special://home/addons/plugin.audio.mp3quran/playlists/009.m3u',
  'icon': 'icon.png',
  'disabled': False
}, {
  'name': '010 Abdulhadi Kanakeri | Rewayat Hafs An Assem',
  'url': 'special://home/addons/plugin.audio.mp3quran/playlists/010.m3u',
  'icon': 'icon.png',
  'disabled': False
}, {
  'name': '011 Abdullah Al-Mattrod | Rewayat Hafs An Assem',
  'url': 'special://home/addons/plugin.audio.mp3quran/playlists/011.m3u',
  'icon': 'icon.png',
  'disabled': False
}, {
  'name': '012 Abdullah Albuajan | Rewayat Hafs An Assem',
  'url': 'special://home/addons/plugin.audio.mp3quran/playlists/012.m3u',
  'icon': 'icon.png',
  'disabled': False
}, {
  'name': '013 Abdullah Basfer | Rewayat Hafs An Assem',
  'url': 'special://home/addons/plugin.audio.mp3quran/playlists/013.m3u',
  'icon': 'icon.png',
  'disabled': False
}, {
  'name': '014 Abdullah Fahmi (From Malaysia) | Rewayat Hafs An Assem',
  'url': 'special://home/addons/plugin.audio.mp3quran/playlists/014.m3u',
  'icon': 'icon.png',
  'disabled': False
}, {
  'name': '015 Abdullah Khayyat | Rewayat Hafs An Assem',
  'url': 'special://home/addons/plugin.audio.mp3quran/playlists/015.m3u',
  'icon': 'icon.png',
  'disabled': False
}, {
  'name': '016 Abdullah Qaulan | Rewayat Hafs An Assem',
  'url': 'special://home/addons/plugin.audio.mp3quran/playlists/016.m3u',
  'icon': 'icon.png',
  'disabled': False
}, {
  'name': '017 Abdulmajeed Al-Arkani | Rewayat Hafs An Assem',
  'url': 'special://home/addons/plugin.audio.mp3quran/playlists/017.m3u',
  'icon': 'icon.png',
  'disabled': False
}, {
  'name': '018 Abdulmohsen Al-Qasim | Rewayat Hafs An Assem',
  'url': 'special://home/addons/plugin.audio.mp3quran/playlists/018.m3u',
  'icon': 'icon.png',
  'disabled': False
}, {
  'name': '019 Abdulmohsin Al-Askar | Rewayat Hafs An Assem',
  'url': 'special://home/addons/plugin.audio.mp3quran/playlists/019.m3u',
  'icon': 'icon.png',
  'disabled': False
}, {
  'name': '020 Abdulmohsin Al-Harthy | Rewayat Hafs An Assem',
  'url': 'special://home/addons/plugin.audio.mp3quran/playlists/020.m3u',
  'icon': 'icon.png',
  'disabled': False
}, {
  'name': '021 Abdulmohsin Al-Obaikan | Rewayat Hafs An Assem',
  'url': 'special://home/addons/plugin.audio.mp3quran/playlists/021.m3u',
  'icon': 'icon.png',
  'disabled': False
}, {
  'name': '022 Abdulrahman Aloosi | Rewayat Hafs An Assem',
  'url': 'special://home/addons/plugin.audio.mp3quran/playlists/022.m3u',
  'icon': 'icon.png',
  'disabled': False
}, {
  'name': '023 Abdulrahman Alsudaes | Rewayat Hafs An Assem',
  'url': 'special://home/addons/plugin.audio.mp3quran/playlists/023.m3u',
  'icon': 'icon.png',
  'disabled': False
}, {
  'name': '024 Abdulrasheed Soufi | Rewayat Assosi An Abi Amr',
  'url': 'special://home/addons/plugin.audio.mp3quran/playlists/024.m3u',
  'icon': 'icon.png',
  'disabled': False
}, {
  'name': '025 Abdulrasheed Soufi | Rewayat Khalaf An Hamzah',
  'url': 'special://home/addons/plugin.audio.mp3quran/playlists/025.m3u',
  'icon': 'icon.png',
  'disabled': False
}, {
  'name': '026 Abdulwadood Haneef | Rewayat Hafs An Assem',
  'url': 'special://home/addons/plugin.audio.mp3quran/playlists/026.m3u',
  'icon': 'icon.png',
  'disabled': False
}, {
  'name': '027 Abdulwali Al-Arkani | Rewayat Hafs An Assem',
  'url': 'special://home/addons/plugin.audio.mp3quran/playlists/027.m3u',
  'icon': 'icon.png',
  'disabled': False
}, {
  'name': '028 Addokali Mohammad Alalim | Rewayat Qalon An Nafi',
  'url': 'special://home/addons/plugin.audio.mp3quran/playlists/028.m3u',
  'icon': 'icon.png',
  'disabled': False
}, {
  'name': '029 Adel Al-Khalbany | Rewayat Hafs An Assem',
  'url': 'special://home/addons/plugin.audio.mp3quran/playlists/029.m3u',
  'icon': 'icon.png',
  'disabled': False
}, {
  'name': '030 Adel Ryyan | Rewayat Hafs An Assem',
  'url': 'special://home/addons/plugin.audio.mp3quran/playlists/030.m3u',
  'icon': 'icon.png',
  'disabled': False
}, {
  'name': '031 Ahmad Al-Ajmy | Rewayat Hafs An Assem',
  'url': 'special://home/addons/plugin.audio.mp3quran/playlists/031.m3u',
  'icon': 'icon.png',
  'disabled': False
}, {
  'name': '032 Ahmad Al-Hawashi | Rewayat Hafs An Assem',
  'url': 'special://home/addons/plugin.audio.mp3quran/playlists/032.m3u',
  'icon': 'icon.png',
  'disabled': False
}, {
  'name': '033 Ahmad Alhuthaifi | Rewayat Hafs An Assem',
  'url': 'special://home/addons/plugin.audio.mp3quran/playlists/033.m3u',
  'icon': 'icon.png',
  'disabled': False
}, {
  'name': '034 Ahmad Khader Al-Tarabulsi | Rewayat Qalon An Nafi',
  'url': 'special://home/addons/plugin.audio.mp3quran/playlists/034.m3u',
  'icon': 'icon.png',
  'disabled': False
}, {
  'name': '035 Ahmad Nauina | Rewayat Hafs An Assem',
  'url': 'special://home/addons/plugin.audio.mp3quran/playlists/035.m3u',
  'icon': 'icon.png',
  'disabled': False
}, {
  'name': '036 Ahmad Saber | Rewayat Hafs An Assem',
  'url': 'special://home/addons/plugin.audio.mp3quran/playlists/036.m3u',
  'icon': 'icon.png',
  'disabled': False
}, {
  'name': '037 Ahmad Saud | Rewayat Hafs An Assem',
  'url': 'special://home/addons/plugin.audio.mp3quran/playlists/037.m3u',
  'icon': 'icon.png',
  'disabled': False
}, {
  'name': '038 Reciter Ahmad Khader Al-Tarabulsi | Rewayat Qalon An Nafi',
  'url': 'special://home/addons/plugin.audio.mp3quran/playlists/038.m3u',
  'icon': 'icon.png',
  'disabled': False
}, {
  'name': '039 Ahmed Amer | Rewayat Hafs An Assem',
  'url': 'special://home/addons/plugin.audio.mp3quran/playlists/039.m3u',
  'icon': 'icon.png',
  'disabled': False
}, {
  'name': '040 Akhil Abdulhayy Rawa (From Malaysia) | Rewayat Hafs An Assem',
  'url': 'special://home/addons/plugin.audio.mp3quran/playlists/040.m3u',
  'icon': 'icon.png',
  'disabled': False
}, {
  'name': '041 Akram Alalaqmi | Rewayat Hafs An Assem',
  'url': 'special://home/addons/plugin.audio.mp3quran/playlists/041.m3u',
  'icon': 'icon.png',
  'disabled': False
}, {
  'name': '042 Al-Qaria Yassen | Rewayat Warsh An Nafi',
  'url': 'special://home/addons/plugin.audio.mp3quran/playlists/042.m3u',
  'icon': 'icon.png',
  'disabled': False
}, {
  'name': '043 Alashri Omran | Rewayat Hafs An Assem',
  'url': 'special://home/addons/plugin.audio.mp3quran/playlists/043.m3u',
  'icon': 'icon.png',
  'disabled': False
}, {
  'name': '044 Alfateh Alzubair | Rewayat Aldori An Abi Amr',
  'url': 'special://home/addons/plugin.audio.mp3quran/playlists/044.m3u',
  'icon': 'icon.png',
  'disabled': False
}, {
  'name': '045 Alhusayni Al-Azazi | Almusshaf Al Molim',
  'url': 'special://home/addons/plugin.audio.mp3quran/playlists/045.m3u',
  'icon': 'icon.png',
  'disabled': False
}, {
  'name': '046 Ali Abo-Hashim | Rewayat Hafs An Assem',
  'url': 'special://home/addons/plugin.audio.mp3quran/playlists/046.m3u',
  'icon': 'icon.png',
  'disabled': False
}, {
  'name': '047 Ali Alhuthaifi | Rewayat Qalon An Nafi',
  'url': 'special://home/addons/plugin.audio.mp3quran/playlists/047.m3u',
  'icon': 'icon.png',
  'disabled': False
}, {
  'name': '048 Ali Alhuthaifi | Rewayat Hafs An Assem',
  'url': 'special://home/addons/plugin.audio.mp3quran/playlists/048.m3u',
  'icon': 'icon.png',
  'disabled': False
}, {
  'name': '049 Ali Hajjaj Alsouasi | Rewayat Hafs An Assem',
  'url': 'special://home/addons/plugin.audio.mp3quran/playlists/049.m3u',
  'icon': 'icon.png',
  'disabled': False
}, {
  'name': '050 Ali Jaber | Rewayat Hafs An Assem',
  'url': 'special://home/addons/plugin.audio.mp3quran/playlists/050.m3u',
  'icon': 'icon.png',
  'disabled': False
}, {
  'name': '051 Aloyoon Al-Koshi | Rewayat Warsh An Nafi',
  'url': 'special://home/addons/plugin.audio.mp3quran/playlists/051.m3u',
  'icon': 'icon.png',
  'disabled': False
}, {
  'name': '052 Alzain Mohammad Ahmad | Rewayat Hafs An Assem',
  'url': 'special://home/addons/plugin.audio.mp3quran/playlists/052.m3u',
  'icon': 'icon.png',
  'disabled': False
}, {
  'name': '053 Bandar Balilah | Rewayat Hafs An Assem',
  'url': 'special://home/addons/plugin.audio.mp3quran/playlists/053.m3u',
  'icon': 'icon.png',
  'disabled': False
}, {
  'name': '054 Dawood Hamza | Rewayat Hafs An Assem',
  'url': 'special://home/addons/plugin.audio.mp3quran/playlists/054.m3u',
  'icon': 'icon.png',
  'disabled': False
}, {
  'name': '055 Emad Hafez | Rewayat Hafs An Assem',
  'url': 'special://home/addons/plugin.audio.mp3quran/playlists/055.m3u',
  'icon': 'icon.png',
  'disabled': False
}, {
  'name': '056 Fahad Al-Kandari | Rewayat Hafs An Assem',
  'url': 'special://home/addons/plugin.audio.mp3quran/playlists/056.m3u',
  'icon': 'icon.png',
  'disabled': False
}, {
  'name': '057 Fahad Al-Otaibi | Rewayat Hafs An Assem',
  'url': 'special://home/addons/plugin.audio.mp3quran/playlists/057.m3u',
  'icon': 'icon.png',
  'disabled': False
}, {
  'name': '058 Fares Abbad | Rewayat Hafs An Assem',
  'url': 'special://home/addons/plugin.audio.mp3quran/playlists/058.m3u',
  'icon': 'icon.png',
  'disabled': False
}, {
  'name': '059 Fawaz Alkabi | Rewayat Hafs An Assem',
  'url': 'special://home/addons/plugin.audio.mp3quran/playlists/059.m3u',
  'icon': 'icon.png',
  'disabled': False
}, {
  'name': '060 Hamad Al Daghriri | Rewayat Hafs An Assem',
  'url': 'special://home/addons/plugin.audio.mp3quran/playlists/060.m3u',
  'icon': 'icon.png',
  'disabled': False
}, {
  'name': '061 Hani Arrifai | Rewayat Hafs An Assem',
  'url': 'special://home/addons/plugin.audio.mp3quran/playlists/061.m3u',
  'icon': 'icon.png',
  'disabled': False
}, {
  'name': '062 Hatem Fareed Alwaer | Rewayat Hafs An Assem',
  'url': 'special://home/addons/plugin.audio.mp3quran/playlists/062.m3u',
  'icon': 'icon.png',
  'disabled': False
}, {
  'name': '063 Hazza Al-Balushi | Rewayat Hafs An Assem',
  'url': 'special://home/addons/plugin.audio.mp3quran/playlists/063.m3u',
  'icon': 'icon.png',
  'disabled': False
}, {
  'name': '064 Hussain Alshaik | Rewayat Hafs An Assem',
  'url': 'special://home/addons/plugin.audio.mp3quran/playlists/064.m3u',
  'icon': 'icon.png',
  'disabled': False
}, {
  'name': '065 Ibrahem Assadan | Rewayat Hafs An Assem',
  'url': 'special://home/addons/plugin.audio.mp3quran/playlists/065.m3u',
  'icon': 'icon.png',
  'disabled': False
}, {
  'name': '066 Ibrahim Al-Akdar | Rewayat Hafs An Assem',
  'url': 'special://home/addons/plugin.audio.mp3quran/playlists/066.m3u',
  'icon': 'icon.png',
  'disabled': False
}, {
  'name': '067 Ibrahim Al-Asiri | Rewayat Hafs An Assem',
  'url': 'special://home/addons/plugin.audio.mp3quran/playlists/067.m3u',
  'icon': 'icon.png',
  'disabled': False
}, {
  'name': '068 Ibrahim Al-Jebreen | Rewayat Hafs An Assem',
  'url': 'special://home/addons/plugin.audio.mp3quran/playlists/068.m3u',
  'icon': 'icon.png',
  'disabled': False
}, {
  'name': '069 Ibrahim Aldosari | Rewayat Warsh An Nafi',
  'url': 'special://home/addons/plugin.audio.mp3quran/playlists/069.m3u',
  'icon': 'icon.png',
  'disabled': False
}, {
  'name': '070 Ibrahim Aldosari | Rewayat Hafs An Assem',
  'url': 'special://home/addons/plugin.audio.mp3quran/playlists/070.m3u',
  'icon': 'icon.png',
  'disabled': False
}, {
  'name': '071 Ibrahim Aljormy | Rewayat Hafs An Assem',
  'url': 'special://home/addons/plugin.audio.mp3quran/playlists/071.m3u',
  'icon': 'icon.png',
  'disabled': False
}, {
  'name': '072 Idrees Abkr | Rewayat Hafs An Assem',
  'url': 'special://home/addons/plugin.audio.mp3quran/playlists/072.m3u',
  'icon': 'icon.png',
  'disabled': False
}, {
  'name': '073 Jamaan Alosaimi | Rewayat Hafs An Assem',
  'url': 'special://home/addons/plugin.audio.mp3quran/playlists/073.m3u',
  'icon': 'icon.png',
  'disabled': False
}, {
  'name': '074 Jamal Addeen Alzailaie | Rewayat Hafs An Assem',
  'url': 'special://home/addons/plugin.audio.mp3quran/playlists/074.m3u',
  'icon': 'icon.png',
  'disabled': False
}, {
  'name': '075 Jamal Shaker Abdullah | Rewayat Hafs An Assem',
  'url': 'special://home/addons/plugin.audio.mp3quran/playlists/075.m3u',
  'icon': 'icon.png',
  'disabled': False
}, {
  'name': '076 Khaled Al-Qahtani | Rewayat Hafs An Assem',
  'url': 'special://home/addons/plugin.audio.mp3quran/playlists/076.m3u',
  'icon': 'icon.png',
  'disabled': False
}, {
  'name': '077 Khalid Abdulkafi | Rewayat Hafs An Assem',
  'url': 'special://home/addons/plugin.audio.mp3quran/playlists/076.m3u',
  'icon': 'icon.png',
  'disabled': False
}, {
  'name': '078 Khalid Al-Jileel | Rewayat Hafs An Assem',
  'url': 'special://home/addons/plugin.audio.mp3quran/playlists/077.m3u',
  'icon': 'icon.png',
  'disabled': False
}, {
  'name': '079 Khalid Al-Shoraimy | Rewayat Hafs An Assem',
  'url': 'special://home/addons/plugin.audio.mp3quran/playlists/078.m3u',
  'icon': 'icon.png',
  'disabled': False
}, {
  'name': '080 Khalid Al-Wehabi | Rewayat Hafs An Assem',
  'url': 'special://home/addons/plugin.audio.mp3quran/playlists/080.m3u',
  'icon': 'icon.png',
  'disabled': False
}, {
  'name': '081 Khalid Algamdi | Rewayat Hafs An Assem',
  'url': 'special://home/addons/plugin.audio.mp3quran/playlists/081.m3u',
  'icon': 'icon.png',
  'disabled': False
}, {
  'name': '082 Khalid Almohana | Rewayat Hafs An Assem',
  'url': 'special://home/addons/plugin.audio.mp3quran/playlists/082.m3u',
  'icon': 'icon.png',
  'disabled': False
}, {
  'name': '083 Khalifa Altunaiji | Rewayat Hafs An Assem',
  'url': 'special://home/addons/plugin.audio.mp3quran/playlists/083.m3u',
  'icon': 'icon.png',
  'disabled': False
}, {
  'name': '084 Lafi Al-Oni | Rewayat Hafs An Assem',
  'url': 'special://home/addons/plugin.audio.mp3quran/playlists/084.m3u',
  'icon': 'icon.png',
  'disabled': False
}, {
  'name': '085 Maher Al Meaqli | Almusshaf Al Molim',
  'url': 'special://home/addons/plugin.audio.mp3quran/playlists/085.m3u',
  'icon': 'icon.png',
  'disabled': False
}, {
  'name': '086 Maher Al Meaqli | Rewayat Hafs An Assem',
  'url': 'special://home/addons/plugin.audio.mp3quran/playlists/086.m3u',
  'icon': 'icon.png',
  'disabled': False
}, {
  'name': '087 Maher Shakhashero | Rewayat Hafs An Assem',
  'url': 'special://home/addons/plugin.audio.mp3quran/playlists/087.m3u',
  'icon': 'icon.png',
  'disabled': False
}, {
  'name': '088 Mahmood Al rifai | Rewayat Hafs An Assem',
  'url': 'special://home/addons/plugin.audio.mp3quran/playlists/088.m3u',
  'icon': 'icon.png',
  'disabled': False
}, {
  'name': '089 Mahmood AlSheimy | Rewayat AlDorai An Al-Kisaai',
  'url': 'special://home/addons/plugin.audio.mp3quran/playlists/089.m3u',
  'icon': 'icon.png',
  'disabled': False
}, {
  'name': '090 Mahmoud Ali Albanna | Almusshaf Al Mojawwad',
  'url': 'special://home/addons/plugin.audio.mp3quran/playlists/090.m3u',
  'icon': 'icon.png',
  'disabled': False
}, {
  'name': '091 Mahmoud Ali Albanna | Rewayat Hafs An Assem',
  'url': 'special://home/addons/plugin.audio.mp3quran/playlists/091.m3u',
  'icon': 'icon.png',
  'disabled': False
}, {
  'name': '092 Mahmoud Khalil Al-Hussary | Rewayat Warsh An Nafi',
  'url': 'special://home/addons/plugin.audio.mp3quran/playlists/092.m3u',
  'icon': 'icon.png',
  'disabled': False
}, {
  'name': '093 Mahmoud Khalil Al-Hussary | Almusshaf Al Mojawwad',
  'url': 'special://home/addons/plugin.audio.mp3quran/playlists/093.m3u',
  'icon': 'icon.png',
  'disabled': False
}, {
  'name': '094 Mahmoud Khalil Al-Hussary | Rewayat Hafs An Assem',
  'url': 'special://home/addons/plugin.audio.mp3quran/playlists/094.m3u',
  'icon': 'icon.png',
  'disabled': False
}, {
  'name': '095 Majed Al-Enezi | Rewayat Hafs An Assem',
  'url': 'special://home/addons/plugin.audio.mp3quran/playlists/095.m3u',
  'icon': 'icon.png',
  'disabled': False
}, {
  'name': '096 Majed Al-Zamil | Rewayat Hafs An Assem',
  'url': 'special://home/addons/plugin.audio.mp3quran/playlists/096.m3u',
  'icon': 'icon.png',
  'disabled': False
}, {
  'name': '097 Malik shaibat Alhamed | Rewayat Hafs An Assem',
  'url': 'special://home/addons/plugin.audio.mp3quran/playlists/097.m3u',
  'icon': 'icon.png',
  'disabled': False
}, {
  'name': '098 Mishary Al Afasi | Rewayat AlDorai An Al-Kisaai',
  'url': 'special://home/addons/plugin.audio.mp3quran/playlists/098.m3u',
  'icon': 'icon.png',
  'disabled': False
}, {
  'name': '099 Mishary Alafasi | Rewayat Hafs An Assem',
  'url': 'special://home/addons/plugin.audio.mp3quran/playlists/099.m3u',
  'icon': 'icon.png',
  'disabled': False
}, {
  'name': '100 Moeedh Alharthi | Rewayat Hafs An Assem',
  'url': 'special://home/addons/plugin.audio.mp3quran/playlists/100.m3u',
  'icon': 'icon.png',
  'disabled': False
}, {
  'name': '101 Mohammad Abdullkarem | Rewayat Hafs An Assem',
  'url': 'special://home/addons/plugin.audio.mp3quran/playlists/101.m3u',
  'icon': 'icon.png',
  'disabled': False
}, {
  'name': '102 Mohammad Abdullkarem | Rewayat Warsh An Nafi Men Tariq Abi Baker Alasbahani',
  'url': 'special://home/addons/plugin.audio.mp3quran/playlists/102.m3u',
  'icon': 'icon.png',
  'disabled': False
}, {
  'name': '103 Mohammad Al-Abdullah | Rewayat Albizi and Qunbol An Ibn Katheer',
  'url': 'special://home/addons/plugin.audio.mp3quran/playlists/103.m3u',
  'icon': 'icon.png',
  'disabled': False
}, {
  'name': '104 Mohammad Al-Abdullah | Rewayat AlDorai An Al-Kisaai',
  'url': 'special://home/addons/plugin.audio.mp3quran/playlists/104.m3u',
  'icon': 'icon.png',
  'disabled': False
}, {
  'name': '105 Mohammad Al-Airawy | Rewayat Warsh An Nafi Men Tariq Abi Baker Alasbahani',
  'url': 'special://home/addons/plugin.audio.mp3quran/playlists/105.m3u',
  'icon': 'icon.png',
  'disabled': False
}, {
  'name': '106 Mohammad Al-Tablaway | Rewayat Hafs An Assem',
  'url': 'special://home/addons/plugin.audio.mp3quran/playlists/106.m3u',
  'icon': 'icon.png',
  'disabled': False
}, {
  'name': '107 Mohammad AlMonshed | Rewayat Hafs An Assem',
  'url': 'special://home/addons/plugin.audio.mp3quran/playlists/107.m3u',
  'icon': 'icon.png',
  'disabled': False
}, {
  'name': '108 Mohammad Khalil Al-Qari | Rewayat Hafs An Assem',
  'url': 'special://home/addons/plugin.audio.mp3quran/playlists/108.m3u',
  'icon': 'icon.png',
  'disabled': False
}, {
  'name': '109 Mohammad Rashad Alshareef | Rewayat Hafs An Assem',
  'url': 'special://home/addons/plugin.audio.mp3quran/playlists/109.m3u',
  'icon': 'icon.png',
  'disabled': False
}, {
  'name': '110 Mohammad Saleh Alim Shah | Rewayat Hafs An Assem',
  'url': 'special://home/addons/plugin.audio.mp3quran/playlists/110.m3u',
  'icon': 'icon.png',
  'disabled': False
}, {
  'name': '111 Mohammed Al-Barrak | Rewayat Hafs An Assem',
  'url': 'special://home/addons/plugin.audio.mp3quran/playlists/111.m3u',
  'icon': 'icon.png',
  'disabled': False
}, {
  'name': '112 Mohammed Al-Lohaidan | Rewayat Hafs An Assem',
  'url': 'special://home/addons/plugin.audio.mp3quran/playlists/112.m3u',
  'icon': 'icon.png',
  'disabled': False
}, {
  'name': '113 Mohammed Al-Muhasny | Rewayat Hafs An Assem',
  'url': 'special://home/addons/plugin.audio.mp3quran/playlists/113.m3u',
  'icon': 'icon.png',
  'disabled': False
}, {
  'name': '114 Mohammed Ayyub | Rewayat Hafs An Assem',
  'url': 'special://home/addons/plugin.audio.mp3quran/playlists/114.m3u',
  'icon': 'icon.png',
  'disabled': False
}, {
  'name': '115 Mohammed Hafas Ali (From Malaysia) | Rewayat Hafs An Assem',
  'url': 'special://home/addons/plugin.audio.mp3quran/playlists/115.m3u',
  'icon': 'icon.png',
  'disabled': False
}, {
  'name': '116 Mohammed Jibreel | Rewayat Hafs An Assem',
  'url': 'special://home/addons/plugin.audio.mp3quran/playlists/116.m3u',
  'icon': 'icon.png',
  'disabled': False
}, {
  'name': '117 Mohammed Osman Khan (from India) | Rewayat Hafs An Assem',
  'url': 'special://home/addons/plugin.audio.mp3quran/playlists/117.m3u',
  'icon': 'icon.png',
  'disabled': False
}, {
  'name': '118 Mohammed Siddiq Al-Minshawi | Almusshaf Al Molim',
  'url': 'special://home/addons/plugin.audio.mp3quran/playlists/118.m3u',
  'icon': 'icon.png',
  'disabled': False
}, {
  'name': '119 Mohammed Siddiq Al-Minshawi | Almusshaf Al Mojawwad',
  'url': 'special://home/addons/plugin.audio.mp3quran/playlists/119.m3u',
  'icon': 'icon.png',
  'disabled': False
}, {
  'name': '120 Mohammed Siddiq Al-Minshawi | Rewayat Hafs An Assem',
  'url': 'special://home/addons/plugin.audio.mp3quran/playlists/120.m3u',
  'icon': 'icon.png',
  'disabled': False
}, {
  'name': '121 Mousa Bilal | Rewayat Hafs An Assem',
  'url': 'special://home/addons/plugin.audio.mp3quran/playlists/121.m3u',
  'icon': 'icon.png',
  'disabled': False
}, {
  'name': '122 Muamar (From Indonesia) | Rewayat Hafs An Assem',
  'url': 'special://home/addons/plugin.audio.mp3quran/playlists/122.m3u',
  'icon': 'icon.png',
  'disabled': False
}, {
  'name': '123 Muftah Alsaltany | Rewayat Aldori An Abi Amr',
  'url': 'special://home/addons/plugin.audio.mp3quran/playlists/123.m3u',
  'icon': 'icon.png',
  'disabled': False
}, {
  'name': '124 Muftah Alsaltany | Rewayat AlDorai An Al-Kisaai',
  'url': 'special://home/addons/plugin.audio.mp3quran/playlists/124.m3u',
  'icon': 'icon.png',
  'disabled': False
}, {
  'name': '125 Muftah Alsaltany | Ibn Thakwan An Ibn Amer',
  'url': 'special://home/addons/plugin.audio.mp3quran/playlists/125.m3u',
  'icon': 'icon.png',
  'disabled': False
}, {
  'name': '126 Muftah Alsaltany | Rewayat Hafs An Assem',
  'url': 'special://home/addons/plugin.audio.mp3quran/playlists/126.m3u',
  'icon': 'icon.png',
  'disabled': False
}, {
  'name': '127 Muftah Alsaltany | Shobah An Asim',
  'url': 'special://home/addons/plugin.audio.mp3quran/playlists/127.m3u',
  'icon': 'icon.png',
  'disabled': False
}, {
  'name': '128 Muhammad Al-Hafiz (From Malaysia) | Rewayat Hafs An Assem',
  'url': 'special://home/addons/plugin.audio.mp3quran/playlists/128.m3u',
  'icon': 'icon.png',
  'disabled': False
}, {
  'name': '129 Muhammed Khairul Anuar (From Malaysia) | Rewayat Hafs An Assem',
  'url': 'special://home/addons/plugin.audio.mp3quran/playlists/129.m3u',
  'icon': 'icon.png',
  'disabled': False
}, {
  'name': '130 Mustafa Al-Lahoni | Rewayat Hafs An Assem',
  'url': 'special://home/addons/plugin.audio.mp3quran/playlists/130.m3u',
  'icon': 'icon.png',
  'disabled': False
}, {
  'name': '131 Mustafa Ismail | Rewayat Hafs An Assem',
  'url': 'special://home/addons/plugin.audio.mp3quran/playlists/131.m3u',
  'icon': 'icon.png',
  'disabled': False
}, {
  'name': '132 Mustafa raad Alazawy | Rewayat Hafs An Assem',
  'url': 'special://home/addons/plugin.audio.mp3quran/playlists/132.m3u',
  'icon': 'icon.png',
  'disabled': False
}, {
  'name': '133 Nabil Al Rifay | Rewayat Hafs An Assem',
  'url': 'special://home/addons/plugin.audio.mp3quran/playlists/133.m3u',
  'icon': 'icon.png',
  'disabled': False
}, {
  'name': '134 Nasser Al obaid | Rewayat Hafs An Assem',
  'url': 'special://home/addons/plugin.audio.mp3quran/playlists/134.m3u',
  'icon': 'icon.png',
  'disabled': False
}, {
  'name': '135 Nasser Alqatami | Rewayat Hafs An Assem',
  'url': 'special://home/addons/plugin.audio.mp3quran/playlists/135.m3u',
  'icon': 'icon.png',
  'disabled': False
}, {
  'name': '136 Neamah Al-Hassan | Rewayat Hafs An Assem',
  'url': 'special://home/addons/plugin.audio.mp3quran/playlists/136.m3u',
  'icon': 'icon.png',
  'disabled': False
}, {
  'name': '137 Omar Al-Qazabri | Rewayat Warsh An Nafi',
  'url': 'special://home/addons/plugin.audio.mp3quran/playlists/137.m3u',
  'icon': 'icon.png',
  'disabled': False
}, {
  'name': '138 Othman Al-Ansary | Rewayat Hafs An Assem',
  'url': 'special://home/addons/plugin.audio.mp3quran/playlists/138.m3u',
  'icon': 'icon.png',
  'disabled': False
}, {
  'name': '139 Raad Al Kurdi | Rewayat Hafs An Assem',
  'url': 'special://home/addons/plugin.audio.mp3quran/playlists/139.m3u',
  'icon': 'icon.png',
  'disabled': False
}, {
  'name': '140 Rachid Belalya | Rewayat Hafs An Assem',
  'url': 'special://home/addons/plugin.audio.mp3quran/playlists/140.m3u',
  'icon': 'icon.png',
  'disabled': False
}, {
  'name': '141 Ramadan Shakoor | Rewayat Hafs An Assem',
  'url': 'special://home/addons/plugin.audio.mp3quran/playlists/14.m3u',
  'icon': 'icon.png',
  'disabled': False
}, {
  'name': '142 Rami Aldeais | Rewayat Hafs An Assem',
  'url': 'special://home/addons/plugin.audio.mp3quran/playlists/142.m3u',
  'icon': 'icon.png',
  'disabled': False
}, {
  'name': '143 Rasheed Ifrad | Rewayat Warsh An Nafi',
  'url': 'special://home/addons/plugin.audio.mp3quran/playlists/143.m3u',
  'icon': 'icon.png',
  'disabled': False
}, {
  'name': '144 Rodziah Abdulrahman (From Malaysia) | Rewayat Hafs An Assem',
  'url': 'special://home/addons/plugin.audio.mp3quran/playlists/144.m3u',
  'icon': 'icon.png',
  'disabled': False
}, {
  'name': '145 Rogayah Sulong (From Malaysia) | Rewayat Hafs An Assem',
  'url': 'special://home/addons/plugin.audio.mp3quran/playlists/145.m3u',
  'icon': 'icon.png',
  'disabled': False
}, {
  'name': '146 Saad Al-Ghamdi | Rewayat Hafs An Assem',
  'url': 'special://home/addons/plugin.audio.mp3quran/playlists/146.m3u',
  'icon': 'icon.png',
  'disabled': False
}, {
  'name': '147 Saber Abdulhakm | Rewayat Hafs An Assem',
  'url': 'special://home/addons/plugin.audio.mp3quran/playlists/147.m3u',
  'icon': 'icon.png',
  'disabled': False
}, {
  'name': '148 Sahl Yassin | Rewayat Hafs An Assem',
  'url': 'special://home/addons/plugin.audio.mp3quran/playlists/148.m3u',
  'icon': 'icon.png',
  'disabled': False
}, {
  'name': '149 Saidin Abdulrahman (From Malaysia) | Rewayat Hafs An Assem',
  'url': 'special://home/addons/plugin.audio.mp3quran/playlists/149.m3u',
  'icon': 'icon.png',
  'disabled': False
}, {
  'name': '150 Salah Albudair | Rewayat Hafs An Assem',
  'url': 'special://home/addons/plugin.audio.mp3quran/playlists/150.m3u',
  'icon': 'icon.png',
  'disabled': False
}, {
  'name': '151 Salah Alhashim | Rewayat Qalon An Nafi',
  'url': 'special://home/addons/plugin.audio.mp3quran/playlists/151.m3u',
  'icon': 'icon.png',
  'disabled': False
}, {
  'name': '152 Salah Alhashim | Rewayat Hafs An Assem',
  'url': 'special://home/addons/plugin.audio.mp3quran/playlists/15.m3u',
  'icon': 'icon.png',
  'disabled': False
}, {
  'name': '153 Saleh Al-Habdan | Rewayat Hafs An Assem',
  'url': 'special://home/addons/plugin.audio.mp3quran/playlists/153.m3u',
  'icon': 'icon.png',
  'disabled': False
}, {
  'name': '154 Saleh Al-Talib | Rewayat Hafs An Assem',
  'url': 'special://home/addons/plugin.audio.mp3quran/playlists/154.m3u',
  'icon': 'icon.png',
  'disabled': False
}, {
  'name': '155 Saleh Alsahood | Rewayat Hafs An Assem',
  'url': 'special://home/addons/plugin.audio.mp3quran/playlists/155.m3u',
  'icon': 'icon.png',
  'disabled': False
}, {
  'name': '156 Sami Al-Dosari | Rewayat Hafs An Assem',
  'url': 'special://home/addons/plugin.audio.mp3quran/playlists/156.m3u',
  'icon': 'icon.png',
  'disabled': False
}, {
  'name': '157 Sami Al-Hasn | Rewayat Hafs An Assem',
  'url': 'special://home/addons/plugin.audio.mp3quran/playlists/157.m3u',
  'icon': 'icon.png',
  'disabled': False
}, {
  'name': '158 Sapinah Mamat (From Malaysia) | Rewayat Hafs An Assem',
  'url': 'special://home/addons/plugin.audio.mp3quran/playlists/158.m3u',
  'icon': 'icon.png',
  'disabled': False
}, {
  'name': '159 Saud Al-Shuraim | Rewayat Hafs An Assem',
  'url': 'special://home/addons/plugin.audio.mp3quran/playlists/159.m3u',
  'icon': 'icon.png',
  'disabled': False
}, {
  'name': '160 Sayeed Ramadan | Rewayat Hafs An Assem',
  'url': 'special://home/addons/plugin.audio.mp3quran/playlists/160.m3u',
  'icon': 'icon.png',
  'disabled': False
}, {
  'name': '161 Shaban Al-Sayiaad | Rewayat Hafs An Assem',
  'url': 'special://home/addons/plugin.audio.mp3quran/playlists/161.m3u',
  'icon': 'icon.png',
  'disabled': False
}, {
  'name': '162 Shaik Abu Bakr Al Shatri | Rewayat Hafs An Assem',
  'url': 'special://home/addons/plugin.audio.mp3quran/playlists/162.m3u',
  'icon': 'icon.png',
  'disabled': False
}, {
  'name': '163 Shirazad Taher | Rewayat Hafs An Assem',
  'url': 'special://home/addons/plugin.audio.mp3quran/playlists/163.m3u',
  'icon': 'icon.png',
  'disabled': False
}, {
  'name': '164 Slaah Bukhatir | Rewayat Hafs An Assem',
  'url': 'special://home/addons/plugin.audio.mp3quran/playlists/164.m3u',
  'icon': 'icon.png',
  'disabled': False
}, {
  'name': '165 Tareq Abdulgani daawob | Rewayat Qalon An Nafi',
  'url': 'special://home/addons/plugin.audio.mp3quran/playlists/165.m3u',
  'icon': 'icon.png',
  'disabled': False
}, {
  'name': '166 Tawfeeq As-Sayegh | Rewayat Hafs An Assem',
  'url': 'special://home/addons/plugin.audio.mp3quran/playlists/166.m3u',
  'icon': 'icon.png',
  'disabled': False
}, {
  'name': '167 Ustaz Zamri (From Malaysia) | Rewayat Hafs An Assem',
  'url': 'special://home/addons/plugin.audio.mp3quran/playlists/167.m3u',
  'icon': 'icon.png',
  'disabled': False
}, {
  'name': '168 Wadeea Al-Yamani | Rewayat Hafs An Assem',
  'url': 'special://home/addons/plugin.audio.mp3quran/playlists/168.m3u',
  'icon': 'icon.png',
  'disabled': False
}, {
  'name': '169 Waleed Alnaehi | Rewayat Qalon An Nafi Men Tariq Abi Nasheet',
  'url': 'special://home/addons/plugin.audio.mp3quran/playlists/169.m3u',
  'icon': 'icon.png',
  'disabled': False
}, {
  'name': '170 Walid Al-Dulaimi | Rewayat Hafs An Assem',
  'url': 'special://home/addons/plugin.audio.mp3quran/playlists/170.m3u',
  'icon': 'icon.png',
  'disabled': False
}, {
  'name': '171 Wasel Almethen | Rewayat Hafs An Assem',
  'url': 'special://home/addons/plugin.audio.mp3quran/playlists/171.m3u',
  'icon': 'icon.png',
  'disabled': False
}, {
  'name': '172 Wishear Hayder Arbili | Rewayat Hafs An Assem',
  'url': 'special://home/addons/plugin.audio.mp3quran/playlists/172.m3u',
  'icon': 'icon.png',
  'disabled': False
}, {
  'name': '173 Yahya Hawwa | Rewayat Hafs An Assem',
  'url': 'special://home/addons/plugin.audio.mp3quran/playlists/173.m3u',
  'icon': 'icon.png',
  'disabled': False
}, {
  'name': '174 Yasser Al-Dosari | Rewayat Hafs An Assem',
  'url': 'special://home/addons/plugin.audio.mp3quran/playlists/174.m3u',
  'icon': 'icon.png',
  'disabled': False
}, {
  'name': '175 Yasser Al-Faylakawi | Rewayat Hafs An Assem',
  'url': 'special://home/addons/plugin.audio.mp3quran/playlists/175.m3u',
  'icon': 'icon.png',
  'disabled': False
}, {
  'name': '176 Yasser Al-Mazroyee | Rewayat Rowis and Rawh An Yakoob Al Hadrami',
  'url': 'special://home/addons/plugin.audio.mp3quran/playlists/176.m3u',
  'icon': 'icon.png',
  'disabled': False
}, {
  'name': '177 Yasser Al-Qurashi | Rewayat Hafs An Assem',
  'url': 'special://home/addons/plugin.audio.mp3quran/playlists/177.m3u',
  'icon': 'icon.png',
  'disabled': False
}, {
  'name': '178 Yasser Salamah | Rewayat Hafs An Assem',
  'url': 'special://home/addons/plugin.audio.mp3quran/playlists/178.m3u',
  'icon': 'icon.png',
  'disabled': False
}, {
  'name': '179 Yousef Alshoaey | Rewayat Hafs An Assem',
  'url': 'special://home/addons/plugin.audio.mp3quran/playlists/179.m3u',
  'icon': 'icon.png',
  'disabled': False
}, {
  'name': '180 Yousef Bin Noah Ahmad | Rewayat Hafs An Assem',
  'url': 'special://home/addons/plugin.audio.mp3quran/playlists/180.m3u',
  'icon': 'icon.png',
  'disabled': False
}, {
  'name': '181 Youssef Edghouch | Rewayat Hafs An Assem',
  'url': 'special://home/addons/plugin.audio.mp3quran/playlists/181.m3u',
  'icon': 'icon.png',
  'disabled': False
}, {
  'name': '182 Zakaria Hamamah | Rewayat Hafs An Assem',
  'url': 'special://home/addons/plugin.audio.mp3quran/playlists/182.m3u',
  'icon': 'icon.png',
  'disabled': False
}, {
  'name': '183 Zaki Daghistani | Rewayat Hafs An Assem',
  'url': 'special://home/addons/plugin.audio.mp3quran/playlists/183.m3u',
  'icon': 'icon.png',
  'disabled': False
},]


rdio = [{
  'name': '001 Abdullah Basfer [English Translation]',
  'url': 'http://live.mp3quran.net:9754',
  'icon': 'icon.png',
  'disabled': False
},{
  'name': '002 AbdulBaset AbdulSamad with Naeem Sultan [Pickthall Translation](English)',
  'url': 'http://live.mp3quran.net:9748',
  'icon': 'icon.png',
  'disabled': False
},{
  'name': '003 AbdulBaset AbdulSamad with Ibrahim Walk [Saheeh Intl Translation(English)]',
  'url': 'http://live.mp3quran.net:9746',
  'icon': 'icon.png',
  'disabled': False
},{
  'name': '004 Main Radio',
  'url': 'http://live.mp3quran.net:8006',
  'icon': 'icon.png',
  'disabled': False
},{
  'name': '005 Beautiful Recitations',
  'url': 'http://live.mp3quran.net:9992',
  'icon': 'icon.png',
  'disabled': False
},{
  'name': '006 Maher Al Meaqli Radio',
  'url': 'http://live.mp3quran.net:9996',
  'icon': 'icon.png',
  'disabled': False
},{
  'name': '007 Ahmad Al-Ajmy Radio',
  'url': 'http://live.mp3quran.net:9990',
  'icon': 'icon.png',
  'disabled': False
},{
  'name': '008 Abdulrahman Alsudaes Radio',
  'url': 'http://live.mp3quran.net:9988',
  'icon': 'icon.png',
  'disabled': False
},{
  'name': '009 Saud Al-Shuraim Radio',
  'url': 'http://live.mp3quran.net:9986',
  'icon': 'icon.png',
  'disabled': False
},{
  'name': '010 Yasser Al-Dosari Radio',
  'url': 'http://live.mp3quran.net:9984',
  'icon': 'icon.png',
  'disabled': False
},{
  'name': '011  Mishary Al Afasi Radio',
  'url': 'http://live.mp3quran.net:9982',
  'icon': 'icon.png',
  'disabled': False
},{
  'name': '012 Abdulbasit Abdulsamad Radio',
  'url': 'http://live.mp3quran.net:9980',
  'icon': 'icon.png',
  'disabled': False
},{
  'name': '013 Nasser Alqatami Radio',
  'url': 'http://live.mp3quran.net:9994',
  'icon': 'icon.png',
  'disabled': False
},{
  'name': '014 Mohammed Siddiq Al-Minshawi Radio',
  'url': 'http://live.mp3quran.net:9978',
  'icon': 'icon.png',
  'disabled': False
},{
  'name': '015 Saad Al-Ghamdi Radio',
  'url': 'http://live.mp3quran.net:9976',
  'icon': 'icon.png',
  'disabled': False
},{
  'name': '016 Abdulbasit Abdulsamad - MJAWOAD Radio',
  'url': 'http://live.mp3quran.net:9974',
  'icon': 'icon.png',
  'disabled': False
},{
  'name': '017 Khaled Al-Qahtani Radio',
  'url': 'http://live.mp3quran.net:9970',
  'icon': 'icon.png',
  'disabled': False
},{
  'name': '018 Fares Abbad Radio',
  'url': 'http://live.mp3quran.net:9972',
  'icon': 'icon.png',
  'disabled': False
},{
  'name': '019 Idrees Abkr Radio',
  'url': 'http://live.mp3quran.net:9968',
  'icon': 'icon.png',
  'disabled': False
},{
  'name': '020 Shaik Abu Bakr Al Shatri Radio',
  'url': 'http://live.mp3quran.net:9966',
  'icon': 'icon.png',
  'disabled': False
},{
  'name': '021 Ali Jaber Radio',
  'url': 'http://live.mp3quran.net:9964',
  'icon': 'icon.png',
  'disabled': False
},{
  'name': '022 Mohammad Jibreel Radio',
  'url': 'http://live.mp3quran.net:9962',
  'icon': 'icon.png',
  'disabled': False
},{
  'name': '023 Mahmoud Khalil Al-Hussary Radio',
  'url': 'http://live.mp3quran.net:9958',
  'icon': 'icon.png',
  'disabled': False
},{
  'name': '024 Mohammad Ayyub Radio',
  'url': 'http://live.mp3quran.net:9960',
  'icon': 'icon.png',
  'disabled': False
},{
  'name': '025 Abdulbasit Abdulsamad (Warsh An Nafi) Radio',
  'url': 'http://live.mp3quran.net:9954',
  'icon': 'icon.png',
  'disabled': False
},{
  'name': '026 Abdullah Basfer',
  'url': 'http://live.mp3quran.net:9748',
  'icon': 'icon.png',
  'disabled': False
},{
  'name': '027 Saber Abdulhakm Radio',
  'url': 'http://live.mp3quran.net:9952',
  'icon': 'icon.png',
  'disabled': False
},{
  'name': '028 Jamaan Alosaimi Radio',
  'url': 'http://live.mp3quran.net:9950',
  'icon': 'icon.png',
  'disabled': False
},{
  'name': '029 Abduulah Kayyat',
  'url': 'http://live.mp3quran.net:9948',
  'icon': 'icon.png',
  'disabled': False
},{
  'name': '030 Ibrahim Al-Akder',
  'url': 'http://live.mp3quran.net:9946',
  'icon': 'icon.png',
  'disabled': False
},{
  'name': '031 Abdullah Aljohani',
  'url': 'http://live.mp3quran.net:9944',
  'icon': 'icon.png',
  'disabled': False
},{
  'name': '032 Ahmad Al-Hawashi',
  'url': 'http://live.mp3quran.net:9928',
  'icon': 'icon.png',
  'disabled': False
},{
  'name': '033 Ahmed Al-trabulsi',
  'url': 'http://live.mp3quran.net:9926',
  'icon': 'icon.png',
  'disabled': False
},{
  'name': '034 Ahmad Khader Al-Tarabulsi - Qalon An Nafi',
  'url': 'http://live.mp3quran.net:9924',
  'icon': 'icon.png',
  'disabled': False
},{
  'name': '035 Ahmad Saber',
  'url': 'http://live.mp3quran.net:9922',
  'icon': 'icon.png',
  'disabled': False
},{
  'name': '036 Ahmed Amer',
  'url': 'http://live.mp3quran.net:9920',
  'icon': 'icon.png',
  'disabled': False
},{
  'name': '037 Akram Alalaqmi',
  'url': 'http://live.mp3quran.net:9918',
  'icon': 'icon.png',
  'disabled': False
},{
  'name': '038 Addokali Mohammad Alalim - Qalon An Nafi',
  'url': 'http://live.mp3quran.net:9748',
  'icon': 'icon.png',
  'disabled': False
},{
  'name': '039 Alzain Mohammad Ahmad',
  'url': 'http://live.mp3quran.net:9914',
  'icon': 'icon.png',
  'disabled': False
},{
  'name': '040 Aloyoon Al-Koshi - Warsh An Nafi',
  'url': 'http://live.mp3quran.net:9912',
  'icon': 'icon.png',
  'disabled': False
},{
  'name': '041 Alfateh Alzubair - Aldori An Abi Amr',
  'url': 'http://live.mp3quran.net:9910',
  'icon': 'icon.png',
  'disabled': False
},{
  'name': '042 Al-Qaria Yassen - Warsh An Nafi',
  'url': 'http://live.mp3quran.net:9908',
  'icon': 'icon.png',
  'disabled': False
},{
  'name': '043 Tawfeeq As-Sayegh',
  'url': 'http://live.mp3quran.net:9906',
  'icon': 'icon.png',
  'disabled': False
},{
  'name': '044 Ahmad Nauina',
  'url': 'http://live.mp3quran.net:9904',
  'icon': 'icon.png',
  'disabled': False
},{
  'name': '045 Ibrahim Aldosari - Warsh An Nafi',
  'url': 'http://live.mp3quran.net:9902',
  'icon': 'icon.png',
  'disabled': False
},{
  'name': '046 Jamal Shaker Abdullah',
  'url': 'http://live.mp3quran.net:9900',
  'icon': 'icon.png',
  'disabled': False
},{
  'name': '047 Hatem Fareed Alwaer',
  'url': 'http://live.mp3quran.net:9898',
  'icon': 'icon.png',
  'disabled': False
},{
  'name': '048 Khalid Almohana',
  'url': 'http://live.mp3quran.net:9896',
  'icon': 'icon.png',
  'disabled': False
},{
  'name': '049 Khalid Abdulkafi',
  'url': 'http://live.mp3quran.net:9894',
  'icon': 'icon.png',
  'disabled': False
},{
  'name': '050 Khalifa Altunaiji',
  'url': 'http://live.mp3quran.net:9892',
  'icon': 'icon.png',
  'disabled': False
},{
  'name': '051 Zaki Daghistani',
  'url': 'http://live.mp3quran.net:9890',
  'icon': 'icon.png',
  'disabled': False
},{
  'name': '052 Sahl Yassin',
  'url': 'http://live.mp3quran.net:9888',
  'icon': 'icon.png',
  'disabled': False
},{
  'name': '053 Sayeed Ramadan',
  'url': 'http://live.mp3quran.net:9886',
  'icon': 'icon.png',
  'disabled': False
},{
  'name': '054 Shirazad Taher',
  'url': 'http://live.mp3quran.net:9884',
  'icon': 'icon.png',
  'disabled': False
},{
  'name': '055 Salah Albudair',
  'url': 'http://live.mp3quran.net:9882',
  'icon': 'icon.png',
  'disabled': False
},{
  'name': '056 Salah Alhashim',
  'url': 'http://live.mp3quran.net:9880',
  'icon': 'icon.png',
  'disabled': False
},{
  'name': '057 Slaah Bukhatir',
  'url': 'http://live.mp3quran.net:9878',
  'icon': 'icon.png',
  'disabled': False
},{
  'name': '058 Tareq Abdulgani daawob',
  'url': 'http://live.mp3quran.net:9876',
  'icon': 'icon.png',
  'disabled': False
},{
  'name': '059 Adel Al-Khalbany',
  'url': 'http://live.mp3quran.net:9874',
  'icon': 'icon.png',
  'disabled': False
},{
  'name': '060 Adel Ryyan',
  'url': 'http://live.mp3quran.net:9872',
  'icon': 'icon.png',
  'disabled': False
},{
  'name': '061 Abdelbari Al-Toubayti',
  'url': 'http://live.mp3quran.net:9870',
  'icon': 'icon.png',
  'disabled': False
},{
  'name': '062 Abdulbari Mohammad',
  'url': 'http://live.mp3quran.net:9868',
  'icon': 'icon.png',
  'disabled': False
},{
  'name': '063 Abdulrasheed Soufi - Assosi An Abi Amr',
  'url': 'http://live.mp3quran.net:9866',
  'icon': 'icon.png',
  'disabled': False
},{
  'name': '064 Abdulrasheed Soufi - Khalaf An Hamzah',
  'url': 'http://live.mp3quran.net:9864',
  'icon': 'icon.png',
  'disabled': False
},{
  'name': '065 Abdul Aziz Al-Ahmad',
  'url': 'http://live.mp3quran.net:9862',
  'icon': 'icon.png',
  'disabled': False
},{
  'name': '066 Abdullah Al-Kandari',
  'url': 'http://live.mp3quran.net:9860',
  'icon': 'icon.png',
  'disabled': False
},{
  'name': '067 Abdullah Al-Mattrod',
  'url': 'http://live.mp3quran.net:9858',
  'icon': 'icon.png',
  'disabled': False
},{
  'name': '068 Abdulmohsin Al-Harthy',
  'url': 'http://live.mp3quran.net:9856',
  'icon': 'icon.png',
  'disabled': False
},{
  'name': '069 Abdulmohsin Al-Obaikan',
  'url': 'http://live.mp3quran.net:9748',
  'icon': 'icon.png',
  'disabled': False
},{
  'name': '070 Abdulmohsen Al-Qasim',
  'url': 'http://live.mp3quran.net:9852',
  'icon': 'icon.png',
  'disabled': False
},{
  'name': '071 Abdulhadi Kanakeri',
  'url': 'http://live.mp3quran.net:9850',
  'icon': 'icon.png',
  'disabled': False
},{
  'name': '072 Abdulwadood Haneef',
  'url': 'http://live.mp3quran.net:9848',
  'icon': 'icon.png',
  'disabled': False
},{
  'name': '073 Ali Alhuthaifi',
  'url': 'http://live.mp3quran.net:9844',
  'icon': 'icon.png',
  'disabled': False
},{
  'name': '074 Ali Alhuthaifi - Qalon An Nafi',
  'url': 'http://live.mp3quran.net:9846',
  'icon': 'icon.png',
  'disabled': False
},{
  'name': '075 Ali Hajjaj Alsouasi',
  'url': 'http://live.mp3quran.net:9842',
  'icon': 'icon.png',
  'disabled': False
},{
  'name': '076 Emad Hafez',
  'url': 'http://live.mp3quran.net:9840',
  'icon': 'icon.png',
  'disabled': False
},{
  'name': '077 Omar Al-Qazabri - Warsh An Nafi',
  'url': 'http://live.mp3quran.net:9838',
  'icon': 'icon.png',
  'disabled': False
},{
  'name': '078 Maher Shakhashero',
  'url': 'http://live.mp3quran.net:9836',
  'icon': 'icon.png',
  'disabled': False
},{
  'name': '079 Mohammad Al-Tablaway',
  'url': 'http://live.mp3quran.net:9834',
  'icon': 'icon.png',
  'disabled': False
},{
  'name': '080 Mohammed Al-Lohaidan',
  'url': 'http://live.mp3quran.net:9832',
  'icon': 'icon.png',
  'disabled': False
},{
  'name': '081 Mohammad Rashad Alshareef',
  'url': 'http://live.mp3quran.net:9830',
  'icon': 'icon.png',
  'disabled': False
},{
  'name': '082 Mohammad Saleh Alim Shah',
  'url': 'http://live.mp3quran.net:9828',
  'icon': 'icon.png',
  'disabled': False
},{
  'name': '083 Mohammed Siddiq Al-Minshawi - MJWD',
  'url': 'http://live.mp3quran.net:9826',
  'icon': 'icon.png',
  'disabled': False
},{
  'name': '084 Mohammad Abdullkarem',
  'url': 'http://live.mp3quran.net:9824',
  'icon': 'icon.png',
  'disabled': False
},{
  'name': '085 Mohammad Abdullkarem - Warsh An Nafi Men Tariq Abi Baker Alasbahani',
  'url': 'http://live.mp3quran.net:9822',
  'icon': 'icon.png',
  'disabled': False
},{
  'name': '086 Mohammed Osman Khan (from India)',
  'url': 'http://live.mp3quran.net:9820',
  'icon': 'icon.png',
  'disabled': False
},{
  'name': '087 Mahmood Al rifai',
  'url': 'http://live.mp3quran.net:9818',
  'icon': 'icon.png',
  'disabled': False
},{
  'name': '088 Mohammad Al-Abdullah - AlDorai An Al-Kisaai',
  'url': 'http://live.mp3quran.net:9816',
  'icon': 'icon.png',
  'disabled': False
},{
  'name': '089 Mohammad Al-Abdullah - Albizi and Qunbol An Ibn Katheer',
  'url': 'http://live.mp3quran.net:9814',
  'icon': 'icon.png',
  'disabled': False
},{
  'name': '090 Mahmood AlSheimy - AlDorai An Al-Kisaai',
  'url': 'http://live.mp3quran.net:9812',
  'icon': 'icon.png',
  'disabled': False
},{
  'name': '091 Mahmoud Ali Albanna - MJWD',
  'url': 'http://live.mp3quran.net:9810',
  'icon': 'icon.png',
  'disabled': False
},{
  'name': '092 Mahmoud Ali Albanna',
  'url': 'http://live.mp3quran.net:9808',
  'icon': 'icon.png',
  'disabled': False
},{
  'name': '093 Mahmoud Khalil Al-Hussary - MJWD',
  'url': 'http://live.mp3quran.net:9806',
  'icon': 'icon.png',
  'disabled': False
},{
  'name': '094 Mahmoud Khalil Al-Hussary - Warsh An Nafi',
  'url': 'http://live.mp3quran.net:9804',
  'icon': 'icon.png',
  'disabled': False
},{
  'name': '095 Moeedh Alharthi',
  'url': 'http://live.mp3quran.net:9802',
  'icon': 'icon.png',
  'disabled': False
},{
  'name': '096 Mustafa Ismail',
  'url': 'http://live.mp3quran.net:9800',
  'icon': 'icon.png',
  'disabled': False
},{
  'name': '097 Mustafa Al-Lahoni',
  'url': 'http://live.mp3quran.net:9798',
  'icon': 'icon.png',
  'disabled': False
},{
  'name': '098 Mustafa raad Alazawy',
  'url': 'http://live.mp3quran.net:9796',
  'icon': 'icon.png',
  'disabled': False
},{
  'name': '099 Muftah Alsaltany - Ibn Thakwan An Ibn Amer',
  'url': 'http://live.mp3quran.net:9794',
  'icon': 'icon.png',
  'disabled': False
},{
  'name': '100 Muftah Alsaltany',
  'url': 'http://live.mp3quran.net:9792',
  'icon': 'icon.png',
  'disabled': False
},{
  'name': '101 Muftah Alsaltany - Aldori An Abi Amr',
  'url': 'http://live.mp3quran.net:9790',
  'icon': 'icon.png',
  'disabled': False
},{
  'name': '102 Muftah Alsaltany - AlDorai An Al-Kisaai',
  'url': 'http://live.mp3quran.net:9788',
  'icon': 'icon.png',
  'disabled': False
},{
  'name': '103 Mousa Bilal',
  'url': 'http://live.mp3quran.net:9786',
  'icon': 'icon.png',
  'disabled': False
},{
  'name': '104 Nabil Al Rifay',
  'url': 'http://live.mp3quran.net:9784',
  'icon': 'icon.png',
  'disabled': False
},{
  'name': '105 Neamah Al-Hassan',
  'url': 'http://live.mp3quran.net:9782',
  'icon': 'icon.png',
  'disabled': False
},{
  'name': '106 Hani Arrifai',
  'url': 'http://live.mp3quran.net:9780',
  'icon': 'icon.png',
  'disabled': False
},{
  'name': '107 Waleed Alnaehi - Qalon An Nafi Men Tariq Abi Nasheet',
  'url': 'http://live.mp3quran.net:9778',
  'icon': 'icon.png',
  'disabled': False
},{
  'name': '108 Yasser Al-Qurashi',
  'url': 'http://live.mp3quran.net:9776',
  'icon': 'icon.png',
  'disabled': False
},{
  'name': '109 Yasser Al-Mazroyee - Rowis and Rawh An Yakoob Al Hadrami',
  'url': 'http://live.mp3quran.net:9774',
  'icon': 'icon.png',
  'disabled': False
},{
  'name': '110 Yahya Hawwa',
  'url': 'http://live.mp3quran.net:9748',
  'icon': 'icon.png',
  'disabled': False
},{
  'name': '111 Yousef Alshoaey',
  'url': 'http://live.mp3quran.net:9770',
  'icon': 'icon.png',
  'disabled': False
},{
  'name': '112 Yousef Bin Noah Ahmad',
  'url': 'http://live.mp3quran.net:9768',
  'icon': 'icon.png',
  'disabled': False
},]


streams = {
  'rctr': sorted((i for i in rctr if not i.get('disabled', False)), key=lower_getter('name')),
  'rdio': sorted((i for i in rdio if not i.get('disabled', False)), key=lower_getter('name')),
  # 'rctr': sorted(rctr, key=lower_getter('name')),
  # 'rdio': sorted(rdio, key=lower_getter('name')),
}

PARAMS = get_params()
TAG = None
logging.warning('PARAMS!!!! %s', PARAMS)

try:
  TAG = PARAMS['tag']
except:
  pass

logging.warning('ARGS!!!! sys.argv %s', sys.argv)

if TAG == None:
  show_tags()
else:
  show_streams(TAG)
