package qzd919.recipist;

import android.content.ActivityNotFoundException;
import android.content.Intent;
import android.graphics.Bitmap;
import android.graphics.BitmapFactory;
import android.graphics.drawable.Drawable;
import android.media.Image;
import android.net.Uri;
import android.os.AsyncTask;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.widget.AdapterView;
import android.widget.ArrayAdapter;
import android.widget.ImageView;
import android.widget.ListView;

import org.json.JSONArray;
import org.json.JSONException;
import org.json.JSONObject;

import java.io.InputStream;
import java.net.URL;
import java.util.ArrayList;

public class ResultPage extends AppCompatActivity {
    ListView listView_thingy;
    public ArrayList<String> reci_list = new ArrayList<String>();
    public ArrayList<String> name_list = new ArrayList<String>();
    //ImageView image = (ImageView)findViewById(R.id.list_image);
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
        Log.d("SUCK<MYEW", Array);
        JSONArray obj = null;




        try {
            obj = new JSONArray(Array);
        } catch (JSONException e) {
            e.printStackTrace();
        }
        //String n = obj.getString("");
        for (int i = 0; i < obj.length(); i++){
            try {
                JSONObject recp = new JSONObject(obj.getString(i));
                Log.d("OMGGG", recp.getString("Name"));
                reci_list.add(recp.getString("url"));
                name_list.add(recp.getString("Name"));
                //new DownloadImageTask((ImageView) findViewById(R.id.list_image)).execute(MY_URL_STRING);
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
            public void onItemClick(AdapterView<?> parent, View view, int position, long id) {
                String urlString=reci_list.get(position);
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

