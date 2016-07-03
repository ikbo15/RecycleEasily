package com.example.mirea.navdraw_api22;

import android.os.Bundle;
import android.support.v7.app.AppCompatActivity;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.RadioButton;
import android.widget.ToggleButton;


public class Settings extends AppCompatActivity {


    RadioButton radioButton;
    RadioButton radioButton2;
    RadioButton radioButton3;
    RadioButton radioButton4;
    RadioButton radioButton5;
    ToggleButton tgButton;


    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_settings);
        Button button1 = (Button) findViewById(R.id.button2);
        radioButton = (RadioButton)findViewById(R.id.radioButton);
        radioButton2 = (RadioButton)findViewById(R.id.radioButton2);
        radioButton3 = (RadioButton)findViewById(R.id.radioButton3);
        radioButton4 = (RadioButton)findViewById(R.id.radioButton4);
        radioButton5 = (RadioButton) findViewById(R.id.radioButton5);
        tgButton = (ToggleButton) findViewById(R.id.toggleButton);



    }
    public void clickButtonColor (View view) {

        EditText editText = (EditText)findViewById(R.id.editText2);

        if (radioButton.isChecked()){
            editText.setText(R.string.nickname);
        } else if (radioButton2.isChecked()) {
            editText.setText(R.string.mail);
        }else if (radioButton3.isChecked()) {
            editText.setText(R.string.mail);
        }else if (radioButton4.isChecked()){
            editText.setText(R.string.account_name);
        }else if (radioButton5.isChecked()){
            editText.setText(R.string.app_name);
        }

    }


}
