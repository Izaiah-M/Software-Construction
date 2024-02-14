import android.os.Bundle
import androidx.appcompat.app.AppCompatActivity

class LoginActivity : AppCompatActivity() {

    private val DEFAULT_USERNAME = "admin"
    private val DEFAULT_PASSWORD = "admin"

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_login)

        performLogin(DEFAULT_USERNAME, DEFAULT_PASSWORD)
    }

    private fun performLogin(username: String, password: String) {
        if (isCredentialsValid(username, password)) {
            // Login successful
        } else {
            // Invalid credentials
        }
    }

    private fun isCredentialsValid(username: String, password: String): Boolean {
        return username == DEFAULT_USERNAME && password == DEFAULT_PASSWORD
    }

}
