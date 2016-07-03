package com.example.mirea.navdraw_api22.fragments;

import android.content.Context;
import android.net.Uri;
import android.os.Bundle;
import android.support.v4.app.Fragment;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.webkit.WebSettings;
import android.webkit.WebView;
import android.widget.ArrayAdapter;
import android.widget.Button;
import android.widget.Spinner;
import android.view.View.OnClickListener;

import com.example.mirea.navdraw_api22.R;

/**
 * A simple {@link Fragment} subclass.
 * Activities that contain this fragment must implement the
 * {@link MpFragment.OnFragmentInteractionListener} interface
 * to handle interaction events.
 * Use the {@link MpFragment#newInstance} factory method to
 * create an instance of this fragment.
 */

public class MpFragment extends android.app.Fragment {
    WebView MapPage;
    Spinner spinner;
    Button button;
    String[] data = {"Пластик", "Макулатура", "Батарейки", "Стекло", "Металл", "Все"};
    // TODO: Rename parameter arguments, choose names that match
    // the fragment initialization parameters, e.g. ARG_ITEM_NUMBER
    private static final String ARG_PARAM1 = "param1";
    private static final String ARG_PARAM2 = "param2";

    // TODO: Rename and change types of parameters
    private String mParam1;
    private String mParam2;

    private OnFragmentInteractionListener mListener;

    public MpFragment() {
        // Required empty public constructor
    }

    /**
     * Use this factory method to create a new instance of
     * this fragment using the provided parameters.
     *
     * @param param1 Parameter 1.
     * @param param2 Parameter 2.
     * @return A new instance of fragment MpFragment.
     */
    // TODO: Rename and change types and number of parameters
    public static MpFragment newInstance(String param1, String param2) {
        MpFragment fragment = new MpFragment();
        Bundle args = new Bundle();
        args.putString(ARG_PARAM1, param1);
        args.putString(ARG_PARAM2, param2);
        fragment.setArguments(args);
        return fragment;
    }

    @Override
    public void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        if (getArguments() != null) {
            mParam1 = getArguments().getString(ARG_PARAM1);
            mParam2 = getArguments().getString(ARG_PARAM2);
        }
    }

    @Override
    public View onCreateView(LayoutInflater inflater, ViewGroup container,
                             Bundle savedInstanceState) {
        // Inflate the layout for this fragment
        View view =  inflater.inflate(R.layout.fragment_mp, container, false);
        //return inflater.inflate(R.layout.fragment_mp, container, false);
        MapPage = (WebView)view.findViewById(R.id.webView);
        WebSettings webSettings = MapPage.getSettings();
        webSettings.setJavaScriptEnabled(true);
        webSettings.setGeolocationEnabled(true);
        MapPage.loadUrl("http://re.alexey109.ru");
        //создание выпадающего списка
        ArrayAdapter<CharSequence> adapter = ArrayAdapter.createFromResource(getActivity(), R.array.recTypesArray, android.R.layout.simple_spinner_item);
        adapter.setDropDownViewResource(android.R.layout.simple_spinner_dropdown_item);
        spinner = (Spinner) view.findViewById(R.id.spinner);
        adapter.setDropDownViewResource(android.R.layout.simple_spinner_dropdown_item);
        spinner.setAdapter(adapter);
        spinner.setPrompt("Виды отходов");
        button = (Button) view.findViewById(R.id.button3);
        button.setOnClickListener(ButtonShowItem);
        spinner.setSelection(5);
        return view;
    }
    OnClickListener ButtonShowItem = new OnClickListener() {
        @Override
        public void onClick(View view) {
            if (spinner.getSelectedItemPosition()==0){
                MapPage.loadUrl("http://46.188.68.120/item1.html");
            } else if (spinner.getSelectedItemPosition()==1){
                MapPage.loadUrl("http://46.188.68.120/item2.html");
            } else if (spinner.getSelectedItemPosition()==2){
                MapPage.loadUrl("http://46.188.68.120/item3.html");
            } else if (spinner.getSelectedItemPosition()==3){
                MapPage.loadUrl("http://46.188.68.120/item4.html");
            } else if (spinner.getSelectedItemPosition()==4){
                MapPage.loadUrl("http://46.188.68.120/item5.html");
            } else if (spinner.getSelectedItemPosition()==5){
                MapPage.loadUrl("http://re.alexey109.ru");
            }

        }
    };





    // TODO: Rename method, update argument and hook method into UI event
    public void onButtonPressed(Uri uri) {
        if (mListener != null) {
            mListener.onFragmentInteraction(uri);
        }
    }

    @Override
    public void onAttach(Context context) {
        super.onAttach(context);
        if (context instanceof OnFragmentInteractionListener) {
            mListener = (OnFragmentInteractionListener) context;
        } else {
            throw new RuntimeException(context.toString()
                    + " must implement OnFragmentInteractionListener");
        }
    }

    @Override
    public void onDetach() {
        super.onDetach();
        mListener = null;
    }

    /**
     * This interface must be implemented by activities that contain this
     * fragment to allow an interaction in this fragment to be communicated
     * to the activity and potentially other fragments contained in that
     * activity.
     * <p/>
     * See the Android Training lesson <a href=
     * "http://developer.android.com/training/basics/fragments/communicating.html"
     * >Communicating with Other Fragments</a> for more information.
     */
    public interface OnFragmentInteractionListener {
        // TODO: Update argument type and name
        void onFragmentInteraction(Uri uri);
    }
}
