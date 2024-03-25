import re

############### Task 1 ################
text=" Archaeologists have found evidence for human occupation of Mongolia starting in the Lower Paleolithic (perhaps 500,000 years ago). \
The area has shown evidence of human occupation ever since. Before GENGHIS Khan, the Mongolian nomads followed a typical pattern of nomadic peoples, \
alternating between vast empires and small-scale tribal organization. The first empire was built by the Hunnu, a proto-Mongolian tribe. \
The Hunnu Empire (3rd century BCE-1st century CE) played a major role in shaping the social and political structures of Central Asian nomadic tribes."

results = {
    "Result 1": re.findall('[a-zA-Z0-9]+',text),
    "Result 2": re.findall('[a-z]+',text),
    "Result 3": re.findall('[A-Z]+',text),
    "Result 4": re.findall('[0-9]+',text),

    "Result 5": re.findall('\d+', text),
    "Result 6": re.findall('\d*', text),
    "Result 7": re.findall('\D+', text),
    "Result 8": re.findall('\D*', text),
    "Result 9": re.findall('\w', text),
    "Result 10": re.findall('\w+', text),
    "Result 11": re.findall('\w*', text),
    "Result 12": re.findall('\W+', text),
    "Result 13": re.findall('\W*', text),
    "Result 14": re.findall('\s\w+', text),

    "Result 15": re.findall('[^aeiou]+',text),
    "Result 16": re.findall('[$aeiou]+',text),
    "Result 17": re.findall('G?E+',text),
    "Result 18": re.findall('\w+.an+',text),

    "Result 19": re.findall('\w+c{1,3}\w+',text),
    "Result 20": re.findall('\w+c{1,}\w+',text),
    "Result 21": re.findall('\w+c{,3}\w+',text),
    "Result 22": re.findall('\w+c{2}\w+',text),

    "Result 23": re.findall('(?<=GENGHIS\s)Khan',text),
    "Result 24": re.findall('\d+(?=rd\s)',text),
    "Result 25": re.findall('(?<!GENGHIS)Khan',text),
    "Result 26": re.findall('\d+(?!rd)',text),
    "Result 27": re.findall(r'\bG\w+', text)
}

# Print results
for key, value in results.items():
    print(f"{key}: {value}")