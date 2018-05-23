def qfunction(text):

    text = text.lower()

    while "  " in text:
        text = text.replace("  ", " ")

    if text[:1] == " ":
        text = text[1:]

    for char in ["?", ".", "!", ","]:
        text = text.replace(char, "")

# Replace common apostrophised words
    text = text.replace("you're", "you-are")
    text = text.replace("what's", "what-is")
    text = text.replace("i'm", "i-am")
    text = text.replace("can't", "cannot")
    text = text.replace("don't", "do-not")
    text = text.replace("i'll", "i-will")
    text = text.replace("i'd", "i-would")
    text = text.replace("that's", "that-is")
    text = text.replace("who's", "who-is")

    # Eliminate common work pairs to reduce vocabulary
    text = text.replace("you are", "you-are")
    text = text.replace("what is", "what-is")
    text = text.replace("i am", "i-am")
    text = text.replace("can not", "cannot")
    text = text.replace("do not", "do-not")
    text = text.replace("i will", "i-will")
    text = text.replace("i would", "i-would")
    text = text.replace("that is", "that-is")
    text = text.replace("who is", "who-is")
    text = text.replace("thank you", "thanks")

    # Remove punctuation as it doesn't add meaning
    text = text.replace("?", "")
    text = text.replace("!", "")
    text = text.replace("'", "")
    text = text.replace(".", "")
    text = text.replace(",","")

    # Elimenate un-necessary white space
    while "  " in text:
        text = text.replace("  "," ")
    while text.endswith(" "):
        text = text[:-1]
    while text.startswith(" "):
        text = text[1:]

    # Replace common American Spelling differences
    text = text.replace(" airplane ", " aeroplane ")
    text = text.replace(" apartment ", " flat ")
    text = text.replace(" apologize ", " apologise ")
    text = text.replace(" automobile ", " car ")
    text = text.replace(" candy ", " sweets ")
    text = text.replace(" center ", " centre ")
    text = text.replace(" color ", " colour ")
    text = text.replace(" cookie ", " biscuit ")
    text = text.replace(" diaper ", " nappy ")
    text = text.replace(" elevator ", " lift ")
    text = text.replace(" eraser ", " rubber ")
    text = text.replace(" favor ", " favour ")
    text = text.replace(" garbage ", " rubbish ")
    text = text.replace(" gray ", " grey ")
    text = text.replace(" humor ", " humour ")
    text = text.replace(" mail ", " post ")
    text = text.replace(" meter ", " metre ")
    text = text.replace(" neighbor ", " neighbour ")
    text = text.replace(" odor ", " odour ")
    text = text.replace(" parlor ", " parlour ")
    text = text.replace(" popsicle ", " ice lolly ")
    text = text.replace(" program ", " programme ")
    text = text.replace(" restroom ", " loo ")
    text = text.replace(" subway ", " underground ")
    text = text.replace(" theater ", " theatre ")
    text = text.replace(" tire ", " tyre ")
    text = text.replace(" truck ", " lorry ")
    text = text.replace(" vacation ", " holiday ")

    # Replace common American Spelling differences - plurals
    text = text.replace(" airplanes ", " aeroplanes ")
    text = text.replace(" apartments ", " flats ")
    text = text.replace(" apologizes ", " apologises ")
    text = text.replace(" automobiles ", " cars ")
    text = text.replace(" candies ", " sweets ")
    text = text.replace(" centers ", " centres ")
    text = text.replace(" colors ", " colours ")
    text = text.replace(" cookies ", " biscuits ")
    text = text.replace(" diapers ", " nappies ")
    text = text.replace(" elevators ", " lifts ")
    text = text.replace(" erasers ", " rubbers ")
    text = text.replace(" favors ", " favours ")
    text = text.replace(" humorous ", " humourous ")
    text = text.replace(" mails ", " posts ")
    text = text.replace(" meters ", " metres ")
    text = text.replace(" neighbors ", " neighbours ")
    text = text.replace(" odors ", " odours ")
    text = text.replace(" parlors ", " parlours ")
    text = text.replace(" popsicles ", " ice lollies ")
    text = text.replace(" programs ", " programmes ")
    text = text.replace(" restrooms ", " loos ")
    text = text.replace(" subways ", " undergrounds ")
    text = text.replace(" theaters ", " theatres ")
    text = text.replace(" tires ", " tyres ")
    text = text.replace(" trucks ", " lorries ")
    text = text.replace(" vacations ", " holidays ")


    # Replace common slang words
    text = text.replace(" doin ", " doing ")
    text = text.replace(" bucks ", " dollars ")
    text = text.replace(" buck ", " dollar ")
    text = text.replace(" quid ", " pounds ")



    # Get rid of word pairs to reduce vocab

    text = text.replace("bletchley park", "bletchley")
    text = text.replace("winston churchill", "churchill")
    text = text.replace("joan clarke", "joan")
    text = text.replace("joan murray", "joan")
    text = text.replace("thank you", "thankyou")
    text = text.replace("that is", "thatis")
    text = text.replace("who is", "whois")
    text = text.replace("alan turing", "alanturing")
    text = text.replace("alan mathison turing", "alanturing")
    text = text.replace("christpoher morcom", "christophermorcom")
    text = text.replace("hugh alexander", "hughalexander")
    text = text.replace("harry golombeck", "harrygolombeck")
    text = text.replace("gordon welshman", "gordonwelshman")
    text = text.replace("benedict cumberbatch", "benedictcumberbatch")
    text = text.replace("prime minister", "primeminister")
    text = text.replace("her maiden name", "her-maiden-name")
    text = text.replace("second world war", "secondworldwar")
    text = text.replace("wwii", "secondworldwar")
    text = text.replace("ww ii", "secondworldwar")
    text = text.replace("world war two", "secondworldwar")
    text = text.replace("world war 2", "secondworldwar")
    text = text.replace("ww2", "secondworldwar")
    text = text.replace("ww 2", "secondworldwar")
    text = text.replace("spinal cord", "spinalcord")
    text = text.replace("stanley eddington", "stanleyeddington")
    text = text.replace("sir stanleyeddington", "stanleyeddington")
    text = text.replace("newtons first law", "newtons-first-law")
    text = text.replace("newtons second law", "newtons-second-law")
    text = text.replace("newtons third law", "newtons-third-law")
    text = text.replace("prime numbers", "prime-numbers")
    text = text.replace("prime number", "prime-number")

    return text

def afunction(text):
    text = text.replace("Ph.D.", "PhD")
    text = text.replace("Ph. D.", "PhD")
    text = text.replace("Second World War", "WW-II")
    text = text.replace("second world war", "WW-II")
    text = text.replace(".", " .")
    text = text.replace("?", " ?")
    text = text.replace(",", " ,")
    while "  " in text:
        text = text.replace("  "," ")
    while text.endswith(" "):
        text = text[:-1]
    while text.startswith(" "):
        text = text[1:]

    return text

question ="         What is your name?!.,"
answer = "My name is Alan Turing."

print qfunction(question)
print afunction(answer)
