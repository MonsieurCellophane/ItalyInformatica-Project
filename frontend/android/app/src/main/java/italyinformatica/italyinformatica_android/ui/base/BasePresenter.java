package italyinformatica.italyinformatica_android.ui.base;

import javax.inject.Inject;

import io.reactivex.disposables.CompositeDisposable;
import italyinformatica.italyinformatica_android.data.DataManager;

public class BasePresenter<V extends BaseContract.View> implements BaseContract.Presenter<V> {

    private final CompositeDisposable mCompositeDisposable;
    private final DataManager mDatamanager;

    private V view;

    @Inject
    public BasePresenter(CompositeDisposable compositeDisposable, DataManager dataManager) {
        mCompositeDisposable = compositeDisposable;
        mDatamanager = dataManager;
    }

    @Override
    public void onAttach(V view) {
        this.view = view;
    }

    @Override
    public void onDetach() {
        mCompositeDisposable.dispose();
        view = null;
    }

    public V getView() {
        return view;
    }

    public CompositeDisposable getCompositeDisposable() {
        return mCompositeDisposable;
    }

    public DataManager getDataManager() {
        return mDatamanager;
    }

}
