package italyinformatica.italyinformatica_android.ui.login;

import italyinformatica.italyinformatica_android.ui.base.BaseContract;

public interface LoginContract {

    interface View extends BaseContract.View {

        void openMainActivity();

        void onConfirmedLogin(String message);

        void onConfirmedLoginVerification(String message);

        void onError();

        void onLoginError(String error);

        void onLoginVerificationError(String error);

        void showLoading();

    }

    interface Presenter<V extends LoginContract.View> extends BaseContract.Presenter<V> {

        void onLoginClick(String user, String pass);

    }

}
