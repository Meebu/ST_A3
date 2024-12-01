import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

class LoginTest {

    private final Login login = new Login();

    @Test
    public void testInValidLogin() {
        System.out.println("Running testInValidLogin...");
        assertFalse(login.validate("umairlatif@example.com", "password456"), "InValid login should return false.");
    }

    @Test
    public void testInvalidEmail() {
        System.out.println("Running testInvalidEmail...");
        assertFalse(login.validate("invalid@example.com", "password123"), "Invalid email should return false.");
    }

    @Test
    public void testIncorrectPassword() {
        System.out.println("Running testIncorrectPassword...");
        assertFalse(login.validate("johndoe@example.com", "wrong password"), "Incorrect password should return false.");
    }

    @Test
    public void testEmptyFields() {
        System.out.println("Running testEmptyFields...");
        assertFalse(login.validate("", ""), "Empty fields should return false.");
    }

    @Test
    public void testSQLInjection() {
        // Modified SQL injection to simulate a malicious attack
        System.out.println("Running testSQLInjection...");
        
        // Simulating a SQL injection attack that could potentially bypass the login system
        String sqlInjectionAttempt = "' OR 1=1 --";
        
        // This will simulate a login attempt with an SQL injection string
        assertFalse(login.validate(sqlInjectionAttempt, "password123"), "SQL injection attempt should return false.");
    }
}
