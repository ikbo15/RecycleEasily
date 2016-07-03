package com.example.mirea.navdraw_api22;

import android.app.FragmentTransaction;
import android.content.Intent;
import android.os.Bundle;
import android.support.design.widget.FloatingActionButton;
import android.support.design.widget.NavigationView;
import android.support.design.widget.Snackbar;
import android.support.v4.view.GravityCompat;
import android.support.v4.widget.DrawerLayout;
import android.support.v7.app.ActionBarDrawerToggle;
import android.support.v7.app.AppCompatActivity;
import android.support.v7.widget.Toolbar;
import android.view.Menu;
import android.view.MenuItem;
import android.view.View;
import android.webkit.WebView;
import android.widget.Spinner;

import com.example.mirea.navdraw_api22.fragments.AccountFragment;
import com.example.mirea.navdraw_api22.fragments.CatFragment;
import com.example.mirea.navdraw_api22.fragments.HelpFragment;
import com.example.mirea.navdraw_api22.fragments.MainFragment;
import com.example.mirea.navdraw_api22.fragments.MpFragment;
import com.example.mirea.navdraw_api22.fragments.NewsFragment;
import com.example.mirea.navdraw_api22.fragments.SearchFragment;

public class MainActivity extends AppCompatActivity
        implements NavigationView.OnNavigationItemSelectedListener {

    AccountFragment faccount;
    CatFragment fcat;
    HelpFragment fhelp;
    MainFragment fmain;
    MpFragment fmap;
    NewsFragment fnews;
    SearchFragment fsearch;
    WebView MapPage;
    Spinner spinner;


    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        Toolbar toolbar = (Toolbar) findViewById(R.id.toolbar);
        setSupportActionBar(toolbar);

        FloatingActionButton fab = (FloatingActionButton) findViewById(R.id.fab);
        fab.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                Snackbar.make(view, "Replace with your own action", Snackbar.LENGTH_LONG)
                        .setAction("Action", null).show();
            }
        });

        DrawerLayout drawer = (DrawerLayout) findViewById(R.id.drawer_layout);
        ActionBarDrawerToggle toggle = new ActionBarDrawerToggle(
                this, drawer, toolbar, R.string.navigation_drawer_open, R.string.navigation_drawer_close);
        drawer.setDrawerListener(toggle);
        toggle.syncState();

        NavigationView navigationView = (NavigationView) findViewById(R.id.nav_view);
        navigationView.setNavigationItemSelectedListener(this);
        faccount = new AccountFragment();
        fcat = new CatFragment();
        fhelp = new HelpFragment();
        fmain = new MainFragment();
        fmap = new MpFragment();
        fnews = new NewsFragment();
        fsearch = new SearchFragment();

    }

    @Override
    public void onBackPressed() {
        DrawerLayout drawer = (DrawerLayout) findViewById(R.id.drawer_layout);
        if (drawer.isDrawerOpen(GravityCompat.START)) {
            drawer.closeDrawer(GravityCompat.START);
        } else {
            super.onBackPressed();
        }
    }

    @Override
    public boolean onCreateOptionsMenu(Menu menu) {
        // Inflate the menu; this adds items to the action bar if it is present.
        getMenuInflater().inflate(R.menu.main, menu);
        return true;
    }

    @Override
    public boolean onOptionsItemSelected(MenuItem item) {
        // Handle action bar item clicks here. The action bar will
        // automatically handle clicks on the Home/Up button, so long
        // as you specify a parent activity in AndroidManifest.xml.
        int id = item.getItemId();

        //noinspection SimplifiableIfStatement
        if (id == R.id.action_settings) {
            Intent settings = new Intent(this, Settings.class);
            startActivity(settings);
        }

        return super.onOptionsItemSelected(item);
    }

    @SuppressWarnings("StatementWithEmptyBody")
    @Override
    public boolean onNavigationItemSelected(MenuItem item) {
        // Handle navigation view item clicks here.
        int id = item.getItemId();
        FragmentTransaction ftrans = getFragmentManager().beginTransaction();

        if (id == R.id.nav_main) {
            ftrans.replace(R.id.container, fmain);
            // Handle the camera action
        } else if (id == R.id.nav_map) {
            ftrans.replace(R.id.container, fmap);
        } else if (id == R.id.nav_cat) {
            ftrans.replace(R.id.container, fcat);
        } else if (id == R.id.nav_search) {
            ftrans.replace(R.id.container, fsearch);
        } else if (id == R.id.nav_news) {
            ftrans.replace(R.id.container, fnews);
        } else if (id == R.id.nav_account) {
            Intent intent = new Intent(this, Main2Activity.class);
            startActivity(intent);
        } else if (id == R.id.nav_help) {
            Intent helpWindow = new Intent(this, Help_Activity.class);
            startActivity(helpWindow);

        } else ftrans.replace(R.id.container, fmain);
            ftrans.commit();

        DrawerLayout drawer = (DrawerLayout) findViewById(R.id.drawer_layout);
        drawer.closeDrawer(GravityCompat.START);
        return true;
    }

}
