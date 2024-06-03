import json
from mdutils.mdutils import MdUtils

if __name__ == "__main__":
    mdFile = MdUtils(file_name='README.md', title='AI Text to Speech Voices')
    mdFile.new_line("This is a list of all the available text to speech voices in the API with their audio samples.")
    mdFile.new_line("Use Voice ID and Narration Styles (for supported voices) from this list to reference a voice and a narration style, respectively, in your calls to the API. You can also listen to a sample of each voice through its Sample URL.")
    with open('list.json', 'r') as f:
        voices:list[dict] = json.load(f)['voices']
    voices = sorted(voices, key=lambda voice: (voice['language'], voice['gender']))
    header = ['Voice ID', 'Voice Nmae', 'Language', 'Gender', 'Sample']
    list_of_strings = []
    for voice in voices:
        list_of_strings.extend([voice.get('value'), 
                                voice.get('name'), 
                                voice.get('language'), 
                                voice.get('gender'), 
                                mdFile.new_inline_link(link=voice.get('sample'), text='sample')])
    list_of_strings = header + list_of_strings
    print(len(header), len(voices)+1, len(header)*(len(voices)+1))  
    print(len(list_of_strings))
    mdFile.new_table(columns=len(header), rows=len(voices)+1, text=list_of_strings, text_align='left')
    
    mdFile.create_md_file()