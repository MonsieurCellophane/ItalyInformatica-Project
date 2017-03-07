package italyinformatica.italyinformatica_android.ui.login;

import android.content.Context;
import android.content.Intent;
import android.os.Bundle;
import android.support.annotation.Nullable;
import android.widget.EditText;
import android.widget.Toast;

import javax.inject.Inject;

import butterknife.BindView;
import butterknife.ButterKnife;
import butterknife.OnClick;
import italyinformatica.italyinformatica_android.R;
import italyinformatica.italyinformatica_android.ui.base.BaseActivity;
import italyinformatica.italyinformatica_android.ui.main.MainActivity;

public class LoginActivity extends BaseActivity implements LoginContract.View {

    @Inject
    LoginContract.Presenter<LoginContract.View> mPresenter;

    @BindView(R.id.input_user)
    EditText mInputUser;

    @BindView(R.id.input_password)
    EditText mInputPassword;

    @Override
    protected void onCreate(@Nullable Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.login_activity);

        getActivityComponent().inject(this);

        setUnBinder(ButterKnife.bind(this));

        mPresenter.onAttach(this);
    }

    @OnClick(R.id.btn_login)
    void onLoginButtonClick() {
        mPresenter.onLoginClick(mInputUser.getText().toString(), mInputPassword.getText().toString());
    }

    public static Intent getStartIntent(Context context) {
        Intent intent = new Intent(context, LoginActivity.class);
        return intent;
    }

    @Override
    public void openMainActivity() {
        Intent intent = MainActivity.getStartIntent(LoginActivity.this);
        startActivity(intent);
        finish();
    }

    @Override
    public void onConfirmedLogin(String message) {
        Toast.makeText(getApplicationContext(), "Token: " + message, Toast.LENGTH_LONG).show();
    }

    @Override
    public void onConfirmedLoginVerification(String message) {
        Toast.makeText(getApplicationContext(), "Token verified: " + message, Toast.LENGTH_LONG).show();
    }

    @Override
    public void onLoginError(String error) {
        Toast.makeText(getApplicationContext(), error, Toast.LENGTH_LONG).show();
    }

    @Override
    public void onLoginVerificationError(String error) {
        Toast.makeText(getApplicationContext(), error, Toast.LENGTH_LONG).show();
    }

    @Override
    public void onError() {

    }

    @Override
    public void showLoading() {

    }

}
