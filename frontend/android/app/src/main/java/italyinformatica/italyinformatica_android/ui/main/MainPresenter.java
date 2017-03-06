package italyinformatica.italyinformatica_android.ui.main;

import javax.inject.Inject;

import io.reactivex.disposables.CompositeDisposable;
import italyinformatica.italyinformatica_android.data.DataManager;
import italyinformatica.italyinformatica_android.ui.base.BasePresenter;

public class MainPresenter<V extends MainContract.View> extends BasePresenter<V> implements MainContract.Presenter<V> {

    @Inject
    public MainPresenter(CompositeDisposable compositeDisposable, DataManager dataManager) {
        super(compositeDisposable, dataManager);
    }

    @Override
    public void onTextClick() {
        getView().changeText("bella");
    }

    @Override
    public void checkIfLoggedin() {

    }
}
