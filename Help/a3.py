# a3.py
# STUDENTS: update the next three lines and then delete this one
# PUT YOUR NAME(S) AND NETID(S) HERE
# Sources/people consulted:  STUDENTS: FILL IN OR WRITE "NONE"
# PUT DATE YOU COMPLETED THIS HERE
# Skeleton by Lillian Lee (LJL2) and Victoria Litvinova (VL242), Mar 22 2018

import urllib.request  # Get vocabulary from a webpage
import string  # Get some useful string built-in values
import os
import sys

from sources import econ_terms# BEGIN REMOVE
ECON_DATA_FNAME = os.path.join('econ_terms_scratch', 'econ_vocab_data.txt')
ECON_VOCAB = econ_terms.ECON_VOCAB

#  STUDENTS: this function has been completed for you.
def get_content_lines(fname=None):
    output = []  # Initialize our accumulator

    # This is how to check if something is None (Pythonistas don't use == here.)
    if fname is None:
        # Fill in fname using a visual dialog window
        fname = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")],
                                           title="Choose an input file")

    # About open(), see section 9.1 "Reading word lists" of the text.
    # "with" makes sure file opening and closing is cleanly done.
    # The 'r' means can only read the file, not change it
    with open(fname, mode='r', encoding='utf-8') as fp:

        # See Section 13.3 "Word histogram" on looping through a file's lines
        for line in fp:
            left_justified_line = line.lstrip()  # Remove leading whitespace
            if len(left_justified_line) == 0 or left_justified_line[0] != '#':
                # Either line was empty or it wasn't a comment.
                line = line.replace('-', ' ')
                words_in_line = line.split()
                for ind in range(len(words_in_line)):
                    word = words_in_line[ind].strip()
                    word = word.strip(string.punctuation + string.whitespace)
                    word = word.lower()
                    words_in_line[ind] = word  # Replace with normalized version
                output.append(' '.join(words_in_line) + '\n')
    return output


def convert_lines_to_string(linelist):
    newString = ""
    for value in linelist:
        if value:
            if value[-1:] == '\n':
                value = value[:-1]
            stringValue = str(value).strip()
            newString = newString + ' ' + stringValue
    return newString[1:] #Removes leading white space


def convert_lines_to_string2(linelist):
    """Same specification as convert_lines_to_string()"""
    newString = ""
    for index in list(range(len(linelist))):
        #Index is now 0, 1 ...
        if linelist[index]:  # Ignores strings = '' but not '\n'
            if linelist[index] == '\n':
                linelist[index] = linelist[index][:-1]
            stringValue = str(linelist[index]).strip()
            newString = newString + ' ' + stringValue
    return newString[1:]


def convert_lines_to_paragraphs(linelist):
    convertedList = []
    stanzaSentences = []
    linelist.append('\n') # The way the code is set up is that it will generate a new part of the convertedlist only if it comes across a '\n' as an individual element in the linelist
    for part in linelist:
        if part != '\n':
            stanzaSentences.append(part)
        elif stanzaSentences:
            combined = ""
            for line in stanzaSentences:
                fixedLine  = convert_lines_to_string(line.split(" "))
                combined += " " + fixedLine.strip()
            convertedList.append(combined[1:]) # [1:] to remove leading white space
            stanzaSentences = []
    return convertedList


def download_econ_vocab_data(fname):
    """(over)write into file fname the concatenation of text regarding
    economics-related terminology text from
        https://www.economist.com/economics-a-to-z/a
        https://www.economist.com/economics-a-to-z/b
        ...
        https://www.economist.com/economics-a-to-z/z

    Preconditions: directory econ_dict exists in the same directory as this file.
    """
    with open(fname, mode='a+', encoding='utf-8') as fp:

        # Isn't it handy to be able to loop through strings?
        for letter in string.ascii_lowercase:
            # You can check that this is like what we did in A1, file
            # get_status_from_webpage.py
            data_name = 'https://www.economist.com/economics-a-to-z/'
            try:
                data_source = urllib.request.urlopen(data_name + letter)
                fp.write(data_source.read().decode('utf-8'))
                fp.write('\n\n')  # have a separator between webpages
            except ValueError:
                print("Something is wrong with the web address or webpage.")
                sys.exit()


def get_econ_vocab_helper(vlist_to_add_to, work_text):
    """Extends vlist_to_add_to with the list of the vocabulary items,
    lower-cased, in work_text, assumed to be well-formatted html"""

    # Add each <h2>...</h2> term or phrase to vlist_to_add_to, separating out
    # comma-separated phrases.

    i_start = work_text.find('<h2>')
    if i_start == -1:
        # No more <h2> tags, all done
        return
    else:
        work_text = work_text[i_start + len('<h2>'):]
        try:
            i_end = work_text.index('</h2>')  # If no matching </h2>,
                                              # quit because the data is corrupt
        except:
            print('ˆData has a <h2> without matching </h2>.')
            sys.exit()
        # Deal with "G7, G8, G20"
        term_list = work_text[:i_end].split(',')
        for term in term_list:
            vlist_to_add_to.append(term.lower().strip())
        work_text = work_text[i_end + len('</h2>') + 1:]

        # Recursive call!
        get_econ_vocab_helper(vlist_to_add_to, work_text)


def get_econ_vocab(fname):
    """Returns a list of the vocabulary items in fname, lower-cased."""
    with open(fname, mode='r', encoding='utf-8') as fp:
        outlist = []
        get_econ_vocab_helper(outlist, fp.read())
        return outlist

def track_topic(docs_list, vocab_list):
    counter = 0
    stripped = docs_list[0].split(" ")
    fixStripped = []
    for word in stripped: # Make a copy of original string to fix
        if word:  # Not empty string is good
            fixStripped.append(word)
    for word in fixStripped:
        if word in vocab_list:
            counter += 1
    return [counter / len(fixStripped)]


    # STUDENTS: Complete this implementation so that it satisfies its
    # specification, with the following constraints.
    # You MUST make effective use a for-loop, and you will might need to use a
    # nested for-loop.
    #
    # Hint: If you are counting how many vocab_list words occur in a given
    # document, don't forget to reset that count every time you start with a
    # new document.
    #
    # Hint: we found the string method split() to be quite useful.  For a
    # (kind of unconventional) example of using split to get a convenient list
    # of words, see the file
    # http://www.cs.cornell.edu/courses/cs1110/2018sp/lectures/lecture12/modules/madlibs2.py



if __name__ == '__main__':
    # econ_vocab= get_econ_vocab()
    # print(econ_vocab)

    # https://www.exaptive.com/blog/topic-modeling-the-state-of-the-union
    red_topic = ['make sure', 'company', 'college', 'republican', 'parent',
                 'medicare', 'bipartisan', 'kid', 'small business', 'global']
    purple_topic = ['afghanistan', 'america', 'terror',  'troop', 'border',
                    'terrorist', 'violence', 'enemy', 'fighting', 'rule']

    sotus = []  # State of the Union addresses, 2005-2016
    for year in range(2001, 2009):
        fname = os.path.join('sources', str(year)+'_bush.txt')
        sotus.append(convert_lines_to_string(get_content_lines(fname)))
    for year in range(2009, 2017):
        fname = os.path.join('sources', str(year)+'_obama.txt')
        sotus.append(convert_lines_to_string(get_content_lines(fname)))
    for year in range(2017, 2019):
        fname = os.path.join('sources', str(year)+'_trump.txt')
        sotus.append(convert_lines_to_string(get_content_lines(fname)))

    print("Demonstration of tracing a topic through a single speech: ")
    print("How the red topic trends through Obama's 2013 SOTU. Topics typically exhibit such `bursty' behavior.")
    fname = os.path.join('sources', '2013_obama.txt')
    obama13 = convert_lines_to_paragraphs(get_content_lines(fname))
    print(track_topic(obama13, red_topic))



    red_trend = track_topic(sotus, red_topic)
    purple_trend = track_topic(sotus, purple_topic)

    import matplotlib.pyplot as plt
    plt.title("Topic trends in recent US State of the Union addresses")
    plt.ylabel("fraction of speech tokens on the topic")
    x = list(range(2001, 2019))
    plt.plot(x, track_topic(sotus, ECON_VOCAB),
             'b', marker='o', label="The Economist's economic terms")
    plt.plot(x, track_topic(sotus, red_topic),
             'r', marker='o',
             label="Evans' red topic (selections: 'college', 'parent', ...)")
    plt.plot(x, track_topic(sotus, purple_topic),
             'purple', marker='o',
             label="Evans' purple topic (selections: 'terrorist', 'enemy', ...)")
    labels = ["2001: Bush", "2005: Bush",
              "2009: Obama", "2013: Obama",
              "2017: Trump"]
    plt.xticks(range(2001, 2019, 4), labels, rotation=45, fontsize=6)
    plt.legend()
    plt.show()
    plt.close('all')
