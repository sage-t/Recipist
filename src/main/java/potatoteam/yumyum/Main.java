package qzd919.recipist;

import android.os.AsyncTask;
import android.os.Bundle;
import android.support.v7.app.AppCompatActivity;
import android.util.Log;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;

//import org.json.JSONArray;
//import org.json.JSONException;
//import org.json.JSONObject;
//import org.json.JSONTokener;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.net.HttpURLConnection;
import java.net.URL;

//code structure from http://www.androidauthority.com/use-remote-web-api-within-android-app-617869/
public class MainActivity extends AppCompatActivity { //search for ingredients for now.

    EditText ingredientText;
    TextView responseView;

    String ingredient;
    //ProgressBar progressBar;
    //static final String API_KEY = "USE_YOUR_OWN_API_KEY";
    static final String API_URL = "http://recipist-csci3308.herokuapp.com/search?ingrds=";
    // noticed the api only takes in lower-case words
    //multi-search only matches 1 ingredient

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        responseView = (TextView) findViewById(R.id.responseView);
        ingredientText = (EditText) findViewById(R.id.ingredientText);

    // got it from: http://stackoverflow.com/questions/32568340/android-studio-error-method-gettext-must-be-called-from-the-ui-thread-curre
        Button queryButton = (Button) findViewById(R.id.queryButton);
        queryButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                ingredient = ingredientText.getText().toString();

                new RetrieveFeedTask().execute();
            }
        });
    }

    class RetrieveFeedTask extends AsyncTask<Void, Void, String> {

       // private Exception exception;

        protected void onPreExecute() {

            responseView.setText("");
        }

        protected String doInBackground(Void... urls) {
            try {
                URL url = new URL(API_URL + ingredient);
                HttpURLConnection urlConnection = (HttpURLConnection) url.openConnection();
                try {
                    BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(urlConnection.getInputStream()));
                    StringBuilder stringBuilder = new StringBuilder();
                    String line;
                    while ((line = bufferedReader.readLine()) != null) {
                        stringBuilder.append(line).append("\n");
                    }
                    bufferedReader.close();
                    return stringBuilder.toString();
                }
                finally{
                    urlConnection.disconnect();
                }
            }
            catch(Exception e) {
                Log.e("ERROR", e.getMessage(), e);
                return null;
            }
        }
        // some error handling
        protected void onPostExecute(String response) {
            if(response == null) {
                response = "THERE WAS AN ERROR";
            }
            Log.i("INFO", response);
            responseView.setText(response);

        }
    }
}
