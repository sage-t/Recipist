package potatoteam.yumyum;

import android.content.Intent;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;

public class DDscreen extends AppCompatActivity {
    public Button but2;
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
