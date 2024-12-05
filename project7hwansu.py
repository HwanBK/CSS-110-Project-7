# CSC 110
# Project 7
# Hwansu Kim (Billy)
# Program that fixes clerical data within a customer's information.


# Replaces alphabetic characters with proper numeric characters, if found.
def fixCustNum(customerNum):
    if not customerNum.isdigit():
        fixedNum = int(customerNum.replace("O", "0").replace("l", "1"))
    else:
        fixedNum = int(customerNum)

    return fixedNum


# Removes any unnecessary white space and splits customer's full name into last and first names.
def fixCustName(customerName):
    fixedName = customerName.replace("  ", " ").split(",")
    lastName, firstName = fixedName[0].strip(), fixedName[1].strip()

    return lastName, firstName


# Removes unnecessary characters and splits the customer's full phone number into area code and main phone number.
def fixCustPhone(customerPhoneNum):
    customerPhoneNum = customerPhoneNum.replace("(", "").replace(")", "").replace("-", "")
    areaCode, phoneNum = customerPhoneNum[0:3], customerPhoneNum[3:11]

    return areaCode, phoneNum


# Removes unnecessary characters before converting string into floating-point number. Also returns a floating-point
# number when an empty string is provided.
def fixCustBalance(customerBalance):
    if customerBalance == "":
        customerBalance = "0.00"
    fixedBalance = float(customerBalance.lstrip("$").replace(",", ""))

    return fixedBalance


# Takes in customer's information, as a string, before function calls.
def main():
    custData = input("Enter customer data: ")
    custList = custData.split("#")
    custNum, custName, custPhoneNum, custBalance = custList[0], custList[1], custList[2], custList[3]

    print("Customer number",     format(":", ">5"), fixCustNum(custNum))

    custLastName, custFirstName = fixCustName(custName)
    print("Customer last name",  format(":", ">2"), custLastName)
    print("Customer first name", format(":", ">1"), custFirstName)

    custAreaCode, custMainNum = fixCustPhone(custPhoneNum)
    print("Customer area code",  format(":", ">2"), custAreaCode)
    print("Customer phone",      format(":", ">6"), custMainNum)

    print("Customer balance",    format(":", ">4"), format(fixCustBalance(custBalance), ".2f"))


if __name__ == "__main__":
    main()


# SUMMARY
#   I started this project by analyzing the project rubric, call hierarchy, and the field specifics provided. After
# establishing a decent mental floor-plan of the individual functions I started coding the functions one-by-one, using
# the provided sample string for testing. The one instance I got stuck was while I was working on the fixCustName
# function. I had started to overthink about where the accidental double spaces could occur, and started to think that
# double spaces could appear in the middle of a name, like "Ch  ris", but after re-reading the project's guidelines, I
# realized that double spaces only happen in spots where a single space should be present. Otherwise, this project was
# simple enough that I didn't really get stuck anywhere.
#   For testing, I had mostly relied on the sample string provided for the majority of the coding process. After my code
# properly output the fixed up strings, integer, and float, I started to create PyUnit tests for the functions, with
# test cases that specifically tested critical points. For once, everything works as intended, so I don't feel like
# something is inadequate or missing. Although, there are additional hypothetical errors I thought of, that don't
# need to be covered by the project, that could occur and cause problems with the existing code.
#   This assignment was great practice for string and list manipulation; I've gotten a much stronger grasp on  the
# methods used to alter strings and return boolean values based on the string's contents. And using this knowledge, for
# future projects, I'll be able to manipulate strings in a more eloquent way, unlike prior to this project; especially
# since we'll be moving onto lists in an upcoming project.

# TEST CASES
# fixCustNum Function
#   -Properly returns an integer.
#       -No chance of breaking, by returning non-numerical characters, due to the selection statement; which requires
#        all the characters in the string to be numeric, or all possible alphabetic characters, "O" and "l", to be
#        replaced with the proper numeric characters, "0" and "1".
#       -If a number beginning with zeroes is entered, the integer conversion removes the zeroes.
#           -Potential issue if all customer numbers require a specific character count.
#           -"OOO111" is returned as 111.
#   -PyUnit tests:
#       -Passed string that is only numeric.
#       -Passed string that is only alphabetic.
#       -Passed string that is alphanumeric.

# fixCustName Function
#   -Properly returns two strings.
#       -Properly removes any white space at the beginning and the end of names.
#       -Properly replaces double spaces with a single space.
#   -PyUnit tests:
#       -Passed string with no spacing errors.
#       -Passed string with single and double spacing errors only at the beginning and the end of the string.
#       -Passed string with double spacing errors in between two-worded names.

# fixCustPhone Function
#   -Properly returns two strings.
#       -Properly replaces "(", ")", and "-" with an empty string.
#       -Properly passes the first three indexes of the modified string as the area code.
#       -Properly passes the remaining indexes as the phone number.
#           -This will break in the instances of unique phone numbers, like 911; granted no one realistically would be
#            providing 911 as their own contact information.
#               -Another example would be commercial phone numbers that start with 1-800.
#               -Also international phone numbers, which might exceed ten digits.
#   -PyUnit tests
#       -Passed standard ten digit strings (phone numbers).
#           -Passed string with no parenthesis or hyphens.
#           -Passed string with parenthesis included.
#           -Passed string with hyphens included.
#           -Passed string with parenthesis and hyphens included.

# fixCustBalance Function
#   -Properly returns a floating-point number.
#       -If no string is passed, properly returns "0.00" before float conversion.
#       -Properly strips "$" and commas included in the string.
#       -Breaks if alphabetical characters are included, due to float conversion.
#           -"Five dollars"
#   -PyUnit tests
#       -Passed string without "$" or commas.
#       -Passed string with "$".
#       -Passed string with commas.
#       -Passed string with "$" and commas.
#       -Passed empty string, returned floating-point number 0.00.

# main Function
#   -Properly takes string input.
#       -Properly splits string at "#".
#       -Properly assigns list's indexes to variables to be used as parameters for function calls.
#       -Output aligns neatly and properly.