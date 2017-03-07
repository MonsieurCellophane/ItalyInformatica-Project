package italyinformatica.italyinformatica_android.ui.base;

import android.os.Bundle;
import android.support.annotation.Nullable;
import android.support.v7.app.AppCompatActivity;

import butterknife.Unbinder;
import italyinformatica.italyinformatica_android.IIPApp;
import italyinformatica.italyinformatica_android.di.component.ActivityComponent;
import italyinformatica.italyinformatica_android.di.component.DaggerActivityComponent;
import italyinformatica.italyinformatica_android.di.module.ActivityModule;
import italyinformatica.italyinformatica_android.utils.NetworkUtils;

public class BaseActivity extends AppCompatActivity implements BaseContract.View {

    private ActivityComponent mActivityComponent;

    private Unbinder mUnBinder;

    @Override
    protected void onCreate(@Nullable Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);

        mActivityComponent = DaggerActivityComponent.builder()
                .activityModule(new ActivityModule(this))
                .appComponent(((IIPApp) getApplication()).getAppComponent())
                .build();

    }

    public ActivityComponent getActivityComponent() {
        return mActivityComponent;
    }

    public void setUnBinder(Unbinder unBinder) {
        mUnBinder = unBinder;
    }

    @Override
    protected void onDestroy() {
        if (mUnBinder != null)
            mUnBinder.unbind();
        super.onDestroy();
    }

    @Override
    public boolean isNetworkConnected() {
        return NetworkUtils.isNetworkConnected(getApplicationContext());
    }
}
