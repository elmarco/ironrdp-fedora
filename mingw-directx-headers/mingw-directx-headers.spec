%global mingw_build_ucrt64 1
%{?mingw_package_header}

%global realname DirectX-Headers

Name:          mingw-directx-headers
Version:       1.616.0
Release:       1%{?dist}
Summary:       Official DirectX headers available under an open source license

License:       MIT
URL:           https://github.com/microsoft/%{realname}
Source0:       https://github.com/microsoft/%{realname}/archive/v%{version}/%{realname}-%{version}.tar.gz

BuildArch:     noarch

BuildRequires: meson
BuildRequires: ninja-build

BuildRequires: mingw32-filesystem
BuildRequires: mingw32-gcc-c++

BuildRequires: mingw64-filesystem
BuildRequires: mingw64-gcc-c++

BuildRequires: ucrt64-filesystem
BuildRequires: ucrt64-gcc-c++


%description
Official DirectX headers available under an open source license

%package -n mingw32-directx-headers
Summary:        Official DirectX headers available under an open source license

%description -n mingw32-directx-headers
Official DirectX headers available under an open source license

%package -n mingw64-directx-headers
Summary:        Official DirectX headers available under an open source license

%description -n mingw64-directx-headers
Official DirectX headers available under an open source license

%package -n ucrt64-directx-headers
Summary:        Official DirectX headers available under an open source license

%description -n ucrt64-directx-headers
Official DirectX headers available under an open source license


%prep
%autosetup -p1 -n %{realname}-%{version}


%build
%mingw_meson
%mingw_ninja


%install
%mingw_ninja_install


%files -n mingw32-directx-headers
%doc README.md SECURITY.md
%license LICENSE
%{mingw32_libdir}/pkgconfig/DirectX-Headers.pc
%{mingw32_libdir}/libDirectX-Guids.a
%{mingw32_libdir}/libd3dx12-format-properties.a
%{mingw32_includedir}/wsl/
%{mingw32_includedir}/dxguids/
%{mingw32_includedir}/directx/

%files -n mingw64-directx-headers
%doc README.md SECURITY.md
%license LICENSE
%{mingw64_libdir}/pkgconfig/DirectX-Headers.pc
%{mingw64_libdir}/libDirectX-Guids.a
%{mingw64_libdir}/libd3dx12-format-properties.a
%{mingw64_includedir}/wsl/
%{mingw64_includedir}/dxguids/
%{mingw64_includedir}/directx/

%files -n ucrt64-directx-headers
%doc README.md SECURITY.md
%license LICENSE
%{ucrt64_libdir}/pkgconfig/DirectX-Headers.pc
%{ucrt64_libdir}/libDirectX-Guids.a
%{ucrt64_libdir}/libd3dx12-format-properties.a
%{ucrt64_includedir}/wsl/
%{ucrt64_includedir}/dxguids/
%{ucrt64_includedir}/directx/


%changelog
* Wed Jul 30 2025 Marc-André Lureau <marcandre.lureau@redhat.com> - 1.616.0-1
- Initial packaging. Fixes: rhbz#XX

