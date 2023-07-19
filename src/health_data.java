import java.io.OutputStream;
import java.net.HttpURLConnection;
import java.net.URL;
import org.json.JSONObject;

public class Main {
    public static void main(String[] args) throws Exception {
        // Create the JSON object for the patient data
        JSONObject patientData = new JSONObject();
        patientData.put("firstName", "John");
        patientData.put("lastName", "Doe");
        patientData.put("dateOfBirth", "1990-01-01");

        // Convert the JSON object to a string
        String jsonString = patientData.toString();

        // The URL of the API endpoint
        String urlString = "https://api.epiq.com/patients/12345";

        // Create a Url object from the urlString
        URL url = new URL(urlString);

        // Open a connection to the url
        HttpURLConnection conn = (HttpURLConnection) url.openConnection();

        // Set the request method to PUT
        conn.setRequestMethod("PUT");

        // Set the Accept and Content-Type headers to application/json
        conn.setRequestProperty("Accept", "application/json");
        conn.setRequestProperty("Content-Type", "application/json");

        // Set doOutput to true if you want to use URLConnection for output
        conn.setDoOutput(true);

        // Write the json data to the OutputStream of the HttpURLConnection
        try (OutputStream os = conn.getOutputStream()) {
            byte[] input = jsonString.getBytes("utf-8");
            os.write(input, 0, input.length);
        }

        // Get the response code
        int responseCode = conn.getResponseCode();
        System.out.println("Response Code : " + responseCode);

        // Finally disconnect the connection
        conn.disconnect();
    }
}
