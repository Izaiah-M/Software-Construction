import android.os.Bundle
import android.util.Log
import androidx.appcompat.app.AppCompatActivity

class LoginActivity : AppCompatActivity() {

    private val TAG = "LoginActivity"
    private val DEFAULT_USERNAME = "admin"
    private val DEFAULT_PASSWORD = "admin"

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_login)

        performLogin(DEFAULT_USERNAME, DEFAULT_PASSWORD)
    }

    private fun performLogin(username: String, password: String) {
        if (isCredentialsValid(username, password)) {
            Log.d(TAG, "Login successful")
            // Show welcome message or navigate to next screen
        } else {
            Log.d(TAG, "Invalid credentials")
            // Show error message
        }
    }

    private fun isCredentialsValid(username: String, password: String): Boolean {
        return username == DEFAULT_USERNAME && password == DEFAULT_PASSWORD
    }
}
