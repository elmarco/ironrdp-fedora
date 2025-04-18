# Generated by rust2rpm 27
%bcond check 1
%global debug_package %{nil}

%global crate qapi-codegen

Name:           rust-qapi-codegen
Version:        0.11.3
Release:        %autorelease
Summary:        QEMU QAPI codegen helper

License:        MIT
URL:            https://crates.io/crates/qapi-codegen
Source:         %{crates_source}
# https://github.com/arcnmx/qapi-rs/pull/26
Source1:        https://raw.githubusercontent.com/arcnmx/qapi-rs/refs/heads/main/COPYING

BuildRequires:  cargo-rpm-macros >= 24

%global _description %{expand:
QEMU QAPI codegen helper.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages which
use the "%{crate}" crate.

%files          devel
%license %{crate_instdir}/COPYING
%doc %{crate_instdir}/README.md
%{crate_instdir}/

%package     -n %{name}+default-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+default-devel %{_description}

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%files       -n %{name}+default-devel
%ghost %{crate_instdir}/Cargo.toml

%prep
%autosetup -n %{crate}-%{version} -p1
cp -pav %{SOURCE1} .
%cargo_prep

%generate_buildrequires
%cargo_generate_buildrequires

%build
%cargo_build

%install
%cargo_install

%if %{with check}
%check
%cargo_test
%endif

%changelog
%autochangelog
