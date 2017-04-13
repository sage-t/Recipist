import android.content.Intent;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.view.inputmethod.EditorInfo;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;
import android.widget.TextView.OnEditorActionListener;

public class DDscreen extends AppCompatActivity {
    public Button but2;
    EditText editText = (EditText) findViewById(R.id.search);
    editText.setOnEditorActionListener(new TextView.OnEditorActionListener(){
        @Override
        public boolean onEditorAction(TextView v, int actionId, KeyEvent){
            boolean handled = false;
            if (actionId == EditorInfo.IME_ACTION_SEND) {
                sendMessage();
                handled = true;
            }
            return handled;
        }
        });

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
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_ddscreen);
        init();
    }


}
