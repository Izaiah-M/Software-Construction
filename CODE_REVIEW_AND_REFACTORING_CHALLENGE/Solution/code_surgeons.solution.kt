import android.os.Bundle
import android.util.Log
import androidx.appcompat.app.AppCompatActivity

class LoginActivity : AppCompatActivity() {

    // Tag for logging
    private val TAG = "LoginActivity"

    // Default username and password
    private val DEFAULT_USERNAME = "admin"
    private val DEFAULT_PASSWORD = "admin"

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_login)

        // Perform login with default credentials
        performLogin(DEFAULT_USERNAME, DEFAULT_PASSWORD)
    }

    // Method to perform login
    private fun performLogin(username: String, password: String) {
        // Check if credentials are valid
        if (isCredentialsValid(username, password)) {
            // Log successful login
            Log.d(TAG, "Login successful")
            // Show welcome message or navigate to next screen
        } else {
            // Log invalid credentials
            Log.d(TAG, "Invalid credentials")
            // Show error message
        }
    }

    // Method to check if credentials are valid
    private fun isCredentialsValid(username: String, password: String): Boolean {
        return username == DEFAULT_USERNAME && password == DEFAULT_PASSWORD
    }

    // Other methods and classes...
}
