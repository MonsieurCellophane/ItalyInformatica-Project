package italyinformatica.italyinformatica_android.ui.base;

public interface BaseContract {

    interface View {

        boolean isNetworkConnected();

    }

    interface Presenter<V extends View> {

        void onAttach(V view);

        void onDetach();

    }

}
