
# Define the ASCII art for each character
ascii_art = {
    'A': r'''
       A
      A A
     A   A
    AAAAAAA
   A       A
  A         A
''',
    'D': r'''
    DDDDD
    D    D
    D     D
    D     D
    D    D
    DDDDD
''',
    'V': r'''
V           V
 V         V
  V       V
   V     V
    V   V
     V V
      V
''',
    'E': r'''
EEEEEE
E
E
EEEE
E
EEEEEE
''',
    'N': r'''
N       N
NN      N
N N     N
N  N    N
N   N   N
N    N  N
N     N N
N      NN
N       N
'''
}

# The word to be displayed
word = "ADVENTURE"

# Function to print the ASCII art for a given word
def print_ascii_art(word):
    for letter in word:
        if letter in ascii_art:
            print(ascii_art[letter], end=' ')
        else:
            print("  ", end=' ')
    print()

print_ascii_art(word)



ascii_art2 = '''
                .-"    `-.      ,
               .'          '.   /j\\
              /              \\,/:/#\\                /\\ 
             ;              ,//' '/#\\              //#\\
             |             /' :   '/#\\            /  /#\\
             :         ,  /' /'    '/#\\__..--""""/    /#\\__
              \\       /'\\'-._:__    '/#\\        ;      /#, """---
               `-.   / ;#\\']" ; """--./#J       ':____...!
                 `-/   /#\\  J  [;[;[;Y]         |      ;
""""""---....             __.--"/    '/#\\ ;   " "  |     !    |   #! |
             ""--.. _.--""     /      ,/#\\'-..____.;_,   |    |   '  |
                   "-.        :_....___,/#} "####" | '_.-",   | #['  |
                      '-._      |[;[;[;[;|         |.;'  /;\\  |      |
                      ,   `-.   |        :     _   .;'    /;\\ |   #" |
                      !      `._:      _  ;   ##' .;'      /;\\|  _,  |
                     .#\"""---..._    ';, |      .;{___     /;\\  ]#' |__....--
          .--.      ;'/#\\         \\    ]! |       "| , """--./_J    /
         /  '%;    /  '/#\\         \\   !' :        |!# #! #! #|    :`.__
        i__..'%] _:_   ;##J         \\      :"#...._!   '  "  "|__  |    `--.._
         | .--""" !|""""  |"""----...J     | '##"" `-._       |  """---.._
     ____: |      #|      |         #|     |          "]      ;   ___...-"T,
    /   :  :      !|      |   _______!_    |           |__..--;"""     ,;MM;
   :____| :    .-.#|      |  /\\      /#\\   |          /'               ''MM;
    |""": |   /   \\|   .----+  ;      /#\\  :___..--"";                  ,'MM;
   _Y--:  |  ;     ;.-'      ;  \\______/#: /         ;                  ''MM;
  /    |  | ;_______;     ____!  |"##"""MM!         ;                    ,'MM;
 !_____|  |  |"#"#"|____.'""##"  |       :         ;                     ''MM
  | """"--!._|     |##""         !       !         :____.....-------"""""" |'
  |          :     |______                        ___!_ "#""#""#"""#"""#"""|
__|          ;     |MM"MM"""""---..._______...--""MM"MM]                   |
  "\\-.      :      |#                                  :                   |
    /#'.    |      /##,                                !                   |
   .',/'\\   |       #:#,                                ;       .==.       |
  /"\\'#"\',.|       ##;#,                               !     ,'||||',     |
        /;/`:       ######,          ____             _ :     M||||||M     |
       ###          /;"\\.__"-._   """                   |===..M!!!!!!M_____|
                           `--..`--.._____             _!_
                                          `--...____,="_.'`-.____        fsc
'''

print(" you have arrived at a castle...")
print( "what will you do")
print_ascii_art("ADVENTURE")