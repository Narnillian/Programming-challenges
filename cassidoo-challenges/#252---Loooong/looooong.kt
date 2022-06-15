val underline = "\u001b[4m"
val bold = "\u001b[1m"
val reset = "\u001b[0m"

fun multiply(string: String, factor: Int): String {
    val vowels = "aeiou"
    var result = ""
    for (letter in string) {
        if (letter in vowels) {
            for (i in 1..factor) {
                result += letter
            }
        }
        else result += letter
    }
    return result
}



fun main(argv: Array<String>) {
    var string = ""
    var factor = 3
    if (argv.size>0) {
        var test = true
        for (i in argv) {
            if (test) {
                try { factor = i.toInt(); test = false}
                catch(e: NumberFormatException) { println("Please make sure your first argument is a valid number");return }
            } else string += i.plus(" ")
        }
    } else {
        print("${underline}Please enter a string to multiply:${reset} ")
        string = readln()
        print("${underline}Please enter a number to multiply each vowel by:${reset} ")
        factor = readln().toInt()
    }
    println("\nResult:")
    println("${bold}${multiply(string, factor)}${reset}")
}