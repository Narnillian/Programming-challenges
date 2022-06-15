val vowels = "aeiou"

fun multiply(string: String, factor: Int): String {
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
        print("Please enter a string to multiply: ")
        string = readln()
        print("Please enter a number to multiply each vowel by: ")
        factor = readln().toInt()
    }
    println(multiply(string, factor))
}