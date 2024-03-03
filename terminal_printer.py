"""
Author: Luke Morris

This class provides functionality for use with a terminal window. This class is 
designed so that an object can be created however most of the functionality within
the class can be used without creating an object.

The functionality includes:

    - printing formatted text to the terminal (print_formatted()). Various 
        formatting commands in square brackets, [], can be used in the text to 
        achieve different formatting features. See the print_formatted() method
        for a full list. Parameters for this method include:
        - the text to be printed 
        - the maximum width for each line of the text
        - whether the cursor should move to a new line after printing
        - how much all of the text should be indented
        - how much text on subsequent lines after the first line should be 
        indented
    - printing headings (print_heading()) which is a specific version of printing 
        formatted text where the text for the heading is provide and a bordering 
        character can be chosen. A line of the bordering character will be printed 
        above and below the heading text a number of times equal to the length 
        of the heading text 
    - combining a list of string into a text string with commas and an appropriate
        joining word such as 'and' or 'or'
    - convert_message() will convert a string with formatting commands into a
        string that is printable using the print() method and the formatting will
        be applied.
    - clears the terminal screen (clear_screen()).
    - applying a pause for a designated time period (pause_before_proceeding())
    - get_input() method allow you to prompt the user for input through the 
        terminal. The functionality includes choosing the preferred input type 
        such as integer or string. Upper and lower limits can be set for integers
        and strings. There is a setting for allowing enter to be received with no
        other input provided. A list can also be provided with strings that the 
        user can input. For instance you may want a user to choose an entry from
        a numbered list however you may want the user to enter "details" to view
        details of the options. In this case "details" can be added in the 
        selection list and only a integer from the list items or "details" will 
        be accepted. If an incorrect input is received then the method will 
        prompt the user to reenter the input until a valid input is received.

Last modified: 22 January 2024
"""

import os
import time
import threading
import terminal_printer_loading_thread

class TerminalPrinter:

    """
    public variables
    tables with codes for text colors
    """

    basic_color_codes = {
        'gray': '90',
        'red': '91',
        'green': '92',
        'yellow': '93',
        'blue': '94',
        'purple': '95',
        'teal': '96',
        'white': '97'
    }
    
    
    color_codes = {
        'aliceblue': '240;248;255',
        'antiquewhite': '250;235;215',
        'aqua': '0;255;255',
        'aquamarine': '127;255;212',
        'azure': '240;255;255',
        'beige': '245;245;220',
        'bisque': '255;228;196',
        'black': '0;0;0',
        'blanchedalmond': '255;235;205',
        'blue': '0;0;255',
        'blueviolet': '138;43;226',
        'brown': '165;42;42',
        'burlywood': '222;184;135',
        'cadetblue': '95;158;160',
        'chartreuse': '127;255;0',
        'chocolate': '210;105;30',
        'coral': '255;127;80',
        'cornflowerblue': '100;149;237',
        'cornsilk': '255;248;220',
        'crimson': '220;20;60',
        'cyan': '0;255;255',
        'darkblue': '0;0;139',
        'darkcyan': '0;139;139',
        'darkgoldenrod': '184;134;11',
        'darkgray': '169;169;169',
        'darkgreen': '0;100;0',
        'darkgrey': '169;169;169',
        'darkkhaki': '189;183;107',
        'darkmagenta': '139;0;139',
        'darkolivegreen': '85;107;47',
        'darkorange': '255;140;0',
        'darkorchid': '153;50;204',
        'darkred': '139;0;0',
        'darksalmon': '233;150;122',
        'darkseagreen': '143;188;143',
        'darkslateblue': '72;61;139',
        'darkslategray': '47;79;79',
        'darkslategrey': '47;79;79',
        'darkturquoise': '0;206;209',
        'darkviolet': '148;0;211',
        'deeppink': '255;20;147',
        'deepskyblue': '0;191;255',
        'dimgray': '105;105;105',
        'dimgrey': '105;105;105',
        'dodgerblue': '30;144;255',
        'firebrick': '178;34;34',
        'floralwhite': '255;250;240',
        'forestgreen': '34;139;34',
        'fuchsia': '255;0;255',
        'gainsboro': '220;220;220',
        'ghostwhite': '248;248;255',
        'gold': '255;215;0',
        'goldenrod': '218;165;32',
        'gray': '128;128;128',
        'green': '0;128;0',
        'greenyellow': '173;255;47',
        'grey': '128;128;128',
        'honeydew': '240;255;240',
        'hotpink': '255;105;180',
        'indianred': '205;92;92',
        'indigo': '75;0;130',
        'ivory': '255;255;240',
        'khaki': '240;230;140',
        'lavender': '230;230;250',
        'lavenderblush': '255;240;245',
        'lawngreen': '124;252;0',
        'lemonchiffon': '255;250;205',
        'lightblue': '173;216;230',
        'lightcoral': '240;128;128',
        'lightcyan': '224;255;255',
        'lightgoldenrodyellow': '250;250;210',
        'lightgray': '211;211;211',
        'lightgreen': '144;238;144',
        'lightgrey': '211;211;211',
        'lightpink': '255;182;193',
        'lightsalmon': '255;160;122',
        'lightseagreen': '32;178;170',
        'lightskyblue': '135;206;250',
        'lightslategray': '119;136;153',
        'lightslategrey': '119;136;153',
        'lightsteelblue': '176;196;222',
        'lightyellow': '255;255;224',
        'lime': '0;255;0',
        'limegreen': '50;205;50',
        'linen': '250;240;230',
        'magenta': '255;0;255',
        'maroon': '128;0;0',
        'mediumaquamarine': '102;205;170',
        'mediumblue': '0;0;205',
        'mediumorchid': '186;85;211',
        'mediumpurple': '147;112;219',
        'mediumseagreen': '60;179;113',
        'mediumslateblue': '123;104;238',
        'mediumspringgreen': '0;250;154',
        'mediumturquoise': '72;209;204',
        'mediumvioletred': '199;21;133',
        'midnightblue': '25;25;112',
        'mintcream': '245;255;250',
        'mistyrose': '255;228;225',
        'moccasin': '255;228;181',
        'navajowhite': '255;222;173',
        'navy': '0;0;128',
        'oldlace': '253;245;230',
        'olive': '128;128;0',
        'olivedrab': '107;142;35',
        'orange': '255;165;0',
        'orangered': '255;69;0',
        'orchid': '218;112;214',
        'palegoldenrod': '238;232;170',
        'palegreen': '152;253;152',
        'paleturquoise': '175;238;238',
        'palevioletred': '219;112;147',
        'papayawhip': '255;239;213',
        'peachpuff': '255;218;185',
        'peru': '205;133;63',
        'pink': '255;192;205',
        'plum': '221;160;221',
        'powderblue': '176;224;230',
        'purple': '128;0;128',
        'red': '255;0;0',
        'rosybrown': '188;143;143',
        'royalblue': '65;105;225',
        'saddlebrown': '139;69;19',
        'salmon': '250;128;114',
        'sandybrown': '244;164;96',
        'seagreen': '46;139;87',
        'seashell': '255;245;238',
        'sienna': '160;82;45',
        'silver': '192;192;192',
        'skyblue': '135;206;235',
        'slateblue': '106;90;205',
        'slategray': '112;128;144',
        'slategrey': '112;128;144',
        'snow': '255;250;250',
        'springgreen': '0;255;127',
        'steelblue': '70;130;180',
        'tan': '210;180;140',
        'teal': '0;128;128',
        'thistle': '216;191;216',
        'tomato': '255;99;71',
        'turquoise': '64;224;208',
        'saddlebrown': '139;69;19',
        'violet': '238;130;238',
        'wheat': '245;222;179',
        'white': '255;255;255',
        'whitesmoke': '245;245;245',
        'yellow': '255;255;0',
        'yellowgreen': '154;205;50'
    }

    def __init__(self) -> None:

        # variables for use as a buffer
        self.__buffer = []
        self.__bold = False
        self.__italics = False
        self.__strikethrough = False
        self.__underline = False
        self.__color = 'none'
        self.__starting_bracket_index_value = -1 # -1 signifies no open bracket

        # variables for printing loading message with dots at time intervals
        self.__loading_thread = None # thread to display message while loading 
        self.loading_thread_stop_event = threading.Event() # event to stop the
        # loading thread 
        self.__loading_thread_max_active_time = 5
    
    def __buffer_add_char(self, new_char) -> bool:

        """
        adds new_char to __buffer.\n
        Checks if new_char is the last character in a formatting instruction 
        (for example [b]) and, if so, then method will pop the other formatting 
        instruction characters from __buffer and append characters to __buffer 
        that will implement the formatting instruction
        """

        # check that new_char is only 1 character long
        if len(new_char) != 1:
            return False
        
        # set buffer length and index value for starting bracket
        BUFFER_LENGTH = len(self.__buffer)
        INDEX_VALUE = self.__starting_bracket_index_value
        
        # process new_char
        if self.__starting_bracket_index_value != -1 and new_char == ']':
                
            # a potential opening bracket has been found and new_char could 
            # be a closing bracket of a formatting instruction
    
            # set string for converted formatting instruction that can be appended
            # initial value is an empty string
            formatting_instruction = ''

            # set string for type to be recorded in buffer for 
            # formatting_instruction characters in this group
            formatting_instruction_type = 'formatting_char'

            # determine type of formatting instruction, if applicable
            if (INDEX_VALUE + 2 == BUFFER_LENGTH
                and self.__buffer[INDEX_VALUE + 1]['char']
                in ['b', 'i', 'n', 's', 'u']):

                # formatting instruction was 3 characters long and is
                # [b], [i], [n], [s] or [u]

                # set formatting_instruction
                if self.__buffer[INDEX_VALUE + 1]['char'] == 'n':
                    formatting_instruction = '\n'
                else:
                    formatting_instruction = self.__buffer_toggle_formatting(
                        self.__buffer[INDEX_VALUE + 1]['char'],
                        self.__bold, self.__italics, self.__strikethrough,
                        self.__underline, self.__color) 

            elif (INDEX_VALUE + 4 == BUFFER_LENGTH
                and self.__buffer[INDEX_VALUE + 1]['char'] in ['i', 't']
                and self.__buffer[INDEX_VALUE + 2]['char'].isdigit()
                and self.__buffer[INDEX_VALUE + 3]['char'].isdigit()):

                # formatting instruction is 5 characters long and is in the
                # format [ixx] or [txx] (where 'xx' is a number between 0 
                # and 99)

                # set formatting_instruction to initial text values in buffer
                # plus ']' at the end
                formatting_instruction = ('[' 
                    + self.__buffer[INDEX_VALUE + 1]['char']
                    + self.__buffer[INDEX_VALUE + 2]['char']
                    + self.__buffer[INDEX_VALUE + 3]['char'] 
                    + ']')
                
                # set formatting_instruction_type to 'special_formatting_char' 
                # to signify that the characters in formatting_instruction
                # require additional consideration by the UI rather than just
                # being able to print them like the other formatting_char
                # characters
                formatting_instruction_type = 'special_formatting_char'

            elif (INDEX_VALUE + 7 == BUFFER_LENGTH
                and self.__buffer[INDEX_VALUE + 1]['char'] == 'c'
                and self.__buffer[INDEX_VALUE + 2]['char'] == '-'
                and self.__buffer[INDEX_VALUE + 3]['char'] == 'n'
                and self.__buffer[INDEX_VALUE + 4]['char'] == 'o'
                and self.__buffer[INDEX_VALUE + 5]['char'] == 'n'
                and self.__buffer[INDEX_VALUE + 6]['char'] == 'e'):

                # update __color value to 'none'
                self.__color = 'none'

                # append text to clear all styles to formatting_instruction
                formatting_instruction += self.get_formatting_clear_formatting()

                # append text to set all existing styles to formatting_instruction
                formatting_instruction += self.get_formatting_start_formatting(
                    self.__bold, self.__italics, self.__strikethrough,
                    self.__underline, self.__color) 

            elif (INDEX_VALUE + 5 < BUFFER_LENGTH
                and self.__buffer[INDEX_VALUE + 1]['char'] == 'c'
                and self.__buffer[INDEX_VALUE + 2]['char'] == '-'):

                # formatting instruction is at least 7 characters long and 
                # starts with '[c-'

                # set string for new color
                new_color = ''

                # populate new_color
                for i in range(INDEX_VALUE + 3, BUFFER_LENGTH):
                    new_color += self.__buffer[i]['char']
                
                # check current_color is a valid code
                color_code_text = self.get_formatting_color_code_text(new_color)

                # if color_code was valid then append formatting code otherwise
                # do not change return_text
                if color_code_text:
                    
                    formatting_instruction += color_code_text

                    # update __color value to 'none'
                    self.__color = new_color

            # update __buffer if formatting_instruction was created
            if formatting_instruction:

                # pop all elements from __starting_bracket_index_value,
                # i.e. '[' onwards, from __buffer as they will be replaced
                # with characters to implement the formatting instruction
                while (len(self.__buffer)
                    > INDEX_VALUE):

                    # pop last element from __buffer
                    self.__buffer.pop()

                # __buffer is ready for formatting instruction characters

                # append new formatting_instruction to buffer
                for i in range(len(formatting_instruction)):
                    self.__buffer.append({'char': formatting_instruction[i],
                    'type': formatting_instruction_type})

            else:

                # ']' is a normal character so can be appended to __buffer
                self.__buffer.append({'char': ']', 'type': 'standard_char'})

            # update __starting_bracket_index_value to -1 as a closing 
            # bracket, ']', was encountered
            self.__starting_bracket_index_value = -1    

        else:

            # if new_char is a '[' then update __starting_bracket_index_value
            # as the length of __buffer before adding the character (i.e. its
            # index position)
            if new_char == '[':
                self.__starting_bracket_index_value = len(self.__buffer)

            # append new_char details to __buffer
            if new_char.isspace():

                # new_char is a space

                # append ' ' to __buffer
                self.__buffer.append({'char': ' ', 'type': 'space_char'})
            
            else:

                # new_char is a standard character

                # append new_char to __buffer
                self.__buffer.append({'char': new_char, 'type': 'standard_char'})

        # new_char processed
        return True
    
    def buffer_clear(self) -> bool:

        """
        Clears all dictionaries (e.g. {'char': 'T', 'type': 'standard_char'}) 
        from the buffer and returns True when done
        """

        self.__buffer.clear()

        return True

    def __buffer_is_empty(self) -> bool:

        """
        Returns True if self.__buffer is empty otherwise returns True
        """

        if self.__buffer:
            return False
        else:
            return True
        
    def __buffer_load_message(self, message_to_convert) -> bool:

        """
        Receives a string which may have formatting instructions embedded within
        it. This method converts the string to a format that will implement all
        of the formatting instructions except tab and indent instructions which
        will contain the original characters. The converted string will be loaded
        into the buffer and can be retrieved using return_test_from_buffer().
        """

        # append each character into __buffer
        for char in message_to_convert:
            self.__buffer_add_char(char)

        # check if there is any formatting in message stored in buffer and, 
        # if so, then add characters to clear the formatting.
        if (self.__bold or self.__italics or self.__strikethrough 
            or self.__underline or self.__color):

            # get text to clear formatting
            clear_formatting_text = self.get_formatting_clear_formatting()

            # append clear_formatting_text to __buffer
            for char in clear_formatting_text:

                self.__buffer.append({'char': char, 'type': 'formatting_char'})

    def __buffer_return_text_portion(self, MAX_NUM_CHARACTERS=1000):

        """
        return tuples consisting of a string up to MAX_NUM_CHARACTERS in length 
        and the number of characters of text (excluding formatting characters)
        and the type of characters returned being 'standard_char', 'space_char',
        'formatting_char' or 'special_formatting_char'. 
        The default value for MAX_NUM_CHARACTERS is set to 1000 which is 
        essentially unlimited as it is much longer than any word.
        """

        # check that there are entries in the buffer
        if not self.__buffer:

            # there are no entries in __buffer

            return '', 0, ''

        # set variable for type of characters to be returned in this block
        block_type = self.__buffer[0]['type']
        
        # set list of types that will cause the method to stop appending
        # characters from the buffer if encountered
        stopping_type_list = ['formatting_char', 'space_char', 
            'special_formatting_char', 'standard_char']
        
        # remove type of first character in buffer
        stopping_type_list.remove(block_type)
        
        # set variable to count the number of non formatting_char characters
        # being returned
        num_non_formatting_chars = 0

        

        
        """
        # check first entry in buffer that is not of type 'formatting_char' and 
        # update stopping_type_list to reflect current type of character
        for i in range(len(self.__buffer)):
            
            # check that this 
            if self.__buffer[i]['type'] in stopping_type_list:
                
                # remove this type from stopping_type_list so that other 
                # characters with this type can be returned by this method
                stopping_type_list.remove(self.__buffer[i]['type'])

                # update block_type
                block_type = self.__buffer[i]['type']

                # break for i loop
                break 
        """           

        # set string to be returned
        return_string = '' 

        # append characters into return_string until character in 
        # stopping_type_list is reached, MAX_NUM_CHARACTERS is reached or 
        # there are no more characters in the buffer
        while (self.__buffer 
            and self.__buffer[0]['type'] not in stopping_type_list
            and num_non_formatting_chars < MAX_NUM_CHARACTERS):
            
            # pop first entry from buffer
            buffer_entry = self.__buffer.pop(0)

            # append popped character to return_string
            return_string += buffer_entry['char']

            # increment num_non_formatting_chars if not 'formatting_char' as type
            if (buffer_entry['type'] 
                not in ['formatting_char', 'special_formatting_char']):
                
                num_non_formatting_chars += 1

        # return characters in return_string and number of non-formatting 
        # characters
        return return_string, num_non_formatting_chars, block_type 

    def __buffer_toggle_formatting(self, formatting_type, current_bold, current_italics,
        current_strikethrough, current_underline, current_color) -> str:

        """
        Receives a formatting type ('b', 'i', 's' or 'u') and, based on the 
        currently toggled formatting styles, returns a string with the code 
        required to set those formatting styles for printing
        """   

        # set text to be returned for inclusion in printable message
        return_text = ''   

        # check if toggling on or off
        if ((formatting_type == 'b' and not current_bold)
            or (formatting_type == 'i' and not current_italics)
            or (formatting_type == 's' and not current_strikethrough)
            or (formatting_type == 'u' and not current_underline)):

            # toggling on

            if formatting_type == 'b':

                # update current_bold to True
                self.__bold = True
                
                # append text to turn on bold formatting style
                return_text += '\033[1m'

            elif formatting_type == 'i':

                # update current_italics to True
                self.__italics = True

                # append text to turn on italics formatting style
                return_text += '\033[3m'
            
            elif formatting_type == 's':

                # update current_strikethrough to True
                self.__strikethrough = True

                # append text to turn on italics formatting style
                return_text += '\033[9m'
            
            else:

                # update current_underline to True
                self.__underline = True

                # append text to turn on underline formatting style
                return_text += '\033[4m'

        else:

            # toggling off  

            # set chosen formatting style to False
            if formatting_type == 'b':

                self.__bold = False
                current_bold = False

            elif formatting_type == 'i':

                self.__italics = False
                current_italics = False

            elif formatting_type == 's':

                self.__strikethrough = False
                current_strikethrough = False
            
            else:

                self.__underline = False
                current_underline = False

            # append text to clear all styles
            return_text += self.get_formatting_clear_formatting()

            # append other formatting text
            return_text += self.get_formatting_start_formatting(current_bold,
                current_italics, current_strikethrough, current_underline, 
                current_color)

        return return_text

    def loading_thread_active(self) -> bool:

        """
        Checks whether there is currently a loading thread active and, if so,
        returns True otherwise returns False
        """

        if not self.__loading_thread or not self.__loading_thread.is_alive():
            return False
        else:
            return True

    def loading_thread_finish(self):

        """
        Terminates an existing thread that was printing a loading message
        """

        # Notify the thread to terminate
        self.loading_thread_stop_event.set()

        # Wait for the thread to finish
        self.__loading_thread.join()
    
    def loading_thread_start(self, starting_text: str = "Loading", 
        time_between_dots: float = 0.5, time_before_start: float = 0.25):

        """
        Creates a thread that prints starting_text and then prints a "." at
        time_between time intervals until the thread is terminated.

        parameters: 
        starting_text is the text to be printed at the beginning of the text,
        such as "Loading" 
        time_between is the time in seconds between "." being printed.
        """

        # check if there is currently a loading thread running
        if self.__loading_thread:

            # finish existing loading_thread
            self.loading_thread_stop_event.set()

            # wait until loading_thread has terminated
            self.__loading_thread.join()

            # reset loading_thread_stop_event
            self.loading_thread_stop_event.clear()
        
        # reset loading_thread_stop_event, if required
        if self.loading_thread_stop_event.is_set():
            self.loading_thread_stop_event.clear()
        
        # create new loading thread and start the tread
        self.__loading_thread = terminal_printer_loading_thread.LoadingThread(
            self.loading_thread_stop_event, starting_text=starting_text,
            time_before_start=time_before_start,
            time_between_dots=time_between_dots,
            max_time_alive=self.__loading_thread_max_active_time)
        self.__loading_thread.start()

    @classmethod
    def get_basic_color_codes(cls) -> dict:

        """
        Returns dictionary containing basic_color_codes (name and number)
        """

        return TerminalPrinter.basic_color_codes
    
    @classmethod
    def get_color_codes(cls) -> dict:

        """
        Returns dictionary containing color_codes (name and RGB code)
        """

        return TerminalPrinter.color_codes

    @staticmethod
    def clear_screen() -> bool:

        """
        Clears the terminal screen
        """

        os.system('cls')

        return True
    
    @staticmethod
    def combine_list_into_text(list_to_combine, joiner_word='and'):

        """
        combines the elements of a list into "element1, element2, and element 3"

        joiner_word is either 'and' or 'or'

        This function uses an Oxford comma
        """

        # check the number of entries
        if not list_to_combine:

            return ""

        elif len(list_to_combine) == 1:

            return str(list_to_combine[0])

        elif len(list_to_combine) == 2:

            # prepare string
            return_text = (str(list_to_combine[0]) + " " + joiner_word + " " 
                + str(list_to_combine[1]))

            return return_text

        else:

            # set text_list to store portions of text
            text_list = []

            # populate text_list
            for i in range(len(list_to_combine)):

                # check that this is not the first or last entries
                if i:

                    # this is not the first so append ", "
                    text_list.append(", ")

                if i == len(list_to_combine) - 1:

                    # this is the last entry so append ", and "
                    text_list.append(joiner_word + " ")

                # append the names from list_to_combine
                text_list.append(str(list_to_combine[i]))

            # combine text_list into a string
            final_text = ''.join(text_list)

            # return combined text
            return final_text

    @staticmethod
    def convert_message(message_to_convert, PARAGRAPH_WIDTH=80, 
        TEXT_INDENT=0, FOLLOWING_LINE_INDENT=0) -> list:

        """
        Converts a string into a printable message by converting embedded
        formatting instructions

        Returns list of strings that can be printed by Python with the embedded 
        formatting.

        PARAGRAPH_WIDTH is the maximum number of characters that will be printed
        on a row of text.\n
        NEW_LINE is whether the curser should go to a new line after the end
        of all of the text is printed.\n
        TEXT_INDENT is the number of blank spaces that should appear before every
        line of text. This amount will count towards the paragraph width, e.g.
        if TEXT_INDENT is 10 and PARAGRAPH_WIDTH is 80 then the first 10 
        characters of every line will be 10 blank spaces followed by up to 70
        characters.\n
        FOLLOWING_LINE_INDENT is the number of blank spaces (in additional to 
        any blank spaces for TEXT_INDENT) that should appear before every line
        of text after the first line of text. This amount will count towards the 
        paragraph width.\n
        There are additional formatting instructions that can appear in the 
        message being converted and they will be between square brackets([]).
        These are\n:
        [txx] - tab of size xx. Use two digits. 05 is 5.\n
        [n] - new line.\n
        [ixx] - is an additional indent value for the next new line. Note that
        [i00] will reset the indent value to the text_indent and 
        following_line_indent values.\n
        [b] - toggles bold text.\n
        [i] - toggles italics text.\n
        [u] - toggles underline text.\n
        [s] - toggles strikethrough text.\n
        There are various colors for text. They will be in square brackets with 
        'c-' followed by the name of the color, the rgb color with 3 numbers 
        between 0 and 255 each separated by ; or 'none' to clear the color.\n 
        The color names include: gray, red, green, yellow, blue, purple, teal 
        and white    
        """

        # check that message has characters otherwise return and empty string
        if message_to_convert.isspace():

            return []

        # set variables
        return_text_list = [] # list of strings to return with converted message
        current_indent = max(TEXT_INDENT, 0) # set current indent value.
        #ensures that current_indent is positive
        current_line = ' ' * current_indent # string to store current line of 
        # converted text
        num_chars_current_line = current_indent # number of printable characters 
        # on current line    
        
        # update current_indent to include FOLLOWING_LINE_INDENT
        current_indent += FOLLOWING_LINE_INDENT   
                
        # create text buffer object
        text_buffer = TerminalPrinter()

        """
        load message_to_convert into __buffer
        """
        
        # load message_to_convert into text_buffer
        text_buffer.__buffer_load_message(message_to_convert)

        """
        retrieve characters from __buffer
        """

        # set variable for whether a new line command was received
        new_line_received = False

        # retrieve blocks of text from text_buffer until text_buffer is empty
        while True:

            # get block of converted text from text_buffer
            new_text, num_chars_new_text, new_text_type = (
                text_buffer.__buffer_return_text_portion())

            # process depending on new_text_type
            if new_text_type == 'standard_char':

                # check if new_text will fit on current_line
                if (num_chars_new_text + num_chars_current_line 
                    <= PARAGRAPH_WIDTH):

                    # append new_text to current_lien
                    current_line += new_text

                    # update num_chars_current_line
                    num_chars_current_line += num_chars_new_text

                else:

                    # new_text is too long to fit on the current_line

                    # check if new_text is too large to fully fit on a single line
                    if num_chars_new_text + current_indent > PARAGRAPH_WIDTH:

                        # new_text will not fit on a line anyway so split over 
                        # multiple lines

                        # fill current_line with as much text from new_text as 
                        # possible
                        last_index_value = (PARAGRAPH_WIDTH 
                            - num_chars_current_line) 
                        current_line += new_text[:last_index_value]
                        num_chars_current_line = (num_chars_current_line 
                            + last_index_value)
                        
                        # remove characters appended to current_line from 
                        # new_text
                        new_text = new_text[last_index_value:]

                        # append current_line to return_text_list
                        return_text_list.append(current_line)

                        # reset current_line and num_chars_current_line
                        current_line = ''
                        num_chars_current_line = 0
                        
                        # fill additional lines of text with remaining new_text
                        while len(new_text):

                            if (len(new_text) 
                                > PARAGRAPH_WIDTH - current_indent):

                                # append new line with as much of the text as 
                                # will fit on a line to return_text_list
                                return_text_list.append(' ' * current_indent
                                    + new_text[:PARAGRAPH_WIDTH - current_indent])
                                
                                # remove appended characters from new_text
                                new_text = new_text[PARAGRAPH_WIDTH 
                                    - current_indent:]
                                
                            else:
                                
                                # new_text will fit on a new line

                                # remaining characters in new_text will fit on 
                                # one line

                                # append current_indent spaces and remaining
                                # new_text to current_line

                                # update current_line
                                current_line += (' ' * current_indent
                                    + new_text) 
                                
                                # update current_line
                                num_chars_current_line = (current_indent 
                                    + len(new_text))
                                
                                # clear new_text as all characters appended
                                new_text = ''
                    
                    else:

                        # new_text can fit on a new line
                        
                        # append current_line to return_text_list
                        return_text_list.append(current_line) 
                        
                        # update new current_line
                        current_line = (' ' * current_indent
                            + new_text) 
                        
                        # update current_line
                        num_chars_current_line = (current_indent 
                            + len(new_text))

            elif new_text_type == 'space_char':

                # spaces will not be added to the start of a line when there are 
                # no other characters on that line already
                
                if (not len(return_text_list)
                    or (len(current_line) and not current_line.isspace())):

                    # Either this is the start of the text and spaces are required 
                    # or there are characters in the current_line and the spaces 
                    # will follow.

                    # check if there is sufficient space for all spaces
                    if (num_chars_current_line + num_chars_new_text 
                        > PARAGRAPH_WIDTH):

                        # too many spaces to fit on current_line

                        # add enough spaces to fill current_line and discard the
                        # additional spaces rather than putting them at the 
                        # start of the next line
                        current_line += (' ' * PARAGRAPH_WIDTH 
                            - num_chars_new_text)
                        
                        # update num_chars_current_line
                        num_chars_current_line = PARAGRAPH_WIDTH
                         
                    else:

                        # all spaces can be added to current_line 
                        
                        # add spaces to current_line
                        current_line += new_text

                        # update num_chars_current_line
                        num_chars_current_line += num_chars_new_text

                # if there were no characters in the current_line then the 
                # spaces are discarded rather than going at the start of the
                # line
            
            elif new_text_type == 'formatting_char':

                # update new_line_received, if applicable
                if new_text == '\n':
                    
                    # do not append '\n' but instead finish the current line
                    # by setting new_line_received to True
                    new_line_received = True

                else:
                
                    # append new_text to current_line
                    current_line += new_text

                

            elif new_text_type == 'special_formatting_char':

                formatting_integer = int(new_text[2:4])
                
                # process indent or tab formatting instruction
                if new_text[1] == 'i':

                    if formatting_integer == 0:

                        # reset current_indent
                        current_indent = TEXT_INDENT + FOLLOWING_LINE_INDENT
                    
                    else:

                        # increase current_indent
                        if current_indent + formatting_integer >= PARAGRAPH_WIDTH:

                            # set current_indent to 1 character less than 
                            # PARAGRAPH_WIDTH to allow at least 1 character to
                            # be printed on each line
                            current_indent = PARAGRAPH_WIDTH - 1

                        else: 

                            # increase current_indent by formatting_integer
                            current_indent += formatting_integer
                
                if new_text[1] == 't':

                    # apply tab

                    if (num_chars_current_line + formatting_integer 
                        >= PARAGRAPH_WIDTH):

                        # tab fills the rest of the current_line
                        current_line += (' ' 
                            * (PARAGRAPH_WIDTH - num_chars_current_line))

                        # update num_chars_current_line
                        num_chars_current_line += (PARAGRAPH_WIDTH 
                            - num_chars_current_line)
                    
                    else:

                        # tab fits on current_line.
                        # tabs are allowed at the beginning of a line even if 
                        # there aren't any characters on the line
                        current_line += ' ' * formatting_integer

                        # update num_chars_current_line
                        num_chars_current_line += formatting_integer

            # update if current_line is full or new line command was received
            if num_chars_current_line == PARAGRAPH_WIDTH or new_line_received:                
                
                # append current_line to return_text_list
                return_text_list.append(current_line)

                # reset current_line and num_chars_current_line
                if text_buffer.__buffer_is_empty():

                    # the is no more text in the buffer so set current_line
                    # to an empty string
                    
                    # set current_line
                    current_line = ''
                    num_chars_current_line = 0 

                else:

                    # there is more text in the buffer

                    # set up next current_line
                    current_line = ' ' * current_indent
                    num_chars_current_line = current_indent

                # reset new_line_received
                if new_line_received:
                    new_line_received = False
            
            # check if __buffer is empty and go to next line if applicable
            if text_buffer.__buffer_is_empty():

                # text has been converted

                # get last current_line, if applicable
                if len(current_line):

                    # append current_line to return_text_list
                    return_text_list.append(current_line)
                
                # NOTE that NEW_LINE is not handled here. When the lines in 
                # return_text_list are printed then that function will handle
                # whether the cursor should move to another line after the text

                # all text has been converted so break while True loop
                break
                
        # return list of printable lines
        return return_text_list

    @staticmethod
    def get_formatting_clear_formatting() -> str:

        """
        Returns string that will clear all existing formatting when passed to 
        print()
        """
        return '\x1b[0m'
    
    @staticmethod
    def get_formatting_start_formatting(bold, italics, strikethrough, underline, 
            color_text) -> str:

        """
        Returns string that implements the chosen formatting styles\n

        bold, italics, underline and strikethrough are to implement those 
        formatting styles and are boolean values.\n
        color_text is a string value and is either 'none' (if there is no text 
        color), a color name or an rgb value formatted as three integers 
        between 0 and 255 inclusive separated by ';'.\n 
        Returns a string that can be passed to the print function to implement
        the chosen formatting.
        """

        # set string to store all formatting text
        return_text = ''

        # prepare formatting text for bold, italics, underline and strikethrough
        if bold:
            return_text += '\033[1m'
        if italics:
            return_text += '\033[3m'
        if strikethrough:
            return_text += '\033[9m'
        if underline:
            return_text += '\033[4m'
        
        # prepare formatting text for text color
        # NOTE 'none' will return an empty string when passed to 
        # get_formatting_color_code_text so no need to check separately
        color_code_text = TerminalPrinter.get_formatting_color_code_text(color_text)
        if color_code_text:
            return_text += color_code_text

        # all formatting text has been added
        return return_text
    
    @staticmethod
    def get_formatting_color_code_text(color_text) -> str:

        """
        Receives a string for the color required. Checks that the string is 
        valid and returns the code for that color.

        returns color_code        
        """

        RGB_NUM_PARTS = 3

        # set color_code to store result
        color_code = ''

        # check if color_text is a word or a rgb code
        if color_text.isalpha():

            # color_text is a word
            
            if color_text in TerminalPrinter.basic_color_codes:
                color_code = TerminalPrinter.basic_color_codes[color_text] 
            elif color_text in TerminalPrinter.color_codes:
                color_code = '38;2;' + TerminalPrinter.color_codes[color_text]
        
        else:

            # color_text is not a word. 

            # check that color_text is in valid rgb format

            # set variable for current_color being a valid code
            current_color_valid = False

            # split current_color using ';' as the separator. Should
            # receive a list with 3 integers between 0 and 255
            color_code_list = color_text.split(';')

            # check color_code_list
            if len(color_code_list) == RGB_NUM_PARTS:

                # correct number of entries for rgb

                # check that the 3 sections of code are valid
                for i in range(RGB_NUM_PARTS):

                    # check if entry is not an integer between 0 and 255,
                    # i.e. it is not valid
                    if (color_code_list[i].isnumeric() == False
                        or int(color_code_list[i]) < 0
                        or int(color_code_list[i]) > 255):

                        # incorrect format for integer between 0 and 255
                        # break for loop (and current_color_valid remains
                        # false)
                        break

                    # correct format for this entry

                    # if this is the last entry then all entries were 
                    # correct and color_text is a valid string
                    if i == len(color_code_list) - 1:

                        # update current_color_valid to True
                        current_color_valid = True
            
            # append text color details if current_color_valid
            if current_color_valid:

                # set color_code
                color_code = '38;2;' + color_text

        # combine color_code with formatting text, if valid color_text
        if color_code:
            
            # set color_code_text to string for changing text color
            color_code_text = '\x1b[' + color_code + 'm'
        
        else:

            # color_text was invalid
            
            # set color_code_text to an empty string
            color_code_text = ''

        return color_code_text

    @staticmethod
    def get_input(input_message, INPUT_TYPE='string', LOWER_LIMIT=0.0,
            UPPER_LIMIT=0.0, IGNORE_ENTER=False, SELECTION_LIST=[],
            PARAGRAPH_WIDTH=80, TEXT_INDENT=0,
            FOLLOWING_LINE_INDENT=0):

        """
        Function prints input_message and receives an input from the User in the
        appropriate format.\n
        Function returns tuple (bool, string). The boolean value is whether an
        input was successfully received and the string is the input received. 
        The function will only return false where the PARAGRAPH_WIDTH is less
        than TEXT_INDENT and FOLLOWING_LINE_INDENT.\n 
        input_message is the message prompt to be displayed for the User.\n
        INPUT_TYPE is the desired format of the input and will be either 
        'string', 'integer', or 'float'. NOTE that the returned value will be a 
        string.\n
        LOWER_LIMIT and UPPER_LIMIT are floats. These are only relevent when the
        desired input is a float or an integer. The range is inclusive of the
        LOWER_LIMIT and UPPER_LIMIT.\n
        IGNORE_ENTER allows the User to press enter without entering an input
        and this will be a valid response. An empty string is returned.\n
        SELECTION_LIST is a list of strings that can be accepted as input. Only
        inputs that are in SELECTION_LIST (or an empty string if IGNORE_ENTER is
        true) will be accepted.\n
        PARAGRAPH_WIDTH is the width of the text to be displayed to receive the 
        input.\n
        TEXT_INDENT is the minimum number of spaces that all of the text should 
        be indented.\n
        FOLLOWING_LINE_INDENT is the number of additional spaces that the text 
        on all lines after the first line should be indented.\n
        All formatting commands for print_formatted function are accepted. 
        """
        width_ok = True
        error_msg_portions_list = []

        # check that after required indents are applied that there are spaces
        # left for text to be printed on a line
        if PARAGRAPH_WIDTH <= TEXT_INDENT:

            # ERROR - TEXT_INDENT does not leave space for text to be printed
            width_ok = False
            error_msg_portions_list.append('ERROR. TEXT_INDENT is greater than'
                + ' or equal to PARAGRAPH_WIDTH hence there is no space to print'
                + ' the text.')
            
        elif PARAGRAPH_WIDTH <= TEXT_INDENT + FOLLOWING_LINE_INDENT:

            # ERROR - TEXT_INDENT and FOLLOWING_LINE_INDENT leaves no space for
            # tet to be printed on a line
            width_ok = False
            error_msg_portions_list.append('ERROR. TEXT_INDENT plus'
                + ' FOLLOWING_LINE_INDENT is greater than or equal to'
                + ' PARAGRAPH_WIDTH hence there is no space to print the text.')
            
        # print message
        if width_ok:

            # get input
            while True:

                input_valid = True

                # print input message without going to a new line as this
                # will replace the message for input()
                TerminalPrinter.print_formatted(input_message, 
                    PARAGRAPH_WIDTH=PARAGRAPH_WIDTH, NEW_LINE=False,
                    TEXT_INDENT=TEXT_INDENT, 
                    FOLLOWING_LINE_INDENT=FOLLOWING_LINE_INDENT)
                
                # get input from User
                input_received = input('')

                if input_received:

                    # check input is valid
                    try:

                        if (SELECTION_LIST 
                            and input_received not in SELECTION_LIST):

                            # input_received must be in SELECTION_LIST but
                            # wasn't

                            if IGNORE_ENTER:
                                additional_text = ' or you can just press enter'
                            else:
                                additional_text = ''

                            raise ValueError('Text must be one of the'
                                + ' following: '
                                + TerminalPrinter.combine_list_into_text(
                                SELECTION_LIST, 'or') + additional_text + '.')
                        
                        elif INPUT_TYPE == 'float':

                            # check that input_received can be converted into a 
                            # float

                            # convert input_received to a float. If unsuccessful
                            # then error will be thrown
                            float(input_received)

                            # check that input_received is within the UPPER_LIMIT
                            # and LOWER_LIMIT
                            if (float(input_received) < min(LOWER_LIMIT, 
                                UPPER_LIMIT)
                                or float(input_received) > max(LOWER_LIMIT,
                                UPPER_LIMIT)):

                                # input_received outside range
                                
                                if IGNORE_ENTER:
                                    additional_text = ' or you can just press enter'
                                else:
                                    additional_text = ''

                                raise ValueError(input_received
                                    + ' was given but value must be between '
                                    + str(float(min(LOWER_LIMIT, UPPER_LIMIT)))
                                    + ' and '
                                    + str(float(max(LOWER_LIMIT, UPPER_LIMIT)))
                                    + additional_text
                                    + '.')

                        elif INPUT_TYPE == 'integer':

                            # check that input_received can be converted into an 
                            # integer

                            # convert input_received to an integer. If unsuccessful
                            # then error will be thrown
                            int(input_received)

                            # check that input_received can be converted into an
                            # integer
                            if (int(input_received) < min(int(LOWER_LIMIT),
                                int(UPPER_LIMIT))
                                or int(input_received) > max(int(LOWER_LIMIT),
                                int(UPPER_LIMIT))):

                                # input_received outside range
                                
                                if IGNORE_ENTER:
                                    additional_text = ' or you can just press enter'
                                else:
                                    additional_text = ''

                                raise ValueError(input_received
                                    + ' was given but value must be between '
                                    + str(int(min(LOWER_LIMIT, UPPER_LIMIT)))
                                    + ' and '
                                    + str(int(max(LOWER_LIMIT, UPPER_LIMIT)))
                                    + additional_text
                                    + '.')

                    except ValueError as ve:

                        # print messages for error
                        TerminalPrinter.print_formatted('ERROR. Incorrect input'
                            + ' type was received. ' + str(ve.args[0]))
                        input("Try again.\nPress any key to continue.")
                        TerminalPrinter.clear_screen()

                        # set input_valid to False as incorrect input
                        input_valid = False

                    except Exception as e:

                        TerminalPrinter.print_formatted('ERROR. An exception of'
                            + ' type ' 
                            + str(type(e).__name__) 
                            + 'occurred. Arguments: '
                            + str(e.args))
                        input("Try again.\nPress any key to continue.")
                        TerminalPrinter.clear_screen()


                elif not input_received and not IGNORE_ENTER:

                    # input wasn't received but it was required

                    # print error message for User
                    TerminalPrinter.print_formatted('Input is required but'
                        + ' no input was received.')
                    input('Try again.\nPress any key to continue.')
                    TerminalPrinter.clear_screen()

                    # set input_valid to False as no input was received
                    input_valid = False

                if input_valid:
                    
                    break # break while True loop

            # return True as successful and input_received as a string
            return True, input_received

        else:

            # width was not ok
            
            error_msg_text = '\n'.join(error_msg_portions_list)

            TerminalPrinter.print_formatted(error_msg_text)

            # an error occured. text_to_print was not printed
            return False, ''

    @staticmethod
    def pause_before_proceeding(seconds_to_pause = 1.5) -> bool:

        """
        Pauses for a number of seconds equal to seconds_to_pause
        """

        time.sleep(seconds_to_pause)

        return True

    @staticmethod
    def print_formatted(text_to_print, PARAGRAPH_WIDTH=80, NEW_LINE=True,
        TEXT_INDENT=0, FOLLOWING_LINE_INDENT=0) -> bool:

        """
        Function receives text (text_to_print) and then prints the text in the 
        desired format.

        Commands within square brackets in the text (e.g. [b]) allow different
        formatting features.

        Note where a command requires 2 digits (i.e. xx) but the desired value 
        is less that 10 then put a zero at the front. For example a tab of 5 
        spaces would be [t05].

        List of commands:
            [n] - go to new line\n
            [b] - toggle bold\n
            [i] - toggle italics\n
            [u] - toggle underline\n
            [s] - toggle strikethrough\n
            [ixx] - apply additional indent of xx for next line onwards\n
            [i00] - reset additional indents. TEXT_INDENT and 
                FOLLOWING_LINE_INDENT still apply.\n
            [txx] - applies a tab of xx spaces.\n
            [c-none] - removes text color.\n
            [c-red] - applies named text color\n
            [c-0;255;255] - applies rgb text color\n

        Tabs

            Tabs are not split over lines. The remaining spaces will not be 
            applied to the new line. 
        """

        width_ok = True
        error_msg_portions_list = []

        # check that after required indents are applied that there are spaces
        # left for text to be printed on a line
        if PARAGRAPH_WIDTH <= TEXT_INDENT:

            # ERROR - TEXT_INDENT does not leave space for text to be printed
            width_ok = False
            error_msg_portions_list.append('ERROR. TEXT_INDENT is greater than'
                + ' or equal to PARAGRAPH_WIDTH hence there is no space to print'
                + ' the text.')
            
        elif PARAGRAPH_WIDTH <= TEXT_INDENT + FOLLOWING_LINE_INDENT:

            # ERROR - TEXT_INDENT and FOLLOWING_LINE_INDENT leaves no space for
            # tet to be printed on a line
            width_ok = False
            error_msg_portions_list.append('ERROR. TEXT_INDENT plus'
                + ' FOLLOWING_LINE_INDENT is greater than or equal to'
                + ' PARAGRAPH_WIDTH hence there is no space to print the text.')
            
        # print message
        if width_ok:

            printable_lines = TerminalPrinter.convert_message(text_to_print,
                PARAGRAPH_WIDTH=PARAGRAPH_WIDTH, TEXT_INDENT=TEXT_INDENT,
                FOLLOWING_LINE_INDENT=FOLLOWING_LINE_INDENT)
            
            for i in range(len(printable_lines)):

                if i == len(printable_lines) - 1 and not NEW_LINE:
                    print(printable_lines[i], end='')
                else:
                    print(printable_lines[i])
            
            # all ok
            return True

        else:

            error_msg_text = '\n'.join(error_msg_portions_list)

            TerminalPrinter.print_formatted(error_msg_text)

            # an error occured. text_to_print was not printed
            return False

    @staticmethod
    def print_heading(heading_text, border_character = '-', PARAGRAPH_WIDTH=80, 
        NEW_LINE=True, TEXT_INDENT=0, FOLLOWING_LINE_INDENT=0):

        """
        Prints heading with '-' above and below each letter in heading_text.
        
        See print_formatted for details of parameters.
        """

        TerminalPrinter.print_formatted(border_character * len(heading_text),
            PARAGRAPH_WIDTH=PARAGRAPH_WIDTH, NEW_LINE=NEW_LINE, 
            TEXT_INDENT=TEXT_INDENT, FOLLOWING_LINE_INDENT=FOLLOWING_LINE_INDENT)
        
        TerminalPrinter.print_formatted(heading_text,
            PARAGRAPH_WIDTH=PARAGRAPH_WIDTH, NEW_LINE=NEW_LINE, 
            TEXT_INDENT=TEXT_INDENT, FOLLOWING_LINE_INDENT=FOLLOWING_LINE_INDENT)

        TerminalPrinter.print_formatted(border_character * len(heading_text),
            PARAGRAPH_WIDTH=PARAGRAPH_WIDTH, NEW_LINE=NEW_LINE, 
            TEXT_INDENT=TEXT_INDENT, FOLLOWING_LINE_INDENT=FOLLOWING_LINE_INDENT)

    @staticmethod
    def testing():

        """
        This method tests all of the methods used by an instance of TerminalPrinter
        """

        UI_object = TerminalPrinter()

        all_tests_passed = True
        
        # print heading for testing getters and setters
        print("\n" + "=" * 80 + "\nTESTING USER INTERFACE\n" 
            + "=" * 80 + "")
        
        """
        TESTING __buffer_is_empty()
        """
        
        # test __buffer_is_empty() with no elements in buffer
        print("\nTesting __buffer_is_empty() for new UI.")
        if UI_object.__buffer_is_empty():
            
            print("{:<15}{}".format('CORRECT','__buffer_is_empty() returned'
                + ' True when empty'))
        
        else:
            
            print("{:<15}{}".format('INCORRECT','__buffer_is_empty() returned'
                + '  False when empty'))
            
            if all_tests_passed:
                all_tests_passed = False

        """ manually append entries in UI """
        character_list = ['T', 'e', 's', 't']
        for char in character_list:
            UI_object.__buffer.append({'char': char, 'type': 'standard_char'})

        # test __buffer_is_empty() with 4 elements in buffer
        print("\nTesting __buffer_is_empty() after 'Test' characters were"
            + " appended.")
        if UI_object.__buffer_is_empty() == False:
            
            print("{:<15}{}".format('CORRECT','__buffer_is_empty() returned'
                + ' False when __buffer has elements.'))
        
        else:
            
            print("{:<15}{}".format('INCORRECT','__buffer_is_empty() returned'
                + '  True when __buffer has elements'))
            
            if all_tests_passed:
                all_tests_passed = False

        # test buffer_clear() to clear buffer
        UI_object.buffer_clear()

        # test __buffer_is_empty() with no elements in buffer
        print("\nTesting buffer_clear() by calling __buffer_is_empty()"
            + " afterwards.")
        if UI_object.__buffer_is_empty():
            
            print("{:<15}{}".format('CORRECT','buffer is empty after'
                + ' buffer_clear()'))
        
        else:
            
            print("{:<15}{}".format('INCORRECT','buffer is not empty after'
                + '  buffer_clear()'))
            
            if all_tests_passed:
                all_tests_passed = False

        """
        TESTING __add_char()
        """

        # update character_list - 'New'
        character_list = ['N', 'e', 'w']

        for char in character_list:
            UI_object.__buffer_add_char(char)
        
        for entry in UI_object.__buffer:
            print("")
            for key, value in entry.items():
                print("{}: {}".format(key, value))
        print("\nEntered: 'New' into buffer")
        if (len(UI_object.__buffer) == len(character_list)  
            and (UI_object.__buffer[0]['char'] == character_list[0] 
                and UI_object.__buffer[0]['type'] == 'standard_char') 
            and (UI_object.__buffer[1]['char'] == character_list[1] 
                and UI_object.__buffer[1]['type'] == 'standard_char') 
            and (UI_object.__buffer[2]['char'] == character_list[2] 
                and UI_object.__buffer[2]['type'] == 'standard_char')):
            
            print("{:<15}{}".format('CORRECT','Characters in buffer are correct'))
            
        else:

            print("{:<15}{}".format('INCORRECT','Characters in buffer are not'
                + ' correct.'))
            
            if all_tests_passed:
                all_tests_passed = False
            
        # update character_list - 'a pig'
        character_list = ['A', ' ', 'p', 'i', 'g']

        # clear buffer
        UI_object.buffer_clear()

        # add characters to __buffer
        for char in character_list:
            UI_object.__buffer_add_char(char)
        
        for entry in UI_object.__buffer:
            print("")
            for key, value in entry.items():
                print("{}: {}".format(key, value))
        print("\nEntered: 'A pig' into buffer")
        if (len(UI_object.__buffer) == len(character_list) 
            and (UI_object.__buffer[0]['char'] == character_list[0] 
                and UI_object.__buffer[0]['type'] == 'standard_char') 
            and (UI_object.__buffer[1]['char'] == character_list[1] 
                and UI_object.__buffer[1]['type'] == 'space_char') 
            and (UI_object.__buffer[2]['char'] == character_list[2] 
                and UI_object.__buffer[2]['type'] == 'standard_char') 
            and (UI_object.__buffer[3]['char'] == character_list[3] 
                and UI_object.__buffer[3]['type'] == 'standard_char') 
            and (UI_object.__buffer[4]['char'] == character_list[4] 
                and UI_object.__buffer[4]['type'] == 'standard_char')):
            
            print("{:<15}{}".format('CORRECT','Characters in buffer are correct'))
            
        else:

            print("{:<15}{}".format('INCORRECT','Characters in buffer are not'
                + ' correct.'))
            
            if all_tests_passed:
                all_tests_passed = False
            
        """ test tab instruction """
        
        # update character_list - 'A[t03]B'
        character_list = ['A', '[', 't', '0', '3', ']', 'B']

        # clear buffer
        UI_object.buffer_clear()

        # add characters to __buffer
        for char in character_list:
            UI_object.__buffer_add_char(char)
        
        for entry in UI_object.__buffer:
            print("")
            for key, value in entry.items():
                print("{}: {}".format(key, value))
        print("\nEntered: 'A[t03]B' into buffer")
        if (len(UI_object.__buffer) == len(character_list)
            and (UI_object.__buffer[0]['char'] == character_list[0]
                and UI_object.__buffer[0]['type'] == 'standard_char') 
            and (UI_object.__buffer[1]['char'] == character_list[1] 
                and UI_object.__buffer[1]['type'] == 'special_formatting_char') 
            and (UI_object.__buffer[2]['char'] == character_list[2]
                and UI_object.__buffer[2]['type'] == 'special_formatting_char') 
            and (UI_object.__buffer[3]['char'] == character_list[3]
                and UI_object.__buffer[3]['type'] == 'special_formatting_char') 
            and (UI_object.__buffer[4]['char'] == character_list[4]
                and UI_object.__buffer[4]['type'] == 'special_formatting_char') 
            and (UI_object.__buffer[5]['char'] == character_list[5]
                and UI_object.__buffer[5]['type'] == 'special_formatting_char') 
            and (UI_object.__buffer[6]['char'] == character_list[6]
                and UI_object.__buffer[6]['type'] == 'standard_char')):
            
            print("{:<15}{}".format('CORRECT','Characters in buffer are correct'))
            
        else:

            print("{:<15}{}".format('INCORRECT','Characters in buffer are not'
                + ' correct.'))
            
            if all_tests_passed:
                all_tests_passed = False
            
        """ test indent instruction """
        
        # update character_list - 'A[t03]B'
        character_list = ['A', '[', 'i', '1', '0', ']', 'B']

        # clear buffer
        UI_object.buffer_clear()

        # add characters to __buffer
        for char in character_list:
            UI_object.__buffer_add_char(char)
        
        for entry in UI_object.__buffer:
            print("")
            for key, value in entry.items():
                print("{}: {}".format(key, value))
        print("\nEntered: 'A[i10]B' into buffer")
        if (len(UI_object.__buffer) == len(character_list)
            and (UI_object.__buffer[0]['char'] == character_list[0]
                and UI_object.__buffer[0]['type'] == 'standard_char') 
            and (UI_object.__buffer[1]['char'] == character_list[1] 
                and UI_object.__buffer[1]['type'] == 'special_formatting_char') 
            and (UI_object.__buffer[2]['char'] == character_list[2]
                and UI_object.__buffer[2]['type'] == 'special_formatting_char') 
            and (UI_object.__buffer[3]['char'] == character_list[3]
                and UI_object.__buffer[3]['type'] == 'special_formatting_char') 
            and (UI_object.__buffer[4]['char'] == character_list[4]
                and UI_object.__buffer[4]['type'] == 'special_formatting_char') 
            and (UI_object.__buffer[5]['char'] == character_list[5]
                and UI_object.__buffer[5]['type'] == 'special_formatting_char') 
            and (UI_object.__buffer[6]['char'] == character_list[6]
                and UI_object.__buffer[6]['type'] == 'standard_char')):
            
            print("{:<15}{}".format('CORRECT','Characters in buffer are correct'))
            
        else:

            print("{:<15}{}".format('INCORRECT','Characters in buffer are not'
                + ' correct.'))
            
            if all_tests_passed:
                all_tests_passed = False

        """ test color instructions """
        
        # test color by name

        # update character_list - 'A[c-red]B' 
        character_list = ['A', '[', 'c', '-', 'r', 'e', 'd', ']', 'B']

        # clear buffer
        UI_object.buffer_clear()

        # add characters to __buffer
        for char in character_list:
            UI_object.__buffer_add_char(char)
        
        for entry in UI_object.__buffer:
            print("")
            for key, value in entry.items():
                print("{}: {}".format(key, value))
        print("\nEntered: 'A#[91mB' into buffer where # is a special character")
        if (len(UI_object.__buffer) == 7
            and (UI_object.__buffer[0]['char'] == character_list[0]
                and UI_object.__buffer[0]['type'] == 'standard_char')
            and (UI_object.__buffer[2]['char'] == '['
                and UI_object.__buffer[2]['type'] == 'formatting_char') 
            and (UI_object.__buffer[3]['char'] == '9'
                and UI_object.__buffer[3]['type'] == 'formatting_char') 
            and (UI_object.__buffer[4]['char'] == '1'
                and UI_object.__buffer[4]['type'] == 'formatting_char') 
            and (UI_object.__buffer[5]['char'] == 'm'
                and UI_object.__buffer[5]['type'] == 'formatting_char') 
            and (UI_object.__buffer[6]['char'] == 'B'
                and UI_object.__buffer[6]['type'] == 'standard_char')
            and UI_object.__color == 'red'):
            
            print("{:<15}{}".format('CORRECT','Characters in buffer are correct'))
            
        else:

            print("{:<15}{}".format('INCORRECT','Characters in buffer are not'
                + ' correct.'))
            
            if all_tests_passed:
                all_tests_passed = False

        """ manually change __color and test removing color """
        UI_object.__color = 'blue'

        # update character_list - 'A[t03]B'
        character_list = ['A', '[', 'c', '-', 'n', 'o', 'n', 'e', ']', 'B']

        # clear buffer
        UI_object.buffer_clear()

        # add characters to __buffer
        for char in character_list:
            UI_object.__buffer_add_char(char)
        
        for entry in UI_object.__buffer:
            print("")
            for key, value in entry.items():
                print("{}: {}".format(key, value))
        print("\nEntered: 'A#[0mB' into buffer where # is a special character")
        if (len(UI_object.__buffer) == 6
            and (UI_object.__buffer[0]['char'] == character_list[0]
                and UI_object.__buffer[0]['type'] == 'standard_char')
            and (UI_object.__buffer[2]['char'] == '['
                and UI_object.__buffer[2]['type'] == 'formatting_char') 
            and (UI_object.__buffer[3]['char'] == '0'
                and UI_object.__buffer[3]['type'] == 'formatting_char') 
            and (UI_object.__buffer[4]['char'] == 'm'
                and UI_object.__buffer[4]['type'] == 'formatting_char') 
            and (UI_object.__buffer[5]['char'] == 'B'
                and UI_object.__buffer[5]['type'] == 'standard_char')
            and UI_object.__color == 'none'):
            
            print("{:<15}{}".format('CORRECT','Characters in buffer are correct'))
            
        else:

            print("{:<15}{}".format('INCORRECT','Characters in buffer are not'
                + ' correct.'))
            
            if all_tests_passed:
                all_tests_passed = False

        # test color instruction by rgb values
        
        # update character_list - 'A[t03]B'
        character_list = ['A', '[', 'c', '-', '2', '5', '5', ';', '2', '5', '5', 
            ';', '2', '5', '5', ']', 'B']

        # clear buffer
        UI_object.buffer_clear()

        # add characters to __buffer
        for char in character_list:
            UI_object.__buffer_add_char(char)
        
        for entry in UI_object.__buffer:
            print("")
            for key, value in entry.items():
                print("{}: {}".format(key, value))
        print("\nEntered: 'A#[38;2;255;255;255mB' into buffer where # is a special character")
        if (len(UI_object.__buffer) == 21
            and (UI_object.__buffer[0]['char'] == character_list[0]
                and UI_object.__buffer[0]['type'] == 'standard_char')
            and UI_object.__buffer[1]['type'] == 'formatting_char'
            and (UI_object.__buffer[2]['char'] == '['
                and UI_object.__buffer[2]['type'] == 'formatting_char') 
            and (UI_object.__buffer[3]['char'] == '3'
                and UI_object.__buffer[3]['type'] == 'formatting_char') 
            and (UI_object.__buffer[4]['char'] == '8'
                and UI_object.__buffer[4]['type'] == 'formatting_char') 
            and (UI_object.__buffer[5]['char'] == ';'
                and UI_object.__buffer[5]['type'] == 'formatting_char') 
            and (UI_object.__buffer[6]['char'] == '2'
                and UI_object.__buffer[6]['type'] == 'formatting_char') 
            and (UI_object.__buffer[7]['char'] == ';'
                and UI_object.__buffer[7]['type'] == 'formatting_char') 
            and (UI_object.__buffer[8]['char'] == '2'
                and UI_object.__buffer[8]['type'] == 'formatting_char') 
            and (UI_object.__buffer[9]['char'] == '5'
                and UI_object.__buffer[9]['type'] == 'formatting_char') 
            and (UI_object.__buffer[10]['char'] == '5'
                and UI_object.__buffer[10]['type'] == 'formatting_char') 
            and (UI_object.__buffer[11]['char'] == ';'
                and UI_object.__buffer[11]['type'] == 'formatting_char') 
            and (UI_object.__buffer[12]['char'] == '2'
                and UI_object.__buffer[12]['type'] == 'formatting_char') 
            and (UI_object.__buffer[13]['char'] == '5'
                and UI_object.__buffer[13]['type'] == 'formatting_char') 
            and (UI_object.__buffer[14]['char'] == '5'
                and UI_object.__buffer[14]['type'] == 'formatting_char') 
            and (UI_object.__buffer[15]['char'] == ';'
                and UI_object.__buffer[15]['type'] == 'formatting_char') 
            and (UI_object.__buffer[16]['char'] == '2'
                and UI_object.__buffer[16]['type'] == 'formatting_char') 
            and (UI_object.__buffer[17]['char'] == '5'
                and UI_object.__buffer[17]['type'] == 'formatting_char') 
            and (UI_object.__buffer[18]['char'] == '5'
                and UI_object.__buffer[18]['type'] == 'formatting_char') 
            and (UI_object.__buffer[19]['char'] == 'm'
                and UI_object.__buffer[19]['type'] == 'formatting_char')
            and (UI_object.__buffer[20]['char'] == 'B'
                and UI_object.__buffer[20]['type'] == 'standard_char')
            and UI_object.__color == '255;255;255'):
            
            print("{:<15}{}".format('CORRECT','Characters in buffer are correct'))
            
        else:

            print("{:<15}{}".format('INCORRECT','Characters in buffer are not'
                + ' correct.'))
            
            if all_tests_passed:
                all_tests_passed = False

        """ test bold, italics, underline and strikethrough toggling on """

        # test bold - toggle on
        
        print("\nTesting [b] instruction.")
        
        # set starting string and processed character list
        starting_string = 'A[b]B'
        processed_character_list = [
            {'char': 'A', 'type': 'standard_char'},
            {'char': '#', 'type': 'formatting_char'},
            {'char': '[', 'type': 'formatting_char'},
            {'char': '1', 'type': 'formatting_char'},
            {'char': 'm', 'type': 'formatting_char'},
            {'char': 'B', 'type': 'standard_char'}
        ]

        # clear buffer
        UI_object.buffer_clear()

        # add characters to __buffer
        for i in range(len(starting_string)):
            UI_object.__buffer_add_char(starting_string[i])

        # set variable for current test result
        current_test_passed = True

        print("Characters after processing are: ", end='')
        
        # check characters in the buffer
        for i in range(len(processed_character_list)):
            
            print(processed_character_list[i]['char'], end='')
            
            if not ((processed_character_list[i]['char'] == '#'
                    and UI_object.__buffer[i]['type'] 
                    == 'formatting_char')
                or (processed_character_list[i]['char'] != '#'
                    and UI_object.__buffer[i]['char'] 
                        == processed_character_list[i]['char']
                    and UI_object.__buffer[i]['type']
                        == processed_character_list[i]['type'])):
                
                # update current_test_passed to False as test failed
                if current_test_passed:
                    current_test_passed = False
        
        print("")

        # print results of current test
        if current_test_passed:
        
            print("{:<15}{}".format('CORRECT','Characters in buffer are correct'))
            
        else:

            print("{:<15}{}".format('INCORRECT','Characters in buffer are not'
                + ' correct.'))
            
            if all_tests_passed:
                all_tests_passed = False

        # test [i]
        print("\nTesting [i] instruction.")
        
        # set starting string and processed character list
        starting_string = 'A[i]B'
        processed_character_list = [
            {'char': 'A', 'type': 'standard_char'},
            {'char': '#', 'type': 'formatting_char'},
            {'char': '[', 'type': 'formatting_char'},
            {'char': '3', 'type': 'formatting_char'},
            {'char': 'm', 'type': 'formatting_char'},
            {'char': 'B', 'type': 'standard_char'}
        ]

        # clear buffer
        UI_object.buffer_clear()

        # add characters to __buffer
        for i in range(len(starting_string)):
            UI_object.__buffer_add_char(starting_string[i])

        # set variable for current test result
        current_test_passed = True

        print("Characters after processing are: ", end='')
        
        # check characters in the buffer
        for i in range(len(processed_character_list)):
            
            print(processed_character_list[i]['char'], end='')
            
            if not ((processed_character_list[i]['char'] == '#'
                    and UI_object.__buffer[i]['type'] 
                    == 'formatting_char')
                or (processed_character_list[i]['char'] != '#'
                    and UI_object.__buffer[i]['char'] 
                        == processed_character_list[i]['char']
                    and UI_object.__buffer[i]['type']
                        == processed_character_list[i]['type'])):
                
                # update current_test_passed to False as test failed
                if current_test_passed:
                    current_test_passed = False
        
        print("")

        # print results of current test
        if current_test_passed:
        
            print("{:<15}{}".format('CORRECT','Characters in buffer are correct'))
            
        else:

            print("{:<15}{}".format('INCORRECT','Characters in buffer are not'
                + ' correct.'))
            
            if all_tests_passed:
                all_tests_passed = False
        
        # test [s]
        print("\nTesting [s] instruction.")
        
        # set starting string and processed character list
        starting_string = 'A[s]B'
        processed_character_list = [
            {'char': 'A', 'type': 'standard_char'},
            {'char': '#', 'type': 'formatting_char'},
            {'char': '[', 'type': 'formatting_char'},
            {'char': '9', 'type': 'formatting_char'},
            {'char': 'm', 'type': 'formatting_char'},
            {'char': 'B', 'type': 'standard_char'}
        ]

        # clear buffer
        UI_object.buffer_clear()

        # add characters to __buffer
        for i in range(len(starting_string)):
            UI_object.__buffer_add_char(starting_string[i])

        # set variable for current test result
        current_test_passed = True

        print("Characters after processing are: ", end='')
        
        # check characters in the buffer
        for i in range(len(processed_character_list)):
            
            print(processed_character_list[i]['char'], end='')
            
            if not ((processed_character_list[i]['char'] == '#'
                    and UI_object.__buffer[i]['type'] 
                    == 'formatting_char')
                or (processed_character_list[i]['char'] != '#'
                    and UI_object.__buffer[i]['char'] 
                        == processed_character_list[i]['char']
                    and UI_object.__buffer[i]['type']
                        == processed_character_list[i]['type'])):
                
                # update current_test_passed to False as test failed
                if current_test_passed:
                    current_test_passed = False
        
        print("")

        # print results of current test
        if current_test_passed:
        
            print("{:<15}{}".format('CORRECT','Characters in buffer are correct'))
            
        else:

            print("{:<15}{}".format('INCORRECT','Characters in buffer are not'
                + ' correct.'))
            
            if all_tests_passed:
                all_tests_passed = False
        
        # test [u]
        print("\nTesting [u] instruction.")
        
        # set starting string and processed character list
        starting_string = 'A[u]B'
        processed_character_list = [
            {'char': 'A', 'type': 'standard_char'},
            {'char': '#', 'type': 'formatting_char'},
            {'char': '[', 'type': 'formatting_char'},
            {'char': '4', 'type': 'formatting_char'},
            {'char': 'm', 'type': 'formatting_char'},
            {'char': 'B', 'type': 'standard_char'}
        ]

        # clear buffer
        UI_object.buffer_clear()

        # add characters to __buffer
        for i in range(len(starting_string)):
            UI_object.__buffer_add_char(starting_string[i])

        # set variable for current test result
        current_test_passed = True

        print("Characters after processing are: ", end='')
        
        # check characters in the buffer
        for i in range(len(processed_character_list)):
            
            print(processed_character_list[i]['char'], end='')
            
            if not ((processed_character_list[i]['char'] == '#'
                    and UI_object.__buffer[i]['type'] 
                    == 'formatting_char')
                or (processed_character_list[i]['char'] != '#'
                    and UI_object.__buffer[i]['char'] 
                        == processed_character_list[i]['char']
                    and UI_object.__buffer[i]['type']
                        == processed_character_list[i]['type'])):
                
                # update current_test_passed to False as test failed
                if current_test_passed:
                    current_test_passed = False
        
        print("")

        # print results of current test
        if current_test_passed:
        
            print("{:<15}{}".format('CORRECT','Characters in buffer are correct'))
            
        else:

            print("{:<15}{}".format('INCORRECT','Characters in buffer are not'
                + ' correct.'))
            
            if all_tests_passed:
                all_tests_passed = False

        print("After toggling on bold, italics, underline, and strikethrough"
            + " the attributes are:")
        print("Bold: {}".format(UI_object.__bold))
        print("Italics: {}".format(UI_object.__italics))
        print("Underline: {}".format(UI_object.__underline))
        print("Strikethrough: {}".format(UI_object.__strikethrough))
        input("Press any key to continue")

        """ test bold, italics, underline and strikethrough toggling off """

        # test bold - toggle off
        
        print("\nTesting [b] instruction for toggle off.")
        
        # set starting string and processed character list
        starting_string = 'C[b]D'
        processed_character_list = [
            {'char': 'C', 'type': 'standard_char'},
            {'char': '#', 'type': 'formatting_char'},
            {'char': '[', 'type': 'formatting_char'},
            {'char': '0', 'type': 'formatting_char'},
            {'char': 'm', 'type': 'formatting_char'},
            {'char': '#', 'type': 'formatting_char'},
            {'char': '[', 'type': 'formatting_char'},
            {'char': '3', 'type': 'formatting_char'},
            {'char': 'm', 'type': 'formatting_char'},
            {'char': '#', 'type': 'formatting_char'},
            {'char': '[', 'type': 'formatting_char'},
            {'char': '9', 'type': 'formatting_char'},
            {'char': 'm', 'type': 'formatting_char'},
            {'char': '#', 'type': 'formatting_char'},
            {'char': '[', 'type': 'formatting_char'},
            {'char': '4', 'type': 'formatting_char'},
            {'char': 'm', 'type': 'formatting_char'},
            {'char': '#', 'type': 'formatting_char'},
            {'char': '[', 'type': 'formatting_char'},
            {'char': '3', 'type': 'formatting_char'},
            {'char': '8', 'type': 'formatting_char'},
            {'char': ';', 'type': 'formatting_char'},
            {'char': '2', 'type': 'formatting_char'},
            {'char': ';', 'type': 'formatting_char'},
            {'char': '2', 'type': 'formatting_char'},
            {'char': '5', 'type': 'formatting_char'},
            {'char': '5', 'type': 'formatting_char'},
            {'char': ';', 'type': 'formatting_char'},
            {'char': '2', 'type': 'formatting_char'},
            {'char': '5', 'type': 'formatting_char'},
            {'char': '5', 'type': 'formatting_char'},
            {'char': ';', 'type': 'formatting_char'},
            {'char': '2', 'type': 'formatting_char'},
            {'char': '5', 'type': 'formatting_char'},
            {'char': '5', 'type': 'formatting_char'},
            {'char': 'm', 'type': 'formatting_char'},
            {'char': 'D', 'type': 'standard_char'}
        ]

        # clear buffer
        UI_object.buffer_clear()

        # add characters to __buffer
        for i in range(len(starting_string)):
            UI_object.__buffer_add_char(starting_string[i])

        # set variable for current test result
        current_test_passed = True

        print("Characters after processing are: ", end='')
        
        # check characters in the buffer
        for i in range(len(processed_character_list)):
            
            print(processed_character_list[i]['char'], end='')
            
            if not ((processed_character_list[i]['char'] == '#'
                    and UI_object.__buffer[i]['type'] 
                    == 'formatting_char')
                or (processed_character_list[i]['char'] != '#'
                    and UI_object.__buffer[i]['char'] 
                        == processed_character_list[i]['char']
                    and UI_object.__buffer[i]['type']
                        == processed_character_list[i]['type'])):
                
                # update current_test_passed to False as test failed
                if current_test_passed:
                    current_test_passed = False
        
        print("")

        # print results of current test
        if current_test_passed:
        
            print("{:<15}{}".format('CORRECT','Characters in buffer are correct'))
            
        else:

            print("{:<15}{}".format('INCORRECT','Characters in buffer are not'
                + ' correct.'))
            
            if all_tests_passed:
                all_tests_passed = False
        
        # test italics - toggle off
        
        print("\nTesting [i] instruction for toggle off.")
        
        # set starting string and processed character list
        starting_string = 'C[i]D'
        processed_character_list = [
            {'char': 'C', 'type': 'standard_char'},
            {'char': '#', 'type': 'formatting_char'},
            {'char': '[', 'type': 'formatting_char'},
            {'char': '0', 'type': 'formatting_char'},
            {'char': 'm', 'type': 'formatting_char'},
            {'char': '#', 'type': 'formatting_char'},
            {'char': '[', 'type': 'formatting_char'},
            {'char': '9', 'type': 'formatting_char'},
            {'char': 'm', 'type': 'formatting_char'},
            {'char': '#', 'type': 'formatting_char'},
            {'char': '[', 'type': 'formatting_char'},
            {'char': '4', 'type': 'formatting_char'},
            {'char': 'm', 'type': 'formatting_char'},
            {'char': '#', 'type': 'formatting_char'},
            {'char': '[', 'type': 'formatting_char'},
            {'char': '3', 'type': 'formatting_char'},
            {'char': '8', 'type': 'formatting_char'},
            {'char': ';', 'type': 'formatting_char'},
            {'char': '2', 'type': 'formatting_char'},
            {'char': ';', 'type': 'formatting_char'},
            {'char': '2', 'type': 'formatting_char'},
            {'char': '5', 'type': 'formatting_char'},
            {'char': '5', 'type': 'formatting_char'},
            {'char': ';', 'type': 'formatting_char'},
            {'char': '2', 'type': 'formatting_char'},
            {'char': '5', 'type': 'formatting_char'},
            {'char': '5', 'type': 'formatting_char'},
            {'char': ';', 'type': 'formatting_char'},
            {'char': '2', 'type': 'formatting_char'},
            {'char': '5', 'type': 'formatting_char'},
            {'char': '5', 'type': 'formatting_char'},
            {'char': 'm', 'type': 'formatting_char'},
            {'char': 'D', 'type': 'standard_char'}
        ]

        # clear buffer
        UI_object.buffer_clear()

        # add characters to __buffer
        for i in range(len(starting_string)):
            UI_object.__buffer_add_char(starting_string[i])

        # set variable for current test result
        current_test_passed = True

        print("Characters after processing are: ", end='')
        
        # check characters in the buffer
        for i in range(len(processed_character_list)):
            
            print(processed_character_list[i]['char'], end='')
            
            if not ((processed_character_list[i]['char'] == '#'
                    and UI_object.__buffer[i]['type'] 
                    == 'formatting_char')
                or (processed_character_list[i]['char'] != '#'
                    and UI_object.__buffer[i]['char'] 
                        == processed_character_list[i]['char']
                    and UI_object.__buffer[i]['type']
                        == processed_character_list[i]['type'])):
                
                # update current_test_passed to False as test failed
                if current_test_passed:
                    current_test_passed = False
        
        print("")

        # print results of current test
        if current_test_passed:
        
            print("{:<15}{}".format('CORRECT','Characters in buffer are correct'))
            
        else:

            print("{:<15}{}".format('INCORRECT','Characters in buffer are not'
                + ' correct.'))
            
            if all_tests_passed:
                all_tests_passed = False
        
        # test strikethrough - toggle off
        
        print("\nTesting [s] instruction for toggle off.")
        
        # set starting string and processed character list
        starting_string = 'C[s]D'
        processed_character_list = [
            {'char': 'C', 'type': 'standard_char'},
            {'char': '#', 'type': 'formatting_char'},
            {'char': '[', 'type': 'formatting_char'},
            {'char': '0', 'type': 'formatting_char'},
            {'char': 'm', 'type': 'formatting_char'},
            {'char': '#', 'type': 'formatting_char'},
            {'char': '[', 'type': 'formatting_char'},
            {'char': '4', 'type': 'formatting_char'},
            {'char': 'm', 'type': 'formatting_char'},
            {'char': '#', 'type': 'formatting_char'},
            {'char': '[', 'type': 'formatting_char'},
            {'char': '3', 'type': 'formatting_char'},
            {'char': '8', 'type': 'formatting_char'},
            {'char': ';', 'type': 'formatting_char'},
            {'char': '2', 'type': 'formatting_char'},
            {'char': ';', 'type': 'formatting_char'},
            {'char': '2', 'type': 'formatting_char'},
            {'char': '5', 'type': 'formatting_char'},
            {'char': '5', 'type': 'formatting_char'},
            {'char': ';', 'type': 'formatting_char'},
            {'char': '2', 'type': 'formatting_char'},
            {'char': '5', 'type': 'formatting_char'},
            {'char': '5', 'type': 'formatting_char'},
            {'char': ';', 'type': 'formatting_char'},
            {'char': '2', 'type': 'formatting_char'},
            {'char': '5', 'type': 'formatting_char'},
            {'char': '5', 'type': 'formatting_char'},
            {'char': 'm', 'type': 'formatting_char'},
            {'char': 'D', 'type': 'standard_char'}
        ]

        # clear buffer
        UI_object.buffer_clear()

        # add characters to __buffer
        for i in range(len(starting_string)):
            UI_object.__buffer_add_char(starting_string[i])

        # set variable for current test result
        current_test_passed = True

        print("Characters after processing are: ", end='')
        
        # check characters in the buffer
        for i in range(len(processed_character_list)):
            
            print(processed_character_list[i]['char'], end='')
            
            if not ((processed_character_list[i]['char'] == '#'
                    and UI_object.__buffer[i]['type'] 
                    == 'formatting_char')
                or (processed_character_list[i]['char'] != '#'
                    and UI_object.__buffer[i]['char'] 
                        == processed_character_list[i]['char']
                    and UI_object.__buffer[i]['type']
                        == processed_character_list[i]['type'])):
                
                # update current_test_passed to False as test failed
                if current_test_passed:
                    current_test_passed = False
        
        print("")

        # print results of current test
        if current_test_passed:
        
            print("{:<15}{}".format('CORRECT','Characters in buffer are correct'))
            
        else:

            print("{:<15}{}".format('INCORRECT','Characters in buffer are not'
                + ' correct.'))
            
            if all_tests_passed:
                all_tests_passed = False
        
        # test strikethrough - toggle off
        
        print("\nTesting [u] instruction for toggle off.")
        
        # set starting string and processed character list
        starting_string = 'C[u]D'
        processed_character_list = [
            {'char': 'C', 'type': 'standard_char'},
            {'char': '#', 'type': 'formatting_char'},
            {'char': '[', 'type': 'formatting_char'},
            {'char': '0', 'type': 'formatting_char'},
            {'char': 'm', 'type': 'formatting_char'},
            {'char': '#', 'type': 'formatting_char'},
            {'char': '[', 'type': 'formatting_char'},
            {'char': '3', 'type': 'formatting_char'},
            {'char': '8', 'type': 'formatting_char'},
            {'char': ';', 'type': 'formatting_char'},
            {'char': '2', 'type': 'formatting_char'},
            {'char': ';', 'type': 'formatting_char'},
            {'char': '2', 'type': 'formatting_char'},
            {'char': '5', 'type': 'formatting_char'},
            {'char': '5', 'type': 'formatting_char'},
            {'char': ';', 'type': 'formatting_char'},
            {'char': '2', 'type': 'formatting_char'},
            {'char': '5', 'type': 'formatting_char'},
            {'char': '5', 'type': 'formatting_char'},
            {'char': ';', 'type': 'formatting_char'},
            {'char': '2', 'type': 'formatting_char'},
            {'char': '5', 'type': 'formatting_char'},
            {'char': '5', 'type': 'formatting_char'},
            {'char': 'm', 'type': 'formatting_char'},
            {'char': 'D', 'type': 'standard_char'}
        ]

        # clear buffer
        UI_object.buffer_clear()

        # add characters to __buffer
        for i in range(len(starting_string)):
            UI_object.__buffer_add_char(starting_string[i])

        # set variable for current test result
        current_test_passed = True

        print("Characters after processing are: ", end='')
        
        # check characters in the buffer
        for i in range(len(processed_character_list)):
            
            print(processed_character_list[i]['char'], end='')
            
            if not ((processed_character_list[i]['char'] == '#'
                    and UI_object.__buffer[i]['type'] 
                    == 'formatting_char')
                or (processed_character_list[i]['char'] != '#'
                    and UI_object.__buffer[i]['char'] 
                        == processed_character_list[i]['char']
                    and UI_object.__buffer[i]['type']
                        == processed_character_list[i]['type'])):
                
                # update current_test_passed to False as test failed
                if current_test_passed:
                    current_test_passed = False
        
        print("")

        # print results of current test
        if current_test_passed:
        
            print("{:<15}{}".format('CORRECT','Characters in buffer are correct'))
            
        else:

            print("{:<15}{}".format('INCORRECT','Characters in buffer are not'
                + ' correct.'))
            
            if all_tests_passed:
                all_tests_passed = False

        
        # print values for bold, italics, underline and strikethrough attributes
        print("After toggling on bold, italics, underline, and strikethrough"
            + " the attributes are:")
        print("Bold: {}".format(UI_object.__bold))
        print("Italics: {}".format(UI_object.__italics))
        print("Underline: {}".format(UI_object.__underline))
        print("Strikethrough: {}".format(UI_object.__strikethrough))
        input("Press any key to continue")

        """ clear text color so all formatting was removed """
        UI_object.__color = 'none'

        """
        Test convert_message and buffer_load_message
        """

        new_message = ('Test message using bold[b], blue text[c-blue], indent 10'
            + '[i10] then a new line[n]removing bold[b] and changing color to white'
            + '[c-255;255;255] before having a tab 5[t05] and removing color'
            + '[c-none] to finish.')
        
        # clear buffer
        UI_object.buffer_clear()

        # load new_message into buffer
        UI_object.__buffer_load_message(new_message)

        print("\nAfter adding characters to buffer, buffer is: ")

        # print text in buffer
        for i in range(len(UI_object.__buffer)):

            if UI_object.__buffer[i]['char'] == '\x1b':
                print('#', end='')
            else:
                print(UI_object.__buffer[i]['char'], end='')
        
        # get text from buffer and print details received
        print("\nTesting __buffer_return_text_portion()")

        while UI_object.__buffer:

            # get text portion from buffer
            text_portion, num_chars, text_type = UI_object.__buffer_return_text_portion()

            print("Returned: '{}' with {} characters of type {}".format(
                text_portion, num_chars, text_type))
        
        print("Buffer is empty {}".format(UI_object.__buffer_is_empty()))

        message_to_test_printing = ('0123456789012345678901234567890123456789'
            + '0123456789012345678901234567890123456789'
            + ' 0123456789012345678901234567890123456789'
            + '0123456789012345678901234567890123456789'
            + 'Test message. No indents or formatting. Indent 10[i10] for next line'
            + ' while making bold[b] and then underlined[u] and blue.[c-blue]'
            + ' Now change[b] to white[c-255;255;255] using rgb. Make strikethrough'
            + ' [s] before using a new line.[n] Now remove strikethrough[s] but'
            + ' add italics[i] and use a tab of 5[t05]. Clear formatting[i][u][b]'
            + '[c-none] so back to normal')
        
        printable_message_list = TerminalPrinter.convert_message(message_to_test_printing)
        print("\nThe following message has numbers that fill the line followed"
              + " by a space then numbers with 'test' appended that exceed"
              + " a full line and should be split. Note that the space should"
              + " not appear as it is at the beginning of a line without"
              + " characters and should be ignored.\n")
        for message in printable_message_list:
            print(message)

        printable_message_list_02 = TerminalPrinter.convert_message(
            message_to_test_printing, PARAGRAPH_WIDTH=100, TEXT_INDENT=5, 
            FOLLOWING_LINE_INDENT=10)
        print("\nThe following text is the same as the previous text. Paragraph"
            + " width has been increased by 20. All text has been indented 5 and"
            + " an additional indent of 10 on each line after the first has"
            + " also been applied.\n")
        for i in range(len(printable_message_list_02)):
            if i != len(printable_message_list_02) - 1:
                print(printable_message_list_02[i])
            else:
                print(printable_message_list_02[i], end='')
        print(" Text didn't have a new line at the end")

            

        
        input("Quit")


        """
        Print final result for tests
        """
        if all_tests_passed:
            print("\nPASSED: All tests for TerminalPrinter were passed.")
        else:
            print("\nFAILED. At least one test for TerminalPrinter was failed.")
        

