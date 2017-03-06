package italyinformatica.italyinformatica_android.ui.main;

import italyinformatica.italyinformatica_android.di.PerActivity;
import italyinformatica.italyinformatica_android.ui.base.BaseContract;

public interface MainContract {

    interface View extends BaseContract.View {

        void openLoginActivity();

        void changeText(String s);

    }

    @PerActivity
    interface Presenter<V extends MainContract.View> extends BaseContract.Presenter<V> {

        void onTextClick();

        void checkIfLoggedin();

    }

}
