#   THE FOLLOWING IS A BASIC LEXICAL ANALYZER
#   IT GENERATES TOKEN FOR INTEGER AT THE MOMENT
#   IT WORKS FOR "=" OPERATOR FOR NOW


# REMOVES WHITESPACE FROM THE PROVIDED EXPRESSION
def remove_whitespace():
    global final_string
    for item in expression:     # FOR EACH ITEM IN EXPRESSION
        # index += 1
        if item not in [" ", "\t", "\n"]:
            final_string += item            # IF NO SPACE, STORE ITEM IN FINAL_STRING
    return final_string


#   FINDS THE KEYWORDS IN THE MODIFIED EXPRESSION
def find_keywords(string1):
    keywords = ["int", "float", "str"]      # LIST OF KEYWORDS
    for x in keywords:                    # FOR EACH KEYWORD
        if x in string1:                 # KEYWORD IN STRING?
            output_tokens.append("<"+x+">")     # APPEND KEYWORD IN THE OUTPUT_TOKEN
            string2 = string1.replace(x, "")    # REMOVE THE KEYWORD FROM STRING
    find_identifier(string2)                    # FIND IDENTIFIERS AND OPERATORS


#   FINDS IDENTIFIERS AND OPERATORS
def find_identifier(string3):
    id_count = 0
    operator = ["=", "!=", "+=", "-="]          # DEFINE OPERATORS
    for x in operator:                          # FOR EACH OPERATOR
        if x in string3:
            id_count += 1
            string4 = string3.split(x)          # SPLIT 2 SIDES OF OPERATOR
            token[str(id_count)] = "<"+string4[0]+">"   # STORE THE IDENTIFIER TOKENS
            output_tokens.append(token)         # ADD IDENTIFIER TOKENS
            output_tokens.append("<"+x+">")     # ADD OPERATOR TOKEN
            if string4[1].isdigit():
                output_tokens.append("<"+string4[1]+">")    # CHECK FOR INTEGER AND ADD OUTPUT_TOKEN


def generate_tokens(fstring):
    find_keywords(fstring)


expression = "int var90 = 1103"    # GIVEN EXPRESSION
final_string = ""
output_tokens = []
token = {}
remove_whitespace()
generate_tokens(final_string)

print(output_tokens)




