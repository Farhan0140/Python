
with open( 'Python/Basic Python/message.txt', 'w' ) as File:
    File.write( "I Love Python" )



with open( 'Python/Basic Python/message.txt', 'a' ) as File:
    File.write( "I Love Python\n" )



with open( 'Python/Basic Python/message.txt', 'r' ) as File:
    from_file = File.read()
    print(from_file)