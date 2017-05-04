package qzd919.recipist;

import android.content.ActivityNotFoundException;
import android.content.Intent;
import android.net.Uri;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.widget.AdapterView;
import android.widget.ArrayAdapter;
import android.widget.ListView;
import org.json.JSONArray;
import org.json.JSONException;
import org.json.JSONObject;
import java.util.ArrayList;

public class ResultPage extends AppCompatActivity {
    ListView listView_thingy;
    public ArrayList<String> reci_list = new ArrayList<String>();
    public ArrayList<String> name_list = new ArrayList<String>();
    //ImageView image = (ImageView)findViewById(R.id.list_image);
    // the image view didn't work properly on a list
 /*  public static Drawable LoadImageFromWebOperations(String url) {
        try {
            InputStream is = (InputStream) new URL(url).getContent();
            Drawable d = Drawable.createFromStream(is, "src name");
            return d;
        } catch (Exception e) {
            return null;
        }
    }*/
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_result_page);
        listView_thingy = (ListView)findViewById(R.id.listlol);

        Bundle b = getIntent().getExtras();
        String Array = b.getString("RawJSON");
        //Log.d("Array", Array);
        JSONArray obj = null;

        try {
            obj = new JSONArray(Array);
        } catch (JSONException e) {
            e.printStackTrace();
        }
        //if we were to store whole thing into a string use this
        //String n = obj.getString("");
        for (int i = 0; i < obj.length(); i++){
            try {
                JSONObject recp = new JSONObject(obj.getString(i));
                //Log.d("OMGGG", recp.getString("Name"));
                reci_list.add(recp.getString("url"));
                name_list.add(recp.getString("Name"));
                //url and name into array
                //new DownloadImageTask((ImageView) findViewById(R.id.list_image)).execute(MY_URL_STRING);
                //image too complicated to load into a list, not enough time to finish
                // this method also slows down UI thread by like 3 seconds
            } catch (JSONException e) {
                e.printStackTrace();
            }
            //Log.d("OMGGG", recp.getString("Name"));
            //Log.d("LOL", obj.getString(i));
        }

        final ArrayAdapter<String> urlAdapter = new ArrayAdapter<String>(ResultPage.this, android.R.layout.simple_expandable_list_item_1, name_list);
        listView_thingy.setAdapter(urlAdapter);
        listView_thingy.setOnItemClickListener(new AdapterView.OnItemClickListener() {
            @Override
            public void onItemClick(AdapterView<?> parent, View view, int position, long id) { //used chrome to open up url from json because app built in browser too slow
                String urlString=reci_list.get(position); //since position is give by clicklistener we can use this to find our stored url in the array
                Intent intent=new Intent(Intent.ACTION_VIEW, Uri.parse(urlString));
                intent.addFlags(Intent.FLAG_ACTIVITY_NEW_TASK);
                intent.setPackage("com.android.chrome");
                try {
                    startActivity(intent);
                } catch (ActivityNotFoundException ex) {
                    // Chrome browser presumably not installed so allow user to choose instead
                    intent.setPackage(null);
                    startActivity(intent);
                }
            }
        });

    }
    // this uses bitmap and asynctask, not sure how I would incorporate this into the for loop for parsing
    //causes crash when run outside async
    /*private class DownloadImageTask extends AsyncTask<String, Void, Bitmap> {
        ImageView bmImage;

        public DownloadImageTask(ImageView bmImage) {
            this.bmImage = bmImage;
        }

        protected Bitmap doInBackground(String... urls) {
            String urldisplay = urls[0];
            Bitmap mIcon11 = null;
            try {
                InputStream in = new java.net.URL(urldisplay).openStream();
                mIcon11 = BitmapFactory.decodeStream(in);
            } catch (Exception e) {
                Log.e("Error", e.getMessage());
                e.printStackTrace();
            }
            return mIcon11;
        }

        protected void onPostExecute(Bitmap result) {
            bmImage.setImageBitmap(result);
        }
    }*/
}

