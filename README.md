## 💬 Gemini Flash Chat (Java Android)

This example demonstrates how to call the Gemini Flash API from an Android app using `HttpURLConnection`.

```java
public class MainActivity extends AppCompatActivity {
    EditText inputEditText;
    Button sendButton;
    TextView chatTextView;
    ScrollView scrollView;

    String geminiApiKey = "AIzaSyDqjx-mQ9vMbmyvMSqX4vz7RsIFFiIu9x0";

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        inputEditText = findViewById(R.id.inputEditText);
        sendButton = findViewById(R.id.sendButton);
        chatTextView = findViewById(R.id.chatTextView);
        scrollView = findViewById(R.id.scrollView);

        sendButton.setOnClickListener(v -> {
            String userMessage = inputEditText.getText().toString().trim();
            if (!userMessage.isEmpty()) {
                appendChat("You: " + userMessage);
                getGeminiFlashResponse(userMessage);
                inputEditText.setText("");
            }
        });
    }

    private void appendChat(String message) {
        runOnUiThread(() -> {
            chatTextView.append(message + "\n\n");
            scrollView.fullScroll(ScrollView.FOCUS_DOWN);
        });
    }

    private void getGeminiFlashResponse(String userInput) {
        new Thread(() -> {
            try {
                URL url = new URL("https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key=" + geminiApiKey);
                HttpURLConnection conn = (HttpURLConnection) url.openConnection();
                conn.setRequestMethod("POST");
                conn.setRequestProperty("Content-Type", "application/json");
                conn.setRequestProperty("X-goog-api-key", geminiApiKey);
                conn.setDoOutput(true);

                String jsonInput = "{ \"contents\": [ { \"parts\": [ { \"text\": \"" + userInput + "\" } ] } ] }";

                try (OutputStream os = conn.getOutputStream()) {
                    byte[] input = jsonInput.getBytes("utf-8");
                    os.write(input, 0, input.length);
                }

                InputStream inputStream = new BufferedInputStream(conn.getInputStream());
                BufferedReader reader = new BufferedReader(new InputStreamReader(inputStream));
                StringBuilder result = new StringBuilder();
                String line;
                while ((line = reader.readLine()) != null) {
                    result.append(line);
                }

                JSONObject responseJson = new JSONObject(result.toString());
                String reply = responseJson
                        .getJSONArray("candidates")
                        .getJSONObject(0)
                        .getJSONObject("content")
                        .getJSONArray("parts")
                        .getJSONObject(0)
                        .getString("text");

                appendChat("Gemini: " + reply);
            } catch (Exception e) {
                appendChat("Error: " + e.getMessage());
            }
        }).start();
    }
}
