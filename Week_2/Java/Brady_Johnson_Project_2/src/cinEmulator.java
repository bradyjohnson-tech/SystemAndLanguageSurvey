import java.math.BigDecimal;
import java.math.BigInteger;
import java.math.RoundingMode;
import java.util.InputMismatchException;
import java.util.Scanner;

public class cinEmulator {
    boolean failed_state = false;
    int number;

    Scanner scanner = new Scanner(System.in);

    public int handleInput(){
        if(failed_state){
            return number;
        }

        String input = scanner.nextLine();
        input = extractLeadingNumbers(input);
        if (isInteger(input)) {
            return Integer.parseInt(input);
        } else if (isDouble(input)) {
            return convertDoubleToInteger(input);
        }
        throw new InputMismatchException();
    }

    // extractLeadingNumbers method is augmented with AI generated code.
    private String extractLeadingNumbers(String input) {
        String regex = "^\\d+"; // Regular expression to match leading digits
        java.util.regex.Pattern pattern = java.util.regex.Pattern.compile(regex); // Create a pattern
        java.util.regex.Matcher matcher = pattern.matcher(input); // Match the pattern against the input string
        if (matcher.find()) { // If a match is found, return the matched numbers
            if (!matcher.group().equals(input)) {
                failed_state = true;
            }
            return matcher.group();
        }
        return ""; // Return an empty string if no leading numbers are found
    }

    private static boolean isInteger(String input) {
        try {
            Integer.parseInt(input);
            return true;
        } catch (NumberFormatException e) {
            return false;
        }
    }

    private static boolean isDouble(String input) {
        try {
            Double.parseDouble(input);
            return true;
        } catch (NumberFormatException e) {
            return false;
        }
    }

    private int convertDoubleToInteger(String input) {
        double _double = Double.parseDouble(input);
        if( _double > Integer.MAX_VALUE) {
            failed_state = true;
            number = Integer.MAX_VALUE;
        }else if(_double < Integer.MIN_VALUE){
            failed_state = true;
            number = Integer.MIN_VALUE;
        }
        return number;
    }
}
