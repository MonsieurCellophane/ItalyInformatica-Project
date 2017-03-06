package italyinformatica.italyinformatica_android.ui.main;

import android.content.Context;
import android.content.Intent;
import android.os.Bundle;
import android.widget.TextView;

import javax.inject.Inject;

import butterknife.BindView;
import butterknife.ButterKnife;
import butterknife.OnClick;
import italyinformatica.italyinformatica_android.R;
import italyinformatica.italyinformatica_android.ui.base.BaseActivity;
import italyinformatica.italyinformatica_android.ui.login.LoginActivity;

public class MainActivity extends BaseActivity implements MainContract.View {

    @Inject
    MainContract.Presenter<MainContract.View> mPresenter;

    @BindView(R.id.text)
    TextView mTextView;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.main_activity);

        getActivityComponent().inject(this);

        setUnBinder(ButterKnife.bind(this));

        mPresenter.onAttach(this);

        mPresenter.checkIfLoggedin();

        openLoginActivity();
    }

    public static Intent getStartIntent(Context context) {
        Intent intent = new Intent(context, MainActivity.class);
        return intent;
    }

    @OnClick(R.id.text)
    void onTextClick() {
        mPresenter.onTextClick();
    }

    @Override
    public void openLoginActivity() {
        Intent intent = LoginActivity.getStartIntent(MainActivity.this);
        startActivity(intent);
        finish();
    }

    @Override
    public void changeText(String s) {
        mTextView.setText(s);
    }
}
