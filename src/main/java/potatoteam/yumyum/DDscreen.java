package potatoteam.yumyum;

import android.content.Intent;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.KeyEvent;
import android.view.View;
import android.view.inputmethod.EditorInfo;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;
import android.widget.TextView.OnEditorActionListener;
import android.widget.Toast;

public class DDscreen extends AppCompatActivity implements OnEditorActionListener {
    public Button but2;
    EditText editText = (EditText) findViewById(R.id.search);

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        editText.setOnEditorActionListener(this);
        setContentView(R.layout.activity_ddscreen);
        init();
    }

    public void init (){
        but2 = (Button)findViewById(R.id.but2);
        but2.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Intent ASS = new Intent(DDscreen.this, Recipes.class);
                startActivity(ASS);
            }
        });
    }


    public boolean onEditorAction(TextView v, int actionId, KeyEvent event){
        boolean handled = false;
        if (actionId == EditorInfo.IME_ACTION_DONE) {
            Toast.makeText(this,"HOFEFDJBKFDSSBKJFDS", Toast.LENGTH_LONG);
            handled = true;
        }
        return handled;
    }


}
