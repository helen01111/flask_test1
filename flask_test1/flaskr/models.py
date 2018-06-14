# coding: utf-8
from sqlalchemy import ARRAY, Boolean, Column, Date, DateTime, Index, Integer, Numeric, String, Table, Text
from sqlalchemy.schema import FetchedValue
from sqlalchemy.dialects.postgresql.base import OID
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


class AccTransErrCv(db.Model):
    __tablename__ = 'acc_trans_err_cvs'

    dmd_month = db.Column(db.String(6), primary_key=True, nullable=False)
    dmdto_id = db.Column(db.String(12), primary_key=True, nullable=False)
    create_date = db.Column(db.DateTime, nullable=False)
    renew_date = db.Column(db.DateTime, nullable=False)
    operate_cd = db.Column(db.String(128), nullable=False)
    trans_kind = db.Column(db.String(1), nullable=False)
    result_cd = db.Column(db.String(1), nullable=False)
    dmd_no = db.Column(db.String(13))
    demand_kbn = db.Column(db.String(2))
    dmd_valid_date = db.Column(db.DateTime)
    cvs_next_month_flag = db.Column(db.String(1), nullable=False)
    dmd_no_next_month = db.Column(db.String(13))
    chg_dmd_kbn_flag = db.Column(db.String(1), nullable=False)
    reserved_dmd_kbn_flag = db.Column(db.String(1), nullable=False)


class AccaDat(db.Model):
    __tablename__ = 'acca_dat'

    ws_common_id = db.Column(db.String(20), primary_key=True)
    ws_common_renbn = db.Column(db.String(2))
    contract_no = db.Column(db.String(12), nullable=False, index=True)
    isp_order_no = db.Column(db.String(20), index=True)
    apply_date = db.Column(db.DateTime, nullable=False)
    send_plan_date = db.Column(db.DateTime)
    send_date = db.Column(db.DateTime)
    apply_kind = db.Column(db.String(4))
    prog_status = db.Column(db.String(2))
    apply_brand = db.Column(db.String(2))
    order_cd = db.Column(db.String(3))
    order_no = db.Column(db.String(10))
    acca_no = db.Column(db.String(60))
    service_id = db.Column(db.String(10))
    gc_name = db.Column(db.String(200))
    line_name = db.Column(db.String(60))
    install_cd = db.Column(db.String(1))
    zip = db.Column(db.String(8))
    todohuken = db.Column(db.String(8))
    gun = db.Column(db.String(30))
    ku = db.Column(db.String(30))
    area = db.Column(db.String(30))
    banchi = db.Column(db.String(50))
    build_name = db.Column(db.String(120))
    telno = db.Column(db.String(13))
    toi_telno = db.Column(db.String(13))
    email = db.Column(db.String(90))
    service_kind = db.Column(db.String(1))
    isdn_type = db.Column(db.String(1))
    user_cd = db.Column(db.String(1))
    isdn_change = db.Column(db.String(1))
    cpe_provider = db.Column(db.String(1))
    cpe_installer = db.Column(db.String(1))
    cpe_kind = db.Column(db.String(3))
    nw_kind = db.Column(db.String(1))
    ntt_result = db.Column(db.String(1))
    ntt_ng1 = db.Column(db.String(2))
    ntt_ng2 = db.Column(db.String(2))
    ntt_notes = db.Column(db.String(1800))
    reason_cd = db.Column(db.String(2))
    result_date = db.Column(db.DateTime)
    change_date = db.Column(db.DateTime)
    ntt_work_date = db.Column(db.DateTime)
    complete_date = db.Column(db.DateTime)
    notes = db.Column(db.String(600))
    entry_cd = db.Column(db.String(10))
    campaign_cd = db.Column(db.String(15))
    agency_cd = db.Column(db.String(12))
    create_date = db.Column(db.DateTime, nullable=False)
    renew_date = db.Column(db.DateTime, nullable=False)
    operate_cd = db.Column(db.String(128), nullable=False)
    c_flag = db.Column(db.String(1))
    remark = db.Column(db.String(80))
    owner_zip = db.Column(db.String(8))
    owner_todohuken = db.Column(db.String(8))
    owner_gun = db.Column(db.String(30))
    owner_ku = db.Column(db.String(30))
    owner_area = db.Column(db.String(30))
    owner_banchi = db.Column(db.String(50))
    owner_build_name = db.Column(db.String(120))
    cert_telno = db.Column(db.String(13))


class Adjust(db.Model):
    __tablename__ = 'adjust'

    bill_month = db.Column(db.Date, primary_key=True, nullable=False)
    adjust_renban = db.Column(db.Numeric(9, 0), primary_key=True, nullable=False)
    dmdto_id = db.Column(db.String(12), nullable=False)
    contbase_no = db.Column(db.String(10))
    contract_no = db.Column(db.String(12))
    opt_contract_no = db.Column(db.Numeric(10, 0))
    customer_id = db.Column(db.String(8))
    reason = db.Column(db.String(64))
    cost = db.Column(db.Numeric(6, 0), nullable=False)
    taxfree_kbn = db.Column(db.String(1), nullable=False)
    adjust_kind = db.Column(db.String(1), nullable=False)
    adjust_cd = db.Column(db.String(9))
    create_date = db.Column(db.DateTime, nullable=False)
    renew_date = db.Column(db.DateTime, nullable=False)
    operate_cd = db.Column(db.String(128), nullable=False)
    c_flag = db.Column(db.String(1))
    creditor_cd = db.Column(db.String(1), nullable=False, server_default=db.FetchedValue())
    creditor_subcd = db.Column(db.String(3))
    sales_dmd_kbn = db.Column(db.String(1))
    stat_kbn = db.Column(db.Numeric(1, 0))
    tax_percent = db.Column(db.Numeric(4, 1))


t_alipay_dat = db.Table(
    'alipay_dat',
    db.Column('contract_no', db.String(12), index=True),
    db.Column('opt_contract_no', db.Numeric(10, 0), index=True),
    db.Column('jpayment_trade_no', db.String(64), nullable=False)
)


class Announce(db.Model):
    __tablename__ = 'announce'

    customer_id = db.Column(db.String(8), primary_key=True)
    type = db.Column(db.String(1), nullable=False)
    create_date = db.Column(db.DateTime, nullable=False)
    renew_date = db.Column(db.DateTime, nullable=False)
    c_flag = db.Column(db.String(1))
    operate_cd = db.Column(db.String(128), nullable=False)


class AppliResMst(db.Model):
    __tablename__ = 'appli_res_mst'

    res_cd = db.Column(db.String(4), primary_key=True)
    address_kind = db.Column(db.String(16), nullable=False)
    res_kind = db.Column(db.String(128), nullable=False)
    append_res1 = db.Column(db.String(4))
    append_res2 = db.Column(db.String(4))
    enc_num = db.Column(db.Numeric(2, 0))


class AppliSendDat(db.Model):
    __tablename__ = 'appli_send_dat'

    send_no = db.Column(db.String(20), primary_key=True)
    renew_date = db.Column(db.DateTime, nullable=False)
    create_date = db.Column(db.DateTime, nullable=False)
    operate_cd = db.Column(db.String(128), nullable=False)
    c_flag = db.Column(db.String(1))
    remark = db.Column(db.String(80))
    apply_date = db.Column(db.DateTime, nullable=False)
    customer_id = db.Column(db.String(8), index=True)
    prog_status = db.Column(db.String(2), nullable=False)
    direct_operate_cd = db.Column(db.String(128), nullable=False)
    direct_date = db.Column(db.DateTime)
    ship_decision_date = db.Column(db.DateTime)
    slip_number = db.Column(db.String(20))
    ship_result = db.Column(db.String(16))
    send_name = db.Column(db.String(72), nullable=False, index=True)
    send_chgdept = db.Column(db.String(100))
    send_chgpost = db.Column(db.String(40))
    send_chgname = db.Column(db.String(40))
    send_zip = db.Column(db.String(7), nullable=False)
    send_addr1 = db.Column(db.String(8), nullable=False)
    send_addr2 = db.Column(db.String(100), nullable=False)
    send_addr3 = db.Column(db.String(100))
    send_telno = db.Column(db.String(11), index=True)
    memo = db.Column(db.String(512))
    express_flg = db.Column(db.String(1), nullable=False)
    sign_kind = db.Column(db.String(1))
    res_base = db.Column(db.String(4))
    res_base_num = db.Column(db.Numeric(2, 0))
    res_add1 = db.Column(db.String(4))
    res_add1_num = db.Column(db.Numeric(2, 0))
    res_add2 = db.Column(db.String(4))
    res_add2_num = db.Column(db.Numeric(2, 0))
    res_add3 = db.Column(db.String(4))
    res_add3_num = db.Column(db.Numeric(2, 0))
    res_add4 = db.Column(db.String(4))
    res_add4_num = db.Column(db.Numeric(2, 0))


class AuSetInfo(db.Model):
    __tablename__ = 'au_set_info'

    contract_no = db.Column(db.String(12), primary_key=True)
    isp_order_no = db.Column(db.String(20), nullable=False)
    renew_date = db.Column(db.DateTime, nullable=False)
    create_date = db.Column(db.DateTime, nullable=False)
    operate_cd = db.Column(db.String(128), nullable=False)
    c_flag = db.Column(db.String(1))
    apply_date = db.Column(db.DateTime, nullable=False)
    auset_camp_status = db.Column(db.String(2), nullable=False)
    auset_camp_available = db.Column(db.String(1), nullable=False)
    auset_camp_ng_reason = db.Column(db.String(1))
    auset_camp_disc = db.Column(db.String(1), nullable=False)
    au_cont_telno = db.Column(db.String(11), nullable=False)
    au_firstname_k = db.Column(db.String(20))
    au_lastname_k = db.Column(db.String(100), nullable=False)
    au_cont_zip = db.Column(db.String(7))
    au_cont_todohuken = db.Column(db.String(8))
    au_cont_shiku = db.Column(db.String(60))
    au_cont_area_chome_banchi = db.Column(db.String(60))
    au_cont_build_name = db.Column(db.String(100))
    auset_appy_available = db.Column(db.String(1), nullable=False)
    auset_appy_ng_reason = db.Column(db.String(1))
    auset_appy_disc = db.Column(db.String(1), nullable=False)


class BankCalenderMst(db.Model):
    __tablename__ = 'bank_calender_mst'

    year_month = db.Column(db.String(6), primary_key=True)
    disp_mmdd = db.Column(db.String(4))


class BankMst(db.Model):
    __tablename__ = 'bank_mst'

    bnkcd = db.Column(db.String(4), primary_key=True)
    bnkkana = db.Column(db.String(60))
    bnkname = db.Column(db.String(46))
    pwd_valid_flag = db.Column(db.String(1), nullable=False)
    pwd_stro_kbn = db.Column(db.String(1))
    abolish_flag = db.Column(db.String(1), nullable=False)


t_bill_customer = db.Table(
    'bill_customer',
    db.Column('customer_id', db.String(8), nullable=False),
    db.Column('creditor_cd', db.String(1), nullable=False),
    db.Column('creditor_subcd', db.String(3)),
    db.Column('sales_dmd_kbn', db.String(1)),
    db.Column('tax_percent', db.Numeric(4, 1), nullable=False),
    db.Column('taxable_total', db.Numeric(10, 0), nullable=False),
    db.Column('taxfree_total', db.Numeric(10, 0), nullable=False),
    db.Column('tax_total', db.Numeric(10, 0), nullable=False),
    db.Index('idx_bill_customer_01', 'customer_id', 'creditor_cd', 'creditor_subcd', 'sales_dmd_kbn', 'tax_percent')
)


class BillDetail(db.Model):
    __tablename__ = 'bill_detail'

    create_date = db.Column(db.DateTime, nullable=False)
    renew_date = db.Column(db.DateTime, nullable=False)
    operate_cd = db.Column(db.String(128), nullable=False)
    c_flag = db.Column(db.String(1))
    dmdto_id = db.Column(db.String(12), primary_key=True, nullable=False)
    customer_id = db.Column(db.String(8), primary_key=True, nullable=False)
    contract_no = db.Column(db.String(12), primary_key=True, nullable=False)
    bill_detailno = db.Column(db.Numeric(5, 0), primary_key=True, nullable=False)
    opt_contract_no = db.Column(db.Numeric(10, 0))
    plan_cd = db.Column(db.String(8))
    disc_type = db.Column(db.String(2))
    disc_cd = db.Column(db.String(3))
    bill_kbn_cd = db.Column(db.String(2), nullable=False)
    bill_start = db.Column(db.DateTime, nullable=False)
    bill_end = db.Column(db.DateTime)
    quantity = db.Column(db.Numeric(19, 0))
    unit = db.Column(db.String(10))
    unit_cost = db.Column(db.Numeric(10, 4))
    tax_cost = db.Column(db.Numeric(9, 0))
    account_id = db.Column(db.String(64))
    adjust_renban = db.Column(db.Numeric(9, 0))
    cost = db.Column(db.Numeric(9, 0), nullable=False)
    taxfree_kbn = db.Column(db.String(1), nullable=False)
    kihon_tuika_kbn = db.Column(db.String(1))
    kddi_plan_cd = db.Column(db.String(10))
    plan_name = db.Column(db.String(128))
    creditor_cd = db.Column(db.String(1), nullable=False)
    ntt_plan_cd = db.Column(db.String(10))
    creditor_subcd = db.Column(db.String(3))
    sales_dmd_kbn = db.Column(db.String(1))
    demand_count = db.Column(db.Numeric(2, 0))
    jpayment_trade_no = db.Column(db.String(64))
    tax_percent = db.Column(db.Numeric(4, 1))


t_bill_dmd = db.Table(
    'bill_dmd',
    db.Column('dmdto_id', db.String(12), nullable=False),
    db.Column('creditor_cd', db.String(1), nullable=False),
    db.Column('creditor_subcd', db.String(3)),
    db.Column('sales_dmd_kbn', db.String(1)),
    db.Column('use_aim', db.Numeric(1, 0)),
    db.Column('stat_kbn', db.Numeric(1, 0)),
    db.Column('tax_percent', db.Numeric(4, 1), nullable=False),
    db.Column('taxable_total', db.Numeric(10, 0), nullable=False),
    db.Column('taxfree_total', db.Numeric(10, 0), nullable=False),
    db.Column('tax_total', db.Numeric(10, 0), nullable=False),
    db.Index('idx_bill_dmd_01', 'dmdto_id', 'creditor_cd', 'creditor_subcd', 'sales_dmd_kbn', 'use_aim', 'stat_kbn', 'tax_percent')
)


class BillHistory(db.Model):
    __tablename__ = 'bill_history'

    bill_month = db.Column(db.Date, primary_key=True, nullable=False)
    history = db.Column(db.Numeric(2, 0), primary_key=True, nullable=False)
    create_date = db.Column(db.DateTime, nullable=False)
    operate_cd = db.Column(db.String(128), nullable=False)


class BillShiftContract(db.Model):
    __tablename__ = 'bill_shift_contract'

    create_date = db.Column(db.DateTime, nullable=False)
    renew_date = db.Column(db.DateTime, nullable=False)
    operate_cd = db.Column(db.String(128), nullable=False)
    c_flag = db.Column(db.String(1))
    contract_no = db.Column(db.String(12), primary_key=True, nullable=False)
    used_month = db.Column(db.Date, primary_key=True, nullable=False)
    org_bill_month = db.Column(db.Date, nullable=False)
    plan_bill_month = db.Column(db.Date)
    dmdto_id = db.Column(db.String(12), nullable=False)
    kddi_taxable_total = db.Column(db.Numeric(10, 0), nullable=False)
    kddi_taxfree_total = db.Column(db.Numeric(10, 0), nullable=False)
    kddi_tax = db.Column(db.Numeric(10, 0), nullable=False)
    collection_taxable_total = db.Column(db.Numeric(10, 0), nullable=False)
    collection_taxin_total = db.Column(db.Numeric(10, 0), nullable=False)
    ntt_e_taxable_total = db.Column(db.Numeric(10, 0), nullable=False)
    ntt_e_taxfree_total = db.Column(db.Numeric(10, 0), nullable=False)
    ntt_e_tax_total = db.Column(db.Numeric(10, 0), nullable=False)
    ntt_w_taxable_total = db.Column(db.Numeric(10, 0), nullable=False)
    ntt_w_taxfree_total = db.Column(db.Numeric(10, 0), nullable=False)
    ntt_w_tax_total = db.Column(db.Numeric(10, 0), nullable=False)


class BillShiftDetail(db.Model):
    __tablename__ = 'bill_shift_detail'

    create_date = db.Column(db.DateTime, nullable=False)
    renew_date = db.Column(db.DateTime, nullable=False)
    operate_cd = db.Column(db.String(128), nullable=False)
    c_flag = db.Column(db.String(1))
    org_bill_month = db.Column(db.Date, primary_key=True, nullable=False)
    plan_bill_month = db.Column(db.Date)
    dmdto_id = db.Column(db.String(12), primary_key=True, nullable=False)
    customer_id = db.Column(db.String(8), primary_key=True, nullable=False)
    contract_no = db.Column(db.String(12), primary_key=True, nullable=False)
    bill_detailno = db.Column(db.Numeric(5, 0), primary_key=True, nullable=False)
    opt_contract_no = db.Column(db.Numeric(10, 0))
    plan_cd = db.Column(db.String(8))
    disc_type = db.Column(db.String(2))
    disc_cd = db.Column(db.String(3))
    bill_kbn_cd = db.Column(db.String(2), nullable=False)
    bill_start = db.Column(db.DateTime, nullable=False)
    bill_end = db.Column(db.DateTime)
    quantity = db.Column(db.Numeric(19, 0))
    unit = db.Column(db.String(10))
    unit_cost = db.Column(db.Numeric(10, 4))
    tax_cost = db.Column(db.Numeric(9, 0))
    account_id = db.Column(db.String(64))
    adjust_renban = db.Column(db.Numeric(9, 0))
    cost = db.Column(db.Numeric(9, 0), nullable=False)
    taxfree_kbn = db.Column(db.String(1), nullable=False)
    kihon_tuika_kbn = db.Column(db.String(1))
    kddi_plan_cd = db.Column(db.String(10))
    plan_name = db.Column(db.String(128))
    creditor_cd = db.Column(db.String(1), nullable=False)
    ntt_plan_cd = db.Column(db.String(10))
    creditor_subcd = db.Column(db.String(3))
    tax_percent = db.Column(db.Numeric(4, 1))


class BranchMst(db.Model):
    __tablename__ = 'branch_mst'

    bnkcd = db.Column(db.String(4), primary_key=True, nullable=False)
    brncd = db.Column(db.String(3), primary_key=True, nullable=False)
    brnsidecd = db.Column(db.String(1), primary_key=True, nullable=False)
    brnkana = db.Column(db.String(40))
    brnname = db.Column(db.String(30))
    brnzip = db.Column(db.String(10))
    brnaddress = db.Column(db.String(110))
    brntelno = db.Column(db.String(20))
    brninvexgno = db.Column(db.String(4))
    abolish_flag = db.Column(db.String(1))


t_branch_wk = db.Table(
    'branch_wk',
    db.Column('bnkcd', db.String(4)),
    db.Column('brncd', db.String(3)),
    db.Column('bnkkana', db.String(60)),
    db.Column('bnkname', db.String(46)),
    db.Column('brnkana', db.String(40)),
    db.Column('brnname', db.String(30)),
    db.Column('brnzip', db.String(10)),
    db.Column('brnaddress', db.String(110)),
    db.Column('brntelno', db.String(20)),
    db.Column('brninvexgno', db.String(4)),
    db.Column('brnsidecd', db.String(1))
)


class BulkAdjust(db.Model):
    __tablename__ = 'bulk_adjust'

    bill_month = db.Column(db.Date, primary_key=True, nullable=False)
    proc_renban = db.Column(db.Numeric(3, 0), primary_key=True, nullable=False)
    file_nm = db.Column(db.String(256), nullable=False)
    proc_status = db.Column(db.String(1), nullable=False)
    proc_date = db.Column(db.DateTime)
    create_date = db.Column(db.DateTime, nullable=False)
    renew_date = db.Column(db.DateTime, nullable=False)
    operate_cd = db.Column(db.String(128), nullable=False)
    c_flag = db.Column(db.String(1))


class BulkAdjustWk(db.Model):
    __tablename__ = 'bulk_adjust_wk'

    bill_month = db.Column(db.Date, primary_key=True, nullable=False)
    proc_renban = db.Column(db.Numeric(3, 0), primary_key=True, nullable=False)
    line_no = db.Column(db.Numeric(6, 0), primary_key=True, nullable=False)
    line_text = db.Column(db.String(1024), nullable=False)
    create_date = db.Column(db.DateTime, nullable=False)
    renew_date = db.Column(db.DateTime, nullable=False)
    operate_cd = db.Column(db.String(128), nullable=False)
    c_flag = db.Column(db.String(1))


class CardRefileMst(db.Model):
    __tablename__ = 'card_refile_mst'

    system_id = db.Column(db.Numeric(4, 0), primary_key=True)
    sales_valid_kbn = db.Column(db.Numeric(1, 0))
    card_corpname = db.Column(db.String(10))
    card_cd = db.Column(db.String(4))
    cd_start = db.Column(db.Numeric(8, 0))
    cd_end = db.Column(db.Numeric(8, 0))
    card_figure = db.Column(db.Numeric(2, 0))
    cardkind = db.Column(db.String(2))
    note = db.Column(db.String(512))
    priority_flag = db.Column(db.String(1))
    amount = db.Column(db.Numeric(6, 0))


class Cashback(db.Model):
    __tablename__ = 'cashback'

    cashback_no = db.Column(db.Numeric(10, 0), primary_key=True)
    master_kbn = db.Column(db.String(1), nullable=False)
    work_kbn = db.Column(db.String(2), nullable=False)
    customer_id = db.Column(db.String(8), nullable=False, index=True)
    policy_no = db.Column(db.String(10))
    cashback_cost = db.Column(db.Numeric(10, 0))
    cashback_status = db.Column(db.String(3))
    order_date = db.Column(db.DateTime)
    create_date = db.Column(db.DateTime, nullable=False)
    renew_date = db.Column(db.DateTime, nullable=False)
    operate_cd = db.Column(db.String(128), nullable=False)
    cashback_lastname_k = db.Column(db.String(200))
    cashback_firstname_k = db.Column(db.String(200))
    cashback_email = db.Column(db.String(128))
    order_plan_month = db.Column(db.Date)
    contract_no = db.Column(db.String(12))
    opt_contract_no = db.Column(db.Numeric(10, 0))
    cashback_method = db.Column(db.String(1))
    prog_status = db.Column(db.String(2))
    send_mail_date = db.Column(db.DateTime)


class CashbackMst(db.Model):
    __tablename__ = 'cashback_mst'

    policy_no = db.Column(db.String(10), primary_key=True)
    policy_name = db.Column(db.String(128), nullable=False)
    policy_start_date = db.Column(db.DateTime)
    policy_end_date = db.Column(db.DateTime)
    cashback_cost = db.Column(db.Numeric(10, 0), nullable=False)
    create_date = db.Column(db.DateTime, nullable=False)
    renew_date = db.Column(db.DateTime, nullable=False)
    operate_cd = db.Column(db.String(128), nullable=False)
    cashback_month = db.Column(db.Numeric(2, 0))
    cashback_method = db.Column(db.String(1))
    open_term = db.Column(db.DateTime)


class CashpoDat(db.Model):
    __tablename__ = 'cashpo_dat'

    cashpo_no = db.Column(db.String(10), primary_key=True)
    epark_order_id = db.Column(db.String(22), nullable=False)
    contbase_no = db.Column(db.String(10), nullable=False, index=True)
    policy_no = db.Column(db.String(10), nullable=False)
    coop_kind = db.Column(db.String(4), nullable=False)
    coop_status = db.Column(db.String(1))
    coop_nth_time = db.Column(db.Numeric(2, 0))
    plan_coop_month = db.Column(db.String(6))
    coop_date = db.Column(db.Date)
    plan_vest_date = db.Column(db.Date)
    create_date = db.Column(db.DateTime, nullable=False)
    renew_date = db.Column(db.DateTime, nullable=False)
    operate_cd = db.Column(db.String(128), nullable=False)


class CashpoMst(db.Model):
    __tablename__ = 'cashpo_mst'

    policy_no = db.Column(db.String(10), primary_key=True)
    policy_name = db.Column(db.String(128), nullable=False)
    policy_start_date = db.Column(db.Date, nullable=False)
    policy_end_date = db.Column(db.Date)
    fee_extract_interval_months = db.Column(db.Numeric(2, 0), nullable=False)
    cashpo_cost = db.Column(db.Numeric(10, 0), nullable=False)
    vest_count = db.Column(db.Numeric(2, 0), nullable=False)
    first_extract_elapsed_months = db.Column(db.Numeric(2, 0), nullable=False)
    extract_interval_months = db.Column(db.Numeric(2, 0), nullable=False)
    vest_elapsed_months = db.Column(db.Numeric(2, 0), nullable=False)
    vest_business_day = db.Column(db.Numeric(2, 0), nullable=False)
    create_date = db.Column(db.DateTime, nullable=False)
    renew_date = db.Column(db.DateTime, nullable=False)
    operate_cd = db.Column(db.String(128), nullable=False)


class ConditionMst(db.Model):
    __tablename__ = 'condition_mst'

    condition_no = db.Column(db.Numeric(5, 0), primary_key=True)
    create_date = db.Column(db.DateTime, nullable=False)
    renew_date = db.Column(db.DateTime, nullable=False)
    operate_cd = db.Column(db.String(128), nullable=False)
    policy_no = db.Column(db.String(10))
    plan_cd = db.Column(db.String(8))
    campaign_cd = db.Column(db.String(15))
    agency_cd = db.Column(db.String(12))


class ConsumptionTax(db.Model):
    __tablename__ = 'consumption_tax'

    valid_date = db.Column(db.DateTime, primary_key=True)
    tax_percent = db.Column(db.Numeric(4, 1), nullable=False)
    create_date = db.Column(db.DateTime, nullable=False)
    renew_date = db.Column(db.DateTime, nullable=False)
    operate_cd = db.Column(db.String(128), nullable=False)
    c_flag = db.Column(db.String(1))


class ContentsBillInfo(db.Model):
    __tablename__ = 'contents_bill_info'

    bill_month = db.Column(db.Date, primary_key=True, nullable=False)
    data_renbn = db.Column(db.Numeric(7, 0), primary_key=True, nullable=False)
    buy_date = db.Column(db.DateTime, nullable=False)
    provider_cd = db.Column(db.String(8), nullable=False)
    service_cd = db.Column(db.String(16), nullable=False)
    cost = db.Column(db.Numeric(9, 0), nullable=False)
    tax_cost = db.Column(db.Numeric(9, 0))
    tax_percent = db.Column(db.Numeric(4, 1))
    note = db.Column(db.String(512))
    contbase_no = db.Column(db.String(10), nullable=False)
    taxfree_kbn = db.Column(db.String(1), nullable=False)
    plan_cd = db.Column(db.String(8))
    create_date = db.Column(db.DateTime, nullable=False)
    renew_date = db.Column(db.DateTime, nullable=False)
    operate_cd = db.Column(db.String(128), nullable=False)


class Contract(db.Model):
    __tablename__ = 'contract'

    contract_no = db.Column(db.String(12), primary_key=True)
    customer_id = db.Column(db.String(8), nullable=False, index=True)
    contbase_no = db.Column(db.String(10), nullable=False, index=True)
    cont_renbn = db.Column(db.String(2), nullable=False)
    plan_cd = db.Column(db.String(8), nullable=False)
    vc_no = db.Column(db.String(10))
    order_status = db.Column(db.String(2), nullable=False)
    cont_apply_date = db.Column(db.DateTime)
    cont_start_date = db.Column(db.DateTime)
    cont_end_date = db.Column(db.DateTime)
    cont_cancel_date = db.Column(db.DateTime)
    cancel_status = db.Column(db.String(2))
    cancel_apply_date = db.Column(db.DateTime)
    cancel_date = db.Column(db.DateTime)
    agency_cd = db.Column(db.String(12), index=True)
    campaign_cd = db.Column(db.String(15))
    flets_apply_id = db.Column(db.String(14))
    create_date = db.Column(db.DateTime, nullable=False)
    renew_date = db.Column(db.DateTime, nullable=False)
    operate_cd = db.Column(db.String(128), nullable=False)
    c_flag = db.Column(db.String(1))
    apply_status = db.Column(db.String(2))
    unsuited_date = db.Column(db.DateTime)
    bill_start_date = db.Column(db.DateTime)
    apply_no = db.Column(db.String(10))
    penalty_remission_month = db.Column(db.Date)
    cont_chgname = db.Column(db.String(20))
    order_no = db.Column(db.String(26))
    partner_channel = db.Column(db.String(128))
    partner_info = db.Column(db.String(1024))
    monthly_end_date = db.Column(db.Date)
    syonin_status = db.Column(db.String(3))
    syonin_date = db.Column(db.DateTime)
    fraud_detect_event_id = db.Column(db.String(47))
    fraud_detect_result = db.Column(db.String(10))


class ContractOpt(db.Model):
    __tablename__ = 'contract_opt'

    opt_contract_no = db.Column(db.Numeric(10, 0), primary_key=True)
    customer_id = db.Column(db.String(8), nullable=False, index=True)
    contbase_no = db.Column(db.String(10), nullable=False, index=True)
    plan_cd = db.Column(db.String(8), nullable=False)
    opt_status = db.Column(db.String(2), nullable=False)
    opt_apply_date = db.Column(db.DateTime)
    opt_start_date = db.Column(db.DateTime)
    opt_end_date = db.Column(db.DateTime)
    opt_cancel_status = db.Column(db.String(2))
    opt_cancel_apply = db.Column(db.DateTime)
    opt_cancel_date = db.Column(db.DateTime)
    opt_agency_cd = db.Column(db.String(12))
    opt_campaign_cd = db.Column(db.String(15))
    opt_kbn_cd = db.Column(db.String(2), nullable=False)
    create_date = db.Column(db.DateTime, nullable=False)
    renew_date = db.Column(db.DateTime, nullable=False)
    operate_cd = db.Column(db.String(128), nullable=False)
    c_flag = db.Column(db.String(1))
    apply_status = db.Column(db.String(2))
    unsuited_date = db.Column(db.DateTime)
    penalty_end_date = db.Column(db.DateTime)
    partner_channel = db.Column(db.String(128))
    partner_info = db.Column(db.String(1024))


class CpassDemandTran(db.Model):
    __tablename__ = 'cpass_demand_trans'

    dmdto_id = db.Column(db.String(12), primary_key=True)
    cpass_cst_no = db.Column(db.String(8), nullable=False)
    create_date = db.Column(db.DateTime, nullable=False)
    renew_date = db.Column(db.DateTime, nullable=False)
    operate_cd = db.Column(db.String(128), nullable=False)


class Customer(db.Model):
    __tablename__ = 'customer'

    custinfo_id = db.Column(db.Numeric(10, 0), primary_key=True)
    old_custid = db.Column(db.String(15))
    firstname = db.Column(db.String(20), index=True)
    firstname_k = db.Column(db.String(20), index=True)
    lastname = db.Column(db.String(50), nullable=False, index=True)
    lastname_k = db.Column(db.String(100), index=True)
    cust_zip = db.Column(db.String(7), nullable=False, index=True)
    cust_addr1 = db.Column(db.String(4), nullable=False)
    cust_addr2 = db.Column(db.String(50), nullable=False)
    cust_addr3 = db.Column(db.String(50))
    cust_addr1_k = db.Column(db.String(6))
    cust_addr2_k = db.Column(db.String(100))
    cust_addr3_k = db.Column(db.String(100))
    cust_telno = db.Column(db.String(11), nullable=False, index=True)
    cust_faxno = db.Column(db.String(11))
    cust_user_type = db.Column(db.String(1), nullable=False)
    cust_level = db.Column(db.String(2))
    cust_fukushi = db.Column(db.String(1))
    cust_chgdept = db.Column(db.String(50))
    cust_chgpost = db.Column(db.String(20))
    cust_chgname = db.Column(db.String(20), index=True)
    cust_chgname_k = db.Column(db.String(40), index=True)
    addr_defect_cre_date = db.Column(db.DateTime)
    addr_defect_off_date = db.Column(db.DateTime)
    create_date = db.Column(db.DateTime, nullable=False)
    renew_date = db.Column(db.DateTime, nullable=False)
    operate_cd = db.Column(db.String(128), nullable=False)
    c_flag = db.Column(db.String(1))
    stockholder_cd = db.Column(db.String(10), index=True)
    address_code = db.Column(db.String(11))
    cust_banchi1 = db.Column(db.String(40))
    cust_banchi2 = db.Column(db.String(20))
    cust_banchi3 = db.Column(db.String(20))
    cust_sex = db.Column(db.String(1))
    cust_birth = db.Column(db.DateTime)
    cust_job = db.Column(db.String(2))


class CustomerIdMng(db.Model):
    __tablename__ = 'customer_id_mng'

    customer_id = db.Column(db.String(8), primary_key=True)
    custinfo_id = db.Column(db.Numeric(10, 0), nullable=False, index=True)
    cust_password = db.Column(db.String(32), nullable=False)
    cust_status = db.Column(db.String(1), nullable=False)
    approval_date = db.Column(db.DateTime)
    pay_status = db.Column(db.String(1), nullable=False)
    pay_status_renew_date = db.Column(db.DateTime)
    dmdto_id = db.Column(db.String(12), nullable=False, index=True)
    dmd_method = db.Column(db.String(1), nullable=False)
    apply_type = db.Column(db.String(1), nullable=False)
    member_kind = db.Column(db.String(1), nullable=False, index=True)
    cust_apply_date = db.Column(db.DateTime)
    cust_start_date = db.Column(db.DateTime)
    cust_end_apply_date = db.Column(db.DateTime)
    cust_cancel_date = db.Column(db.DateTime)
    cust_end_date = db.Column(db.DateTime)
    cust_email = db.Column(db.String(128))
    create_date = db.Column(db.DateTime, nullable=False, index=True)
    renew_date = db.Column(db.DateTime, nullable=False)
    operate_cd = db.Column(db.String(128), nullable=False)
    c_flag = db.Column(db.String(1))
    cust_apply_status = db.Column(db.String(2))
    old_isp = db.Column(db.String(3))
    non_volume_discount = db.Column(db.String(1))


class CustomerReserve(db.Model):
    __tablename__ = 'customer_reserve'

    customer_id = db.Column(db.String(8), primary_key=True)
    change_status = db.Column(db.String(1), nullable=False)
    change_date = db.Column(db.DateTime, nullable=False)
    cust_zip = db.Column(db.String(7), nullable=False)
    cust_addr1 = db.Column(db.String(4), nullable=False)
    cust_addr2 = db.Column(db.String(50), nullable=False)
    cust_addr3 = db.Column(db.String(50))
    cust_telno = db.Column(db.String(11), nullable=False)
    create_date = db.Column(db.DateTime, nullable=False)
    renew_date = db.Column(db.DateTime, nullable=False)
    operate_cd = db.Column(db.String(128), nullable=False)


class CustomerSup(db.Model):
    __tablename__ = 'customer_sup'

    incident_id = db.Column(db.Numeric(10, 0), primary_key=True)
    incident_kind = db.Column(db.String(1))
    customer_id = db.Column(db.String(8), nullable=False, index=True)
    contract_no = db.Column(db.String(12), index=True)
    receipt_channel = db.Column(db.String(2))
    base_plan_cd = db.Column(db.String(8))
    add_plan_cd = db.Column(db.String(8))
    opt_plan_cd = db.Column(db.String(8))
    account_kind = db.Column(db.String(1))
    account_name = db.Column(db.String(128))
    contact_telno = db.Column(db.String(16))
    contact_email = db.Column(db.String(128))
    incident_status = db.Column(db.String(2))
    lock_status = db.Column(db.String(1))
    inq_item1 = db.Column(db.Numeric(10, 0))
    inq_item2 = db.Column(db.Numeric(10, 0))
    inq_item3 = db.Column(db.Numeric(10, 0))
    subject = db.Column(db.String(1))
    area = db.Column(db.String(8))
    line_traders = db.Column(db.String(2))
    os = db.Column(db.String(3))
    line_kind = db.Column(db.Numeric(10, 0))
    document_kind = db.Column(db.String(2048))
    inquiry_content = db.Column(db.Text)
    answer = db.Column(db.Text)
    register_cd = db.Column(db.String(128))
    create_date = db.Column(db.DateTime, nullable=False)
    renew_date = db.Column(db.DateTime, nullable=False, index=True)
    operate_cd = db.Column(db.String(128), nullable=False)
    c_flag = db.Column(db.String(1))
    firstname = db.Column(db.String(20))
    lastname = db.Column(db.String(50))
    cust_zip = db.Column(db.String(7))
    cust_addr1 = db.Column(db.String(4))
    cust_addr2 = db.Column(db.String(50))
    cust_addr3 = db.Column(db.String(50))
    cust_chgdept = db.Column(db.String(50))
    cust_chgpost = db.Column(db.String(20))
    cust_chgname = db.Column(db.String(20))
    cust_telno = db.Column(db.String(11))
    req_plan_cd = db.Column(db.String(128))


class Demandto(db.Model):
    __tablename__ = 'demandto'

    dmdto_id = db.Column(db.String(12), primary_key=True, nullable=False)
    valid_date = db.Column(db.DateTime, primary_key=True, nullable=False)
    valid_flag = db.Column(db.String(1))
    pwd_kbn = db.Column(db.String(1))
    dmdto_status = db.Column(db.String(2))
    ng_rsn = db.Column(db.String(3))
    pay_chg_rsn = db.Column(db.String(2))
    account_ask_no = db.Column(db.String(20))
    demand_kbn = db.Column(db.String(2), nullable=False)
    detail_kbn = db.Column(db.String(2), nullable=False)
    detail_rsn = db.Column(db.String(255))
    pwd_demandprint_kbn = db.Column(db.String(1), nullable=False)
    old_dmdto_cd = db.Column(db.String(15), index=True)
    cust_user_type = db.Column(db.String(1), nullable=False)
    dmd_firstname = db.Column(db.String(20))
    dmd_firstname_k = db.Column(db.String(20))
    dmd_lastname = db.Column(db.String(50))
    dmd_lastname_k = db.Column(db.String(100))
    dmd_zip = db.Column(db.String(7))
    dmd_addr1 = db.Column(db.String(4))
    dmd_addr2 = db.Column(db.String(50))
    dmd_addr3 = db.Column(db.String(50))
    dmd_addr1_k = db.Column(db.String(6))
    dmd_addr2_k = db.Column(db.String(100))
    dmd_addr3_k = db.Column(db.String(100))
    dmd_telno = db.Column(db.String(11), index=True)
    dmd_faxno = db.Column(db.String(11))
    dmd_email = db.Column(db.String(128))
    dmd_chgdept = db.Column(db.String(50))
    dmd_chgtitle = db.Column(db.String(20))
    dmd_chgname = db.Column(db.String(20))
    dmd_chgname_k = db.Column(db.String(40))
    cardkind = db.Column(db.String(2))
    cardno = db.Column(db.String(16))
    cardvalid = db.Column(db.String(6))
    verify_no = db.Column(db.String(8))
    verify_money = db.Column(db.Numeric(8, 0))
    verify_date = db.Column(db.DateTime)
    agreement = db.Column(db.String(1))
    pwd_stro_cd = db.Column(db.String(1))
    trans_bankcd = db.Column(db.String(4))
    trans_branchcd = db.Column(db.String(3))
    trans_linecd = db.Column(db.String(1))
    trans_acckind = db.Column(db.String(1))
    trans_accno = db.Column(db.String(7))
    trans_accname = db.Column(db.String(60))
    kobetu_bankcd = db.Column(db.String(4))
    kobetu_branchcd = db.Column(db.String(3))
    kobetu_linecd = db.Column(db.String(1))
    kobetu_acckind = db.Column(db.String(1))
    kobetu_accno = db.Column(db.String(7))
    kobetu_accname = db.Column(db.String(60))
    dmdto_memo = db.Column(db.String(128))
    end_date = db.Column(db.DateTime)
    addr_defect_cre_date = db.Column(db.DateTime)
    addr_defect_off_date = db.Column(db.DateTime)
    demand_renew_date = db.Column(db.DateTime)
    demand_operate_cd = db.Column(db.String(128))
    payment_renew_date = db.Column(db.DateTime)
    payment_operate_cd = db.Column(db.String(128))
    ol_new_user_trans_flag = db.Column(db.String(1))
    create_date = db.Column(db.DateTime, nullable=False)
    renew_date = db.Column(db.DateTime, nullable=False)
    operate_cd = db.Column(db.String(128), nullable=False)
    c_flag = db.Column(db.String(1))
    confirm_kbn = db.Column(db.String(1))
    ntt_assentor_name = db.Column(db.String(128))
    ntt_kbn = db.Column(db.String(2))
    ntt_apply_date = db.Column(db.DateTime)
    ntt_user_tel_no = db.Column(db.String(11))
    entrepreneur_cd = db.Column(db.String(4))
    address_code = db.Column(db.String(11))
    dmd_banchi1 = db.Column(db.String(40))
    dmd_banchi2 = db.Column(db.String(20))
    dmd_banchi3 = db.Column(db.String(20))
    yuso_ptn_cd = db.Column(db.String(2), nullable=False, server_default=db.FetchedValue())
    kddi_dmd_kbn = db.Column(db.String(1))
    kddi_mng_no = db.Column(db.Numeric(10, 0), index=True)
    ntt_id = db.Column(db.String(12))
    ntt_name = db.Column(db.String(128))
    ntt_name_k = db.Column(db.String(256))
    change_possible_date = db.Column(db.DateTime)
    tabal_keep_branch = db.Column(db.String(4))
    nttf_kind = db.Column(db.String(1))


class DeviceChangeDat(db.Model):
    __tablename__ = 'device_change_dat'

    ws_common_id = db.Column(db.String(20), primary_key=True)
    ws_common_renbn = db.Column(db.String(2), nullable=False)
    contract_no = db.Column(db.String(12), nullable=False, index=True)
    opt_contract_no = db.Column(db.Numeric(10, 0), nullable=False)
    isp_order_no = db.Column(db.String(16), nullable=False)
    renew_date = db.Column(db.DateTime, nullable=False)
    create_date = db.Column(db.DateTime, nullable=False)
    operate_cd = db.Column(db.String(128), nullable=False)
    c_flag = db.Column(db.String(1))
    send_plan_date = db.Column(db.DateTime)
    send_date = db.Column(db.DateTime)
    apply_date = db.Column(db.DateTime)
    apply_kind = db.Column(db.String(4), nullable=False)
    prog_status = db.Column(db.String(2), nullable=False)
    send_service_cd = db.Column(db.String(8), nullable=False)
    send_name_lastname = db.Column(db.String(60), nullable=False)
    send_name_firstname = db.Column(db.String(60), nullable=False)
    send_name_lastname_k = db.Column(db.String(120))
    send_name_firstname_k = db.Column(db.String(120))
    send_zip = db.Column(db.String(7), nullable=False)
    send_todohuken = db.Column(db.String(8), nullable=False)
    send_addr1 = db.Column(db.String(100), nullable=False)
    send_addr2 = db.Column(db.String(100))
    send_build_name = db.Column(db.String(80))
    send_telno = db.Column(db.String(11))
    ship_no = db.Column(db.String(20))
    ship_decision_date = db.Column(db.DateTime)
    ship_comp_date = db.Column(db.DateTime)
    ship_return_date = db.Column(db.DateTime)
    send_status = db.Column(db.String(2))
    org_isp_order_no = db.Column(db.String(20))
    cont_sex = db.Column(db.String(1), nullable=False)
    cont_birth = db.Column(db.DateTime, nullable=False)
    send_rent_device_cd = db.Column(db.String(20), nullable=False)
    send_rent_lost_opt_contract_no = db.Column(db.Numeric(10, 0))
    send_rent_return_limit_date = db.Column(db.DateTime)
    send_rent_return_flg = db.Column(db.String(1))
    send_rent_return_date = db.Column(db.DateTime)


class DeviceCont(db.Model):
    __tablename__ = 'device_cont'

    imei = db.Column(db.String(15), primary_key=True)
    isp_order_no = db.Column(db.String(16), nullable=False)
    contbase_no = db.Column(db.String(10), nullable=False)
    opt_contract_no = db.Column(db.Numeric(10, 0))
    renew_date = db.Column(db.DateTime, nullable=False)
    create_date = db.Column(db.DateTime, nullable=False)
    operate_cd = db.Column(db.String(128), nullable=False)
    c_flag = db.Column(db.String(1))
    work_kind = db.Column(db.String(2), nullable=False)
    rent_device_cd = db.Column(db.String(20), nullable=False)
    device_status = db.Column(db.String(2))


t_df_headrecord_mst = db.Table(
    'df_headrecord_mst',
    db.Column('hdrcmmcd', db.String(10)),
    db.Column('hdrcmmname', db.String(80)),
    db.Column('hdrgetdate', db.String(4)),
    db.Column('hdrbnkcd', db.String(4)),
    db.Column('hdrbnkname', db.String(92)),
    db.Column('hdrbrncd', db.String(3)),
    db.Column('hdrbrnname', db.String(60)),
    db.Column('hdracckind', db.String(1)),
    db.Column('hdraccno', db.String(7))
)


class DfRegreference(db.Model):
    __tablename__ = 'df_regreference'

    dmdto_id = db.Column(db.String(12), primary_key=True)
    rgraccname = db.Column(db.String(60))
    rgrbnkname = db.Column(db.String(4))
    rgrbrncd = db.Column(db.String(3))
    rgracckind = db.Column(db.String(1))
    rgraccno = db.Column(db.String(7))
    create_date = db.Column(db.DateTime, nullable=False)
    renew_date = db.Column(db.DateTime, nullable=False)


t_disc_commission_old_isp = db.Table(
    'disc_commission_old_isp',
    db.Column('disc_cd', db.String(3)),
    db.Column('customer_id', db.String(8))
)


t_disc_mail_point = db.Table(
    'disc_mail_point',
    db.Column('customer_id', db.String(8)),
    db.Column('n', db.Numeric(2, 0))
)


class DiscRelMng(db.Model):
    __tablename__ = 'disc_rel_mng'
    __table_args__ = (
        db.Index('idx_disc_rel_mng_01', 'rel_contbase_no', 'rel_cont_renbn'),
    )

    customer_id = db.Column(db.String(8), nullable=False)
    contbase_no = db.Column(db.String(10), nullable=False)
    cont_renbn = db.Column(db.String(2), nullable=False)
    rel_contbase_no = db.Column(db.String(10), primary_key=True, nullable=False)
    rel_cont_renbn = db.Column(db.String(2), primary_key=True, nullable=False)
    create_date = db.Column(db.DateTime, nullable=False)
    renew_date = db.Column(db.DateTime, nullable=False)
    operate_cd = db.Column(db.String(128), nullable=False)
    disc_cd = db.Column(db.String(3))
    set_kind = db.Column(db.String(1), nullable=False)


class DiscReserve(db.Model):
    __tablename__ = 'disc_reserve'

    customer_id = db.Column(db.String(8), primary_key=True, nullable=False)
    disc_type = db.Column(db.String(2), primary_key=True, nullable=False)
    disc_cd = db.Column(db.String(3), primary_key=True, nullable=False)


class Discount(db.Model):
    __tablename__ = 'discount'

    contract_no = db.Column(db.String(12), primary_key=True, nullable=False)
    disc_renbn = db.Column(db.Numeric(4, 0), primary_key=True, nullable=False)
    opt_contract_no = db.Column(db.Numeric(10, 0), nullable=False, index=True)
    disc_type = db.Column(db.String(2), nullable=False)
    disc_cd = db.Column(db.String(3), nullable=False)
    disc_start_date = db.Column(db.DateTime)
    disc_end_date = db.Column(db.DateTime)
    create_date = db.Column(db.DateTime, nullable=False)
    renew_date = db.Column(db.DateTime, nullable=False)
    operate_cd = db.Column(db.String(128), nullable=False)
    c_flag = db.Column(db.String(1))
    disc_status = db.Column(db.String(2), nullable=False)
    cancel_date = db.Column(db.DateTime)


class DiscountMst(db.Model):
    __tablename__ = 'discount_mst'

    disc_type = db.Column(db.String(2), primary_key=True, nullable=False)
    disc_cd = db.Column(db.String(3), primary_key=True, nullable=False)
    disc_name = db.Column(db.String(256))
    plan_cd = db.Column(db.String(17), index=True)
    aitai_cd = db.Column(db.String(13))
    disc_mst_init = db.Column(db.Numeric(10, 0))
    disc_useal = db.Column(db.Numeric(10, 0))
    disc_work = db.Column(db.Numeric(10, 0))
    disc_term = db.Column(db.Numeric(2, 0))
    open_term = db.Column(db.DateTime)
    disc_point = db.Column(db.Numeric(10, 0))
    disc_memo = db.Column(db.String(128))
    disc_start_date = db.Column(db.DateTime)
    disc_end_date = db.Column(db.DateTime)
    create_date = db.Column(db.DateTime, nullable=False)
    renew_date = db.Column(db.DateTime, nullable=False)
    operate_cd = db.Column(db.String(128), nullable=False)
    partner_cd = db.Column(db.String(10))
    bfcampaign = db.Column(db.String(64))
    disc_term_round = db.Column(db.String(1))
    policy_no = db.Column(db.String(10))
    campaign_cd = db.Column(db.String(15))
    ntt_service_name = db.Column(db.String(64))
    ntt_e_agency_cd = db.Column(db.String(8))


t_dmd_customer_total = db.Table(
    'dmd_customer_total',
    db.Column('dmd_month', db.String(6), nullable=False),
    db.Column('customer_id', db.String(8), nullable=False),
    db.Column('creditor_cd', db.String(1), nullable=False),
    db.Column('creditor_subcd', db.String(3)),
    db.Column('taxable_total', db.Numeric(10, 0), nullable=False, server_default=db.FetchedValue()),
    db.Column('taxfree_total', db.Numeric(10, 0), nullable=False, server_default=db.FetchedValue()),
    db.Column('tax_total', db.Numeric(10, 0), nullable=False, server_default=db.FetchedValue()),
    db.Column('tax_percent', db.Numeric(4, 1), nullable=False),
    db.Index('idx_dmd_customer_total_01', 'dmd_month', 'customer_id', 'creditor_cd', 'creditor_subcd', 'tax_percent')
)


t_dmd_dmdto_total = db.Table(
    'dmd_dmdto_total',
    db.Column('dmd_no', db.String(13), nullable=False),
    db.Column('creditor_cd', db.String(1), nullable=False),
    db.Column('creditor_subcd', db.String(3)),
    db.Column('taxable_total', db.Numeric(10, 0), nullable=False, server_default=db.FetchedValue()),
    db.Column('taxfree_total', db.Numeric(10, 0), nullable=False, server_default=db.FetchedValue()),
    db.Column('tax_total', db.Numeric(10, 0), nullable=False, server_default=db.FetchedValue()),
    db.Column('tax_percent', db.Numeric(4, 1), nullable=False),
    db.Index('idx_dmd_dmdto_total_01', 'dmd_no', 'creditor_cd', 'creditor_subcd', 'tax_percent')
)


class DmdJobMng(db.Model):
    __tablename__ = 'dmd_job_mng'

    dmd_job_id = db.Column(db.String(3), primary_key=True, nullable=False)
    dmd_month = db.Column(db.String(6), primary_key=True, nullable=False)
    job_complete_date = db.Column(db.DateTime, nullable=False)


class Docomol2Packet(db.Model):
    __tablename__ = 'docomol2_packet'

    msisdn = db.Column(db.String(11), primary_key=True, nullable=False)
    packet_date = db.Column(db.DateTime, primary_key=True, nullable=False)
    bl_status = db.Column(db.Numeric(2, 0), primary_key=True, nullable=False)
    packet = db.Column(db.Numeric(16, 0))
    create_date = db.Column(db.DateTime, nullable=False)
    renew_date = db.Column(db.DateTime, nullable=False)
    operate_cd = db.Column(db.String(128), nullable=False)


class DomainLstMst(db.Model):
    __tablename__ = 'domain_lst_mst'

    domain_renbn = db.Column(db.Numeric(3, 0), primary_key=True)
    domain_id = db.Column(db.String(32), nullable=False)
    domain_start_date = db.Column(db.DateTime)


class DtiSimSmsLog(db.Model):
    __tablename__ = 'dti_sim_sms_log'

    used_month = db.Column(db.Date, primary_key=True, nullable=False)
    line_no = db.Column(db.Numeric(7, 0), primary_key=True, nullable=False)
    telno = db.Column(db.String(16), nullable=False, index=True)
    call_date = db.Column(db.String(8))
    call_time = db.Column(db.String(6))
    telno_dialed = db.Column(db.String(32))
    dist_type = db.Column(db.String(6))
    dist_detail = db.Column(db.String(24))
    call_duration = db.Column(db.String(7))
    time_period = db.Column(db.String(24))
    discount = db.Column(db.String(24))
    call_classification_1 = db.Column(db.String(24))
    call_classification_2 = db.Column(db.String(24))
    call_classification_3 = db.Column(db.String(24))
    separate_cd = db.Column(db.String(1), nullable=False)
    isp_name = db.Column(db.String(32))
    trans_type = db.Column(db.String(100))
    trans_kbn = db.Column(db.String(32))
    bill_month = db.Column(db.Date, nullable=False)
    contract_no = db.Column(db.String(12))
    user_charge = db.Column(db.Numeric(6, 0))
    bill_kbn_cd = db.Column(db.String(2))
    create_date = db.Column(db.DateTime, nullable=False)
    renew_date = db.Column(db.DateTime, nullable=False)
    operate_cd = db.Column(db.String(128), nullable=False)


class DtisimMst(db.Model):
    __tablename__ = 'dtisim_mst'

    plan_cd = db.Column(db.String(8), primary_key=True)
    pt2_plancd = db.Column(db.String(32), nullable=False)
    sim_type = db.Column(db.String(1), nullable=False)
    use_kbn = db.Column(db.String(1))
    pt2_account_add_kbn = db.Column(db.String(1), nullable=False)
    plan_change_kbn = db.Column(db.String(1), nullable=False)
    pt2_plancd_after = db.Column(db.String(32))
    create_date = db.Column(db.DateTime, nullable=False)
    renew_date = db.Column(db.DateTime, nullable=False)
    operate_cd = db.Column(db.String(128), nullable=False)


t_dual = db.Table(
    'dual',
    db.Column('dummy', db.String)
)


class EaDat(db.Model):
    __tablename__ = 'ea_dat'

    ws_common_id = db.Column(db.String(20), primary_key=True)
    ws_common_renbn = db.Column(db.String(2))
    contract_no = db.Column(db.String(12), nullable=False, index=True)
    isp_order_no = db.Column(db.String(20), nullable=False, index=True)
    apply_date = db.Column(db.DateTime)
    send_plan_date = db.Column(db.DateTime)
    send_date = db.Column(db.DateTime)
    apply_kind = db.Column(db.String(4))
    prog_status = db.Column(db.String(2))
    web_no = db.Column(db.String(10))
    user_cd = db.Column(db.String(1))
    ea_cust_id = db.Column(db.String(8))
    ea_contract_id = db.Column(db.String(8))
    appli_cd = db.Column(db.String(50))
    pw_cd = db.Column(db.String(50))
    plan_cd = db.Column(db.String(10))
    connect_type = db.Column(db.String(1))
    modem_cd = db.Column(db.String(1))
    work_cd = db.Column(db.String(1))
    zip = db.Column(db.String(8))
    todohuken = db.Column(db.String(8))
    gun = db.Column(db.String(40))
    ku = db.Column(db.String(40))
    area = db.Column(db.String(40))
    chome = db.Column(db.String(10))
    banchi = db.Column(db.String(40))
    build_name = db.Column(db.String(150))
    contract_telno = db.Column(db.String(13))
    telno = db.Column(db.String(13))
    toi_telno = db.Column(db.String(13))
    email = db.Column(db.String(120))
    ntt_cd = db.Column(db.String(50))
    line_kind = db.Column(db.String(1))
    line_name = db.Column(db.String(60))
    analog_cd = db.Column(db.String(1))
    linechg_cd = db.Column(db.String(1))
    facility_cd = db.Column(db.String(1))
    linein_cd = db.Column(db.String(1))
    result_date = db.Column(db.DateTime)
    ntt_result = db.Column(db.String(1))
    ntt_ng_rsn = db.Column(db.String(2))
    trans_status = db.Column(db.String(4))
    bill_date = db.Column(db.DateTime)
    change_date = db.Column(db.DateTime)
    work_date = db.Column(db.DateTime)
    campaign_cd = db.Column(db.String(15))
    agency_cd = db.Column(db.String(12))
    create_date = db.Column(db.DateTime, nullable=False)
    renew_date = db.Column(db.DateTime, nullable=False)
    operate_cd = db.Column(db.String(128), nullable=False)
    c_flag = db.Column(db.String(1))
    remark = db.Column(db.String(80))
    acca_isp_order_no = db.Column(db.String(20))


class EmBillInfo(db.Model):
    __tablename__ = 'em_bill_info'

    em_cont_cd = db.Column(db.String(10), primary_key=True, nullable=False)
    used_month = db.Column(db.Date, primary_key=True, nullable=False)
    em_plan_cd = db.Column(db.String(6), primary_key=True, nullable=False)
    create_date = db.Column(db.DateTime, nullable=False)
    renew_date = db.Column(db.DateTime, nullable=False)
    operate_cd = db.Column(db.String(128), nullable=False)
    msisdn = db.Column(db.String(11), nullable=False)
    bill_month = db.Column(db.Date, nullable=False, index=True)
    bill_kbn_cd = db.Column(db.String(2), nullable=False)
    em_plan_name = db.Column(db.String(44), nullable=False)
    cost = db.Column(db.Numeric(9, 0), nullable=False)
    quantity = db.Column(db.Numeric(19, 0))
    taxfree_kbn = db.Column(db.String(1), nullable=False)


class EmCont(db.Model):
    __tablename__ = 'em_cont'

    contract_no = db.Column(db.String(12), primary_key=True)
    renew_date = db.Column(db.DateTime, nullable=False)
    create_date = db.Column(db.DateTime, nullable=False)
    operate_cd = db.Column(db.String(128), nullable=False)
    c_flag = db.Column(db.String(1))
    send_zip = db.Column(db.String(7), nullable=False)
    send_todohuken = db.Column(db.String(8), nullable=False)
    send_addr1 = db.Column(db.String(40))
    send_addr2 = db.Column(db.String(50))
    send_addr3 = db.Column(db.String(50))
    send_addr4 = db.Column(db.String(40))
    send_build_name = db.Column(db.String(80))
    send_name = db.Column(db.String(60), nullable=False)
    send_telno = db.Column(db.String(11), index=True)
    user_telno = db.Column(db.String(11), index=True)
    imei = db.Column(db.String(15))
    iccid = db.Column(db.String(19))
    msisdn = db.Column(db.String(11))
    em_cont_cd = db.Column(db.String(10))
    append_cancel_no = db.Column(db.String(4))
    em_note = db.Column(db.String(20))
    note1 = db.Column(db.String(100))


class EmDat(db.Model):
    __tablename__ = 'em_dat'

    ws_common_id = db.Column(db.String(20), primary_key=True)
    ws_common_renbn = db.Column(db.String(2), nullable=False)
    contract_no = db.Column(db.String(12), nullable=False)
    renew_date = db.Column(db.DateTime, nullable=False)
    create_date = db.Column(db.DateTime, nullable=False)
    operate_cd = db.Column(db.String(128), nullable=False)
    c_flag = db.Column(db.String(1))
    remark = db.Column(db.String(80))
    apply_date = db.Column(db.DateTime)
    apply_kind = db.Column(db.String(4), nullable=False)
    prog_status = db.Column(db.String(2), nullable=False)
    send_plan_date = db.Column(db.DateTime)
    send_date = db.Column(db.DateTime)
    send_flg = db.Column(db.String(1))
    isp_order_no = db.Column(db.String(14))
    item_cd = db.Column(db.String(10))
    item_num = db.Column(db.Numeric(4, 0))
    item_opt = db.Column(db.String(2))
    arrival_plan_date = db.Column(db.DateTime)
    arrival_plan_time = db.Column(db.String(1))
    em_campaign_cd = db.Column(db.String(6))
    ship_date = db.Column(db.DateTime)
    slip_no = db.Column(db.String(20))
    ship_decision_date = db.Column(db.DateTime)
    arrival_date = db.Column(db.DateTime)
    ship_comp_date = db.Column(db.DateTime)
    send_status = db.Column(db.String(2))


class Enduser(db.Model):
    __tablename__ = 'enduser'

    contbase_no = db.Column(db.String(10), primary_key=True)
    enduser_flag = db.Column(db.String(1))
    enduser_firstname = db.Column(db.String(20))
    enduser_firstname_k = db.Column(db.String(20))
    enduser_lastname = db.Column(db.String(50))
    enduser_lastname_k = db.Column(db.String(100))
    enduser_sex = db.Column(db.String(1))
    enduser_birth = db.Column(db.DateTime)
    enduser_addr_flag = db.Column(db.String(1))
    enduser_zip = db.Column(db.String(7))
    enduser_addr1 = db.Column(db.String(4))
    enduser_addr2 = db.Column(db.String(50))
    enduser_addr3 = db.Column(db.String(50))
    renew_date = db.Column(db.DateTime, nullable=False)
    create_date = db.Column(db.DateTime, nullable=False)
    operate_cd = db.Column(db.String(128), nullable=False)
    tid = db.Column(db.String(16))
    identified_date = db.Column(db.DateTime)


t_ex_acc_trans_err_cvs = db.Table(
    'ex_acc_trans_err_cvs',
    db.Column('ex_acc_trans_err_cvs_seq', db.Integer, nullable=False, server_default=db.FetchedValue()),
    db.Column('dmd_month', db.String(6), nullable=False),
    db.Column('dmdto_id', db.String(12), nullable=False),
    db.Column('create_date', db.DateTime, nullable=False),
    db.Column('renew_date', db.DateTime, nullable=False),
    db.Column('operate_cd', db.String(128), nullable=False),
    db.Column('trans_kind', db.String(1), nullable=False),
    db.Column('result_cd', db.String(1), nullable=False),
    db.Column('dmd_no', db.String(13)),
    db.Column('demand_kbn', db.String(2)),
    db.Column('dmd_valid_date', db.DateTime),
    db.Column('cvs_next_month_flag', db.String(1), nullable=False),
    db.Column('dmd_no_next_month', db.String(13)),
    db.Column('chg_dmd_kbn_flag', db.String(1), nullable=False),
    db.Column('reserved_dmd_kbn_flag', db.String(1), nullable=False),
    db.Index('idx_ex_acc_trans_err_cvs_key', 'dmd_month', 'dmdto_id')
)


t_ex_acca_dat = db.Table(
    'ex_acca_dat',
    db.Column('ex_acca_dat_seq', db.Integer, nullable=False, server_default=db.FetchedValue()),
    db.Column('ws_common_id', db.String(20), nullable=False, index=True),
    db.Column('ws_common_renbn', db.String(2)),
    db.Column('contract_no', db.String(12), nullable=False),
    db.Column('isp_order_no', db.String(20)),
    db.Column('apply_date', db.DateTime, nullable=False),
    db.Column('send_plan_date', db.DateTime),
    db.Column('send_date', db.DateTime),
    db.Column('apply_kind', db.String(4)),
    db.Column('prog_status', db.String(2)),
    db.Column('apply_brand', db.String(2)),
    db.Column('order_cd', db.String(3)),
    db.Column('order_no', db.String(10)),
    db.Column('acca_no', db.String(60)),
    db.Column('service_id', db.String(10)),
    db.Column('gc_name', db.String(200)),
    db.Column('line_name', db.String(60)),
    db.Column('install_cd', db.String(1)),
    db.Column('zip', db.String(8)),
    db.Column('todohuken', db.String(8)),
    db.Column('gun', db.String(30)),
    db.Column('ku', db.String(30)),
    db.Column('area', db.String(30)),
    db.Column('banchi', db.String(50)),
    db.Column('build_name', db.String(120)),
    db.Column('telno', db.String(13)),
    db.Column('toi_telno', db.String(13)),
    db.Column('email', db.String(90)),
    db.Column('service_kind', db.String(1)),
    db.Column('isdn_type', db.String(1)),
    db.Column('user_cd', db.String(1)),
    db.Column('isdn_change', db.String(1)),
    db.Column('cpe_provider', db.String(1)),
    db.Column('cpe_installer', db.String(1)),
    db.Column('cpe_kind', db.String(3)),
    db.Column('nw_kind', db.String(1)),
    db.Column('ntt_result', db.String(1)),
    db.Column('ntt_ng1', db.String(2)),
    db.Column('ntt_ng2', db.String(2)),
    db.Column('ntt_notes', db.String(1800)),
    db.Column('reason_cd', db.String(2)),
    db.Column('result_date', db.DateTime),
    db.Column('change_date', db.DateTime),
    db.Column('ntt_work_date', db.DateTime),
    db.Column('complete_date', db.DateTime),
    db.Column('notes', db.String(600)),
    db.Column('entry_cd', db.String(10)),
    db.Column('campaign_cd', db.String(15)),
    db.Column('agency_cd', db.String(12)),
    db.Column('create_date', db.DateTime, nullable=False),
    db.Column('renew_date', db.DateTime, nullable=False),
    db.Column('operate_cd', db.String(128), nullable=False),
    db.Column('c_flag', db.String(1)),
    db.Column('remark', db.String(80)),
    db.Column('owner_zip', db.String(8)),
    db.Column('owner_todohuken', db.String(8)),
    db.Column('owner_gun', db.String(30)),
    db.Column('owner_ku', db.String(30)),
    db.Column('owner_area', db.String(30)),
    db.Column('owner_banchi', db.String(50)),
    db.Column('owner_build_name', db.String(120)),
    db.Column('cert_telno', db.String(13))
)


t_ex_appli_send_dat = db.Table(
    'ex_appli_send_dat',
    db.Column('ex_appli_send_dat_seq', db.Integer, nullable=False, server_default=db.FetchedValue()),
    db.Column('send_no', db.String(20), nullable=False, index=True),
    db.Column('renew_date', db.DateTime, nullable=False),
    db.Column('create_date', db.DateTime, nullable=False),
    db.Column('operate_cd', db.String(128), nullable=False),
    db.Column('c_flag', db.String(1)),
    db.Column('remark', db.String(80)),
    db.Column('apply_date', db.DateTime, nullable=False),
    db.Column('customer_id', db.String(8)),
    db.Column('prog_status', db.String(2), nullable=False),
    db.Column('direct_operate_cd', db.String(128), nullable=False),
    db.Column('direct_date', db.DateTime),
    db.Column('ship_decision_date', db.DateTime),
    db.Column('slip_number', db.String(20)),
    db.Column('ship_result', db.String(16)),
    db.Column('send_name', db.String(72), nullable=False),
    db.Column('send_chgdept', db.String(100)),
    db.Column('send_chgpost', db.String(40)),
    db.Column('send_chgname', db.String(40)),
    db.Column('send_zip', db.String(7), nullable=False),
    db.Column('send_addr1', db.String(8), nullable=False),
    db.Column('send_addr2', db.String(100), nullable=False),
    db.Column('send_addr3', db.String(100)),
    db.Column('send_telno', db.String(11)),
    db.Column('memo', db.String(512)),
    db.Column('express_flg', db.String(1), nullable=False),
    db.Column('sign_kind', db.String(1)),
    db.Column('res_base', db.String(4)),
    db.Column('res_base_num', db.Numeric(2, 0)),
    db.Column('res_add1', db.String(4)),
    db.Column('res_add1_num', db.Numeric(2, 0)),
    db.Column('res_add2', db.String(4)),
    db.Column('res_add2_num', db.Numeric(2, 0)),
    db.Column('res_add3', db.String(4)),
    db.Column('res_add3_num', db.Numeric(2, 0)),
    db.Column('res_add4', db.String(4)),
    db.Column('res_add4_num', db.Numeric(2, 0))
)


t_ex_au_set_info = db.Table(
    'ex_au_set_info',
    db.Column('ex_au_set_info_seq', db.Integer, nullable=False, server_default=db.FetchedValue()),
    db.Column('contract_no', db.String(12), nullable=False, index=True),
    db.Column('isp_order_no', db.String(20), nullable=False),
    db.Column('renew_date', db.DateTime, nullable=False),
    db.Column('create_date', db.DateTime, nullable=False),
    db.Column('operate_cd', db.String(128), nullable=False),
    db.Column('c_flag', db.String(1)),
    db.Column('apply_date', db.DateTime, nullable=False),
    db.Column('auset_camp_status', db.String(2), nullable=False),
    db.Column('auset_camp_available', db.String(1), nullable=False),
    db.Column('auset_camp_ng_reason', db.String(1)),
    db.Column('auset_camp_disc', db.String(1), nullable=False),
    db.Column('au_cont_telno', db.String(11), nullable=False),
    db.Column('au_firstname_k', db.String(20)),
    db.Column('au_lastname_k', db.String(100), nullable=False),
    db.Column('au_cont_zip', db.String(7)),
    db.Column('au_cont_todohuken', db.String(8)),
    db.Column('au_cont_shiku', db.String(60)),
    db.Column('au_cont_area_chome_banchi', db.String(60)),
    db.Column('au_cont_build_name', db.String(100)),
    db.Column('auset_appy_available', db.String(1), nullable=False),
    db.Column('auset_appy_ng_reason', db.String(1)),
    db.Column('auset_appy_disc', db.String(1), nullable=False)
)


t_ex_bill_customer = db.Table(
    'ex_bill_customer',
    db.Column('bill_month', db.DateTime, nullable=False),
    db.Column('history', db.Numeric(22, 0), nullable=False),
    db.Column('customer_id', db.String(8), nullable=False),
    db.Column('creditor_cd', db.String(1), nullable=False),
    db.Column('creditor_subcd', db.String(3)),
    db.Column('sales_dmd_kbn', db.String(1)),
    db.Column('tax_percent', db.Numeric(4, 1), nullable=False),
    db.Column('taxable_total', db.Numeric(10, 0), nullable=False),
    db.Column('taxfree_total', db.Numeric(10, 0), nullable=False),
    db.Column('tax_total', db.Numeric(10, 0), nullable=False)
)


t_ex_bill_detail = db.Table(
    'ex_bill_detail',
    db.Column('create_date', db.DateTime, nullable=False),
    db.Column('renew_date', db.DateTime, nullable=False),
    db.Column('operate_cd', db.String(128), nullable=False),
    db.Column('c_flag', db.String(1)),
    db.Column('bill_month', db.DateTime, nullable=False),
    db.Column('history', db.Numeric(22, 0), nullable=False),
    db.Column('dmdto_id', db.String(12), nullable=False),
    db.Column('customer_id', db.String(8), nullable=False),
    db.Column('contract_no', db.String(12), nullable=False),
    db.Column('bill_detailno', db.Numeric(5, 0), nullable=False),
    db.Column('opt_contract_no', db.Numeric(10, 0)),
    db.Column('plan_cd', db.String(8)),
    db.Column('disc_type', db.String(2)),
    db.Column('disc_cd', db.String(3)),
    db.Column('bill_kbn_cd', db.String(2), nullable=False),
    db.Column('bill_start', db.DateTime, nullable=False),
    db.Column('bill_end', db.DateTime),
    db.Column('quantity', db.Numeric(19, 0)),
    db.Column('unit', db.String(10)),
    db.Column('unit_cost', db.Numeric(10, 4)),
    db.Column('tax_cost', db.Numeric(9, 0)),
    db.Column('account_id', db.String(64)),
    db.Column('adjust_renban', db.Numeric(9, 0)),
    db.Column('cost', db.Numeric(9, 0), nullable=False),
    db.Column('taxfree_kbn', db.String(1), nullable=False),
    db.Column('kihon_tuika_kbn', db.String(1)),
    db.Column('kddi_plan_cd', db.String(10)),
    db.Column('plan_name', db.String(128)),
    db.Column('creditor_cd', db.String(1), nullable=False),
    db.Column('ntt_plan_cd', db.String(10)),
    db.Column('creditor_subcd', db.String(3)),
    db.Column('sales_dmd_kbn', db.String(1)),
    db.Column('demand_count', db.Numeric(2, 0)),
    db.Column('jpayment_trade_no', db.String(64)),
    db.Column('tax_percent', db.Numeric(4, 1)),
    db.Index('idx_ex_bill_detail_key', 'dmdto_id', 'customer_id', 'contract_no', 'bill_detailno')
)


t_ex_bill_dmd = db.Table(
    'ex_bill_dmd',
    db.Column('bill_month', db.DateTime, nullable=False),
    db.Column('history', db.Numeric(22, 0), nullable=False),
    db.Column('dmdto_id', db.String(12), nullable=False),
    db.Column('creditor_cd', db.String(1), nullable=False),
    db.Column('creditor_subcd', db.String(3)),
    db.Column('sales_dmd_kbn', db.String(1)),
    db.Column('use_aim', db.Numeric(1, 0)),
    db.Column('stat_kbn', db.Numeric(1, 0)),
    db.Column('tax_percent', db.Numeric(4, 1), nullable=False),
    db.Column('taxable_total', db.Numeric(10, 0), nullable=False),
    db.Column('taxfree_total', db.Numeric(10, 0), nullable=False),
    db.Column('tax_total', db.Numeric(10, 0), nullable=False)
)


t_ex_cashback = db.Table(
    'ex_cashback',
    db.Column('ex_cashback_seq', db.Integer, nullable=False, server_default=db.FetchedValue()),
    db.Column('cashback_no', db.Numeric(10, 0), nullable=False, index=True),
    db.Column('master_kbn', db.String(1), nullable=False),
    db.Column('work_kbn', db.String(2), nullable=False),
    db.Column('customer_id', db.String(8), nullable=False, index=True),
    db.Column('policy_no', db.String(10)),
    db.Column('cashback_cost', db.Numeric(10, 0)),
    db.Column('cashback_status', db.String(3)),
    db.Column('order_date', db.DateTime),
    db.Column('create_date', db.DateTime, nullable=False),
    db.Column('renew_date', db.DateTime, nullable=False),
    db.Column('operate_cd', db.String(128), nullable=False),
    db.Column('cashback_lastname_k', db.String(200)),
    db.Column('cashback_firstname_k', db.String(200)),
    db.Column('cashback_email', db.String(128)),
    db.Column('order_plan_month', db.Date),
    db.Column('contract_no', db.String(12)),
    db.Column('opt_contract_no', db.Numeric(10, 0)),
    db.Column('cashback_method', db.String(1)),
    db.Column('prog_status', db.String(2)),
    db.Column('send_mail_date', db.DateTime)
)


t_ex_cashpo_dat = db.Table(
    'ex_cashpo_dat',
    db.Column('ex_cashpo_dat_seq', db.Integer, nullable=False, server_default=db.FetchedValue()),
    db.Column('cashpo_no', db.String(10), nullable=False, index=True),
    db.Column('epark_order_id', db.String(22), nullable=False),
    db.Column('contbase_no', db.String(10), nullable=False),
    db.Column('policy_no', db.String(10), nullable=False),
    db.Column('coop_kind', db.String(4), nullable=False),
    db.Column('coop_status', db.String(1)),
    db.Column('coop_nth_time', db.Numeric(2, 0)),
    db.Column('plan_coop_month', db.String(6)),
    db.Column('coop_date', db.Date),
    db.Column('plan_vest_date', db.Date),
    db.Column('create_date', db.DateTime, nullable=False),
    db.Column('renew_date', db.DateTime, nullable=False),
    db.Column('operate_cd', db.String(128), nullable=False)
)


t_ex_contract = db.Table(
    'ex_contract',
    db.Column('ex_contract_seq', db.Integer, nullable=False, server_default=db.FetchedValue()),
    db.Column('contract_no', db.String(12), nullable=False, index=True),
    db.Column('customer_id', db.String(8), nullable=False, index=True),
    db.Column('contbase_no', db.String(10), nullable=False),
    db.Column('cont_renbn', db.String(2), nullable=False),
    db.Column('plan_cd', db.String(8), nullable=False),
    db.Column('vc_no', db.String(10)),
    db.Column('order_status', db.String(2), nullable=False),
    db.Column('cont_apply_date', db.DateTime),
    db.Column('cont_start_date', db.DateTime),
    db.Column('cont_end_date', db.DateTime),
    db.Column('cont_cancel_date', db.DateTime),
    db.Column('cancel_status', db.String(2)),
    db.Column('cancel_apply_date', db.DateTime),
    db.Column('cancel_date', db.DateTime),
    db.Column('agency_cd', db.String(12)),
    db.Column('campaign_cd', db.String(15)),
    db.Column('flets_apply_id', db.String(14)),
    db.Column('create_date', db.DateTime, nullable=False),
    db.Column('renew_date', db.DateTime, nullable=False),
    db.Column('operate_cd', db.String(128), nullable=False),
    db.Column('c_flag', db.String(1)),
    db.Column('apply_status', db.String(2)),
    db.Column('unsuited_date', db.DateTime),
    db.Column('bill_start_date', db.DateTime),
    db.Column('apply_no', db.String(10)),
    db.Column('penalty_remission_month', db.Date),
    db.Column('cont_chgname', db.String(20)),
    db.Column('order_no', db.String(26)),
    db.Column('partner_channel', db.String(128)),
    db.Column('partner_info', db.String(1024)),
    db.Column('monthly_end_date', db.Date),
    db.Column('syonin_status', db.String(3)),
    db.Column('syonin_date', db.DateTime),
    db.Column('fraud_detect_event_id', db.String(47)),
    db.Column('fraud_detect_result', db.String(10))
)


t_ex_contract_opt = db.Table(
    'ex_contract_opt',
    db.Column('ex_contract_opt_seq', db.Integer, nullable=False, server_default=db.FetchedValue()),
    db.Column('opt_contract_no', db.Numeric(10, 0), nullable=False, index=True),
    db.Column('customer_id', db.String(8), nullable=False, index=True),
    db.Column('contbase_no', db.String(10), nullable=False),
    db.Column('plan_cd', db.String(8), nullable=False),
    db.Column('opt_status', db.String(2), nullable=False),
    db.Column('opt_apply_date', db.DateTime),
    db.Column('opt_start_date', db.DateTime),
    db.Column('opt_end_date', db.DateTime),
    db.Column('opt_cancel_status', db.String(2)),
    db.Column('opt_cancel_apply', db.DateTime),
    db.Column('opt_cancel_date', db.DateTime),
    db.Column('opt_agency_cd', db.String(12)),
    db.Column('opt_campaign_cd', db.String(15)),
    db.Column('opt_kbn_cd', db.String(2), nullable=False),
    db.Column('create_date', db.DateTime, nullable=False),
    db.Column('renew_date', db.DateTime, nullable=False),
    db.Column('operate_cd', db.String(128), nullable=False),
    db.Column('c_flag', db.String(1)),
    db.Column('apply_status', db.String(2)),
    db.Column('unsuited_date', db.DateTime),
    db.Column('penalty_end_date', db.DateTime),
    db.Column('partner_channel', db.String(128)),
    db.Column('partner_info', db.String(1024))
)


t_ex_customer = db.Table(
    'ex_customer',
    db.Column('ex_customer_seq', db.Integer, nullable=False, server_default=db.FetchedValue()),
    db.Column('custinfo_id', db.Numeric(10, 0), nullable=False, index=True),
    db.Column('old_custid', db.String(15)),
    db.Column('firstname', db.String(20)),
    db.Column('firstname_k', db.String(20)),
    db.Column('lastname', db.String(50), nullable=False),
    db.Column('lastname_k', db.String(100)),
    db.Column('cust_zip', db.String(7)),
    db.Column('cust_addr1', db.String(4), nullable=False),
    db.Column('cust_addr2', db.String(50), nullable=False),
    db.Column('cust_addr3', db.String(50)),
    db.Column('cust_addr1_k', db.String(6)),
    db.Column('cust_addr2_k', db.String(100)),
    db.Column('cust_addr3_k', db.String(100)),
    db.Column('cust_telno', db.String(11), nullable=False),
    db.Column('cust_faxno', db.String(11)),
    db.Column('cust_user_type', db.String(1), nullable=False),
    db.Column('cust_level', db.String(2)),
    db.Column('cust_fukushi', db.String(1)),
    db.Column('cust_chgdept', db.String(50)),
    db.Column('cust_chgpost', db.String(20)),
    db.Column('cust_chgname', db.String(20)),
    db.Column('cust_chgname_k', db.String(40)),
    db.Column('addr_defect_cre_date', db.DateTime),
    db.Column('addr_defect_off_date', db.DateTime),
    db.Column('create_date', db.DateTime, nullable=False),
    db.Column('renew_date', db.DateTime, nullable=False),
    db.Column('operate_cd', db.String(128), nullable=False),
    db.Column('c_flag', db.String(1)),
    db.Column('stockholder_cd', db.String(10)),
    db.Column('address_code', db.String(11)),
    db.Column('cust_banchi1', db.String(40)),
    db.Column('cust_banchi2', db.String(20)),
    db.Column('cust_banchi3', db.String(20)),
    db.Column('cust_sex', db.String(1)),
    db.Column('cust_birth', db.DateTime),
    db.Column('cust_job', db.String(2))
)


t_ex_customer_id_mng = db.Table(
    'ex_customer_id_mng',
    db.Column('ex_customer_id_mng_seq', db.Integer, nullable=False, server_default=db.FetchedValue()),
    db.Column('customer_id', db.String(8), nullable=False, index=True),
    db.Column('custinfo_id', db.Numeric(10, 0), nullable=False),
    db.Column('cust_password', db.String(32), nullable=False),
    db.Column('cust_status', db.String(1), nullable=False),
    db.Column('approval_date', db.DateTime),
    db.Column('pay_status', db.String(1), nullable=False),
    db.Column('pay_status_renew_date', db.DateTime),
    db.Column('dmdto_id', db.String(12), nullable=False),
    db.Column('dmd_method', db.String(1), nullable=False),
    db.Column('apply_type', db.String(1), nullable=False),
    db.Column('member_kind', db.String(1), nullable=False),
    db.Column('cust_apply_date', db.DateTime),
    db.Column('cust_start_date', db.DateTime),
    db.Column('cust_end_apply_date', db.DateTime),
    db.Column('cust_cancel_date', db.DateTime),
    db.Column('cust_end_date', db.DateTime),
    db.Column('cust_email', db.String(128)),
    db.Column('create_date', db.DateTime),
    db.Column('renew_date', db.DateTime, nullable=False),
    db.Column('operate_cd', db.String(128), nullable=False),
    db.Column('c_flag', db.String(1)),
    db.Column('cust_apply_status', db.String(2)),
    db.Column('old_isp', db.String(3)),
    db.Column('non_volume_discount', db.String(1))
)


t_ex_customer_reserve = db.Table(
    'ex_customer_reserve',
    db.Column('ex_customer_reserve_seq', db.Integer, nullable=False, server_default=db.FetchedValue()),
    db.Column('customer_id', db.String(8), nullable=False, index=True),
    db.Column('change_status', db.String(1), nullable=False),
    db.Column('change_date', db.DateTime, nullable=False),
    db.Column('cust_zip', db.String(7), nullable=False),
    db.Column('cust_addr1', db.String(4), nullable=False),
    db.Column('cust_addr2', db.String(50), nullable=False),
    db.Column('cust_addr3', db.String(50)),
    db.Column('cust_telno', db.String(11), nullable=False),
    db.Column('create_date', db.DateTime, nullable=False),
    db.Column('renew_date', db.DateTime, nullable=False),
    db.Column('operate_cd', db.String(128), nullable=False)
)


t_ex_demandto = db.Table(
    'ex_demandto',
    db.Column('ex_demandto_seq', db.Integer, nullable=False, server_default=db.FetchedValue()),
    db.Column('dmdto_id', db.String(12), nullable=False),
    db.Column('valid_date', db.DateTime, nullable=False),
    db.Column('valid_flag', db.String(1)),
    db.Column('pwd_kbn', db.String(1)),
    db.Column('dmdto_status', db.String(2)),
    db.Column('ng_rsn', db.String(3)),
    db.Column('pay_chg_rsn', db.String(2)),
    db.Column('account_ask_no', db.String(20)),
    db.Column('demand_kbn', db.String(2), nullable=False),
    db.Column('detail_kbn', db.String(2), nullable=False),
    db.Column('detail_rsn', db.String(255)),
    db.Column('pwd_demandprint_kbn', db.String(1), nullable=False),
    db.Column('old_dmdto_cd', db.String(15)),
    db.Column('cust_user_type', db.String(1), nullable=False),
    db.Column('dmd_firstname', db.String(20)),
    db.Column('dmd_firstname_k', db.String(20)),
    db.Column('dmd_lastname', db.String(50)),
    db.Column('dmd_lastname_k', db.String(100)),
    db.Column('dmd_zip', db.String(7)),
    db.Column('dmd_addr1', db.String(4)),
    db.Column('dmd_addr2', db.String(50)),
    db.Column('dmd_addr3', db.String(50)),
    db.Column('dmd_addr1_k', db.String(6)),
    db.Column('dmd_addr2_k', db.String(100)),
    db.Column('dmd_addr3_k', db.String(100)),
    db.Column('dmd_telno', db.String(11)),
    db.Column('dmd_faxno', db.String(11)),
    db.Column('dmd_email', db.String(128)),
    db.Column('dmd_chgdept', db.String(50)),
    db.Column('dmd_chgtitle', db.String(20)),
    db.Column('dmd_chgname', db.String(20)),
    db.Column('dmd_chgname_k', db.String(40)),
    db.Column('cardkind', db.String(2)),
    db.Column('cardno', db.String(16)),
    db.Column('cardvalid', db.String(6)),
    db.Column('verify_no', db.String(8)),
    db.Column('verify_money', db.Numeric(8, 0)),
    db.Column('verify_date', db.DateTime),
    db.Column('agreement', db.String(1)),
    db.Column('pwd_stro_cd', db.String(1)),
    db.Column('trans_bankcd', db.String(4)),
    db.Column('trans_branchcd', db.String(3)),
    db.Column('trans_linecd', db.String(1)),
    db.Column('trans_acckind', db.String(1)),
    db.Column('trans_accno', db.String(7)),
    db.Column('trans_accname', db.String(60)),
    db.Column('kobetu_bankcd', db.String(4)),
    db.Column('kobetu_branchcd', db.String(3)),
    db.Column('kobetu_linecd', db.String(1)),
    db.Column('kobetu_acckind', db.String(1)),
    db.Column('kobetu_accno', db.String(7)),
    db.Column('kobetu_accname', db.String(60)),
    db.Column('dmdto_memo', db.String(128)),
    db.Column('end_date', db.DateTime),
    db.Column('addr_defect_cre_date', db.DateTime),
    db.Column('addr_defect_off_date', db.DateTime),
    db.Column('demand_renew_date', db.DateTime),
    db.Column('demand_operate_cd', db.String(128)),
    db.Column('payment_renew_date', db.DateTime),
    db.Column('payment_operate_cd', db.String(128)),
    db.Column('ol_new_user_trans_flag', db.String(1)),
    db.Column('create_date', db.DateTime, nullable=False),
    db.Column('renew_date', db.DateTime, nullable=False),
    db.Column('operate_cd', db.String(128), nullable=False),
    db.Column('c_flag', db.String(1)),
    db.Column('confirm_kbn', db.String(1)),
    db.Column('ntt_assentor_name', db.String(128)),
    db.Column('ntt_kbn', db.String(2)),
    db.Column('ntt_apply_date', db.DateTime),
    db.Column('ntt_user_tel_no', db.String(11)),
    db.Column('entrepreneur_cd', db.String(4)),
    db.Column('address_code', db.String(11)),
    db.Column('dmd_banchi1', db.String(40)),
    db.Column('dmd_banchi2', db.String(20)),
    db.Column('dmd_banchi3', db.String(20)),
    db.Column('yuso_ptn_cd', db.String(2)),
    db.Column('kddi_dmd_kbn', db.String(1)),
    db.Column('kddi_mng_no', db.Numeric(10, 0)),
    db.Column('ntt_id', db.String(12)),
    db.Column('ntt_name', db.String(128)),
    db.Column('ntt_name_k', db.String(256)),
    db.Column('change_possible_date', db.DateTime),
    db.Column('tabal_keep_branch', db.String(4)),
    db.Column('nttf_kind', db.String(1)),
    db.Index('idx_ex_demandto_key', 'dmdto_id', 'valid_date')
)


t_ex_device_change_dat = db.Table(
    'ex_device_change_dat',
    db.Column('ex_device_change_dat_seq', db.Integer, nullable=False, server_default=db.FetchedValue()),
    db.Column('ws_common_id', db.String(20), nullable=False, index=True),
    db.Column('ws_common_renbn', db.String(2), nullable=False),
    db.Column('contract_no', db.String(12), nullable=False, index=True),
    db.Column('opt_contract_no', db.Numeric(10, 0), nullable=False),
    db.Column('isp_order_no', db.String(16), nullable=False),
    db.Column('renew_date', db.DateTime, nullable=False),
    db.Column('create_date', db.DateTime, nullable=False),
    db.Column('operate_cd', db.String(128), nullable=False),
    db.Column('c_flag', db.String(1)),
    db.Column('send_plan_date', db.DateTime),
    db.Column('send_date', db.DateTime),
    db.Column('apply_date', db.DateTime),
    db.Column('apply_kind', db.String(4), nullable=False),
    db.Column('prog_status', db.String(2), nullable=False),
    db.Column('send_service_cd', db.String(8), nullable=False),
    db.Column('send_name_lastname', db.String(60), nullable=False),
    db.Column('send_name_firstname', db.String(60), nullable=False),
    db.Column('send_name_lastname_k', db.String(120)),
    db.Column('send_name_firstname_k', db.String(120)),
    db.Column('send_zip', db.String(7), nullable=False),
    db.Column('send_todohuken', db.String(8), nullable=False),
    db.Column('send_addr1', db.String(100), nullable=False),
    db.Column('send_addr2', db.String(100)),
    db.Column('send_build_name', db.String(80)),
    db.Column('send_telno', db.String(11)),
    db.Column('ship_no', db.String(20)),
    db.Column('ship_decision_date', db.DateTime),
    db.Column('ship_comp_date', db.DateTime),
    db.Column('ship_return_date', db.DateTime),
    db.Column('send_status', db.String(2)),
    db.Column('org_isp_order_no', db.String(20)),
    db.Column('cont_sex', db.String(1), nullable=False),
    db.Column('cont_birth', db.DateTime, nullable=False),
    db.Column('send_rent_device_cd', db.String(20), nullable=False),
    db.Column('send_rent_lost_opt_contract_no', db.Numeric(10, 0)),
    db.Column('send_rent_return_limit_date', db.DateTime),
    db.Column('send_rent_return_flg', db.String(1)),
    db.Column('send_rent_return_date', db.DateTime)
)


t_ex_device_cont = db.Table(
    'ex_device_cont',
    db.Column('ex_device_cont_seq', db.Integer, nullable=False, server_default=db.FetchedValue()),
    db.Column('imei', db.String(15), nullable=False, index=True),
    db.Column('isp_order_no', db.String(16), nullable=False),
    db.Column('contbase_no', db.String(10), nullable=False),
    db.Column('opt_contract_no', db.Numeric(10, 0)),
    db.Column('renew_date', db.DateTime, nullable=False),
    db.Column('create_date', db.DateTime, nullable=False),
    db.Column('operate_cd', db.String(128), nullable=False),
    db.Column('c_flag', db.String(1)),
    db.Column('work_kind', db.String(2), nullable=False),
    db.Column('rent_device_cd', db.String(20), nullable=False),
    db.Column('device_status', db.String(2))
)


t_ex_discount = db.Table(
    'ex_discount',
    db.Column('ex_discount_seq', db.Integer, nullable=False, server_default=db.FetchedValue()),
    db.Column('contract_no', db.String(12), nullable=False),
    db.Column('disc_renbn', db.Numeric(4, 0), nullable=False),
    db.Column('opt_contract_no', db.Numeric(10, 0), nullable=False),
    db.Column('disc_type', db.String(2), nullable=False),
    db.Column('disc_cd', db.String(3), nullable=False),
    db.Column('disc_start_date', db.DateTime),
    db.Column('disc_end_date', db.DateTime),
    db.Column('create_date', db.DateTime, nullable=False),
    db.Column('renew_date', db.DateTime, nullable=False),
    db.Column('operate_cd', db.String(128), nullable=False),
    db.Column('c_flag', db.String(1)),
    db.Column('disc_status', db.String(2)),
    db.Column('cancel_date', db.DateTime),
    db.Index('idx_ex_discount_key', 'contract_no', 'disc_renbn')
)


t_ex_discount_mst = db.Table(
    'ex_discount_mst',
    db.Column('ex_discount_mst_seq', db.Integer, nullable=False, server_default=db.FetchedValue()),
    db.Column('disc_type', db.String(2), nullable=False),
    db.Column('disc_cd', db.String(3), nullable=False),
    db.Column('disc_name', db.String(256)),
    db.Column('plan_cd', db.String(17)),
    db.Column('aitai_cd', db.String(13)),
    db.Column('disc_mst_init', db.Numeric(10, 0)),
    db.Column('disc_useal', db.Numeric(10, 0)),
    db.Column('disc_work', db.Numeric(10, 0)),
    db.Column('disc_term', db.Numeric(2, 0)),
    db.Column('open_term', db.DateTime),
    db.Column('disc_point', db.Numeric(10, 0)),
    db.Column('disc_memo', db.String(128)),
    db.Column('disc_start_date', db.DateTime),
    db.Column('disc_end_date', db.DateTime),
    db.Column('create_date', db.DateTime, nullable=False),
    db.Column('renew_date', db.DateTime, nullable=False),
    db.Column('operate_cd', db.String(128), nullable=False),
    db.Column('partner_cd', db.String(10)),
    db.Column('bfcampaign', db.String(64)),
    db.Column('disc_term_round', db.String(1)),
    db.Column('policy_no', db.String(10)),
    db.Column('campaign_cd', db.String(15)),
    db.Column('ntt_service_name', db.String(64)),
    db.Column('ntt_e_agency_cd', db.String(8)),
    db.Index('idx_ex_discount_mst_key', 'disc_type', 'disc_cd')
)


t_ex_dtisim_mst = db.Table(
    'ex_dtisim_mst',
    db.Column('ex_dtisim_mst_seq', db.Integer, nullable=False, server_default=db.FetchedValue()),
    db.Column('plan_cd', db.String(8), nullable=False, index=True),
    db.Column('pt2_plancd', db.String(32), nullable=False),
    db.Column('sim_type', db.String(1), nullable=False),
    db.Column('use_kbn', db.String(1)),
    db.Column('pt2_account_add_kbn', db.String(1), nullable=False),
    db.Column('plan_change_kbn', db.String(1), nullable=False),
    db.Column('pt2_plancd_after', db.String(32)),
    db.Column('create_date', db.DateTime, nullable=False),
    db.Column('renew_date', db.DateTime, nullable=False),
    db.Column('operate_cd', db.String(128), nullable=False)
)


t_ex_ea_dat = db.Table(
    'ex_ea_dat',
    db.Column('ex_ea_dat_seq', db.Integer, nullable=False, server_default=db.FetchedValue()),
    db.Column('ws_common_id', db.String(20), nullable=False, index=True),
    db.Column('ws_common_renbn', db.String(2)),
    db.Column('contract_no', db.String(12), nullable=False),
    db.Column('isp_order_no', db.String(20), nullable=False),
    db.Column('apply_date', db.DateTime),
    db.Column('send_plan_date', db.DateTime),
    db.Column('send_date', db.DateTime),
    db.Column('apply_kind', db.String(4)),
    db.Column('prog_status', db.String(2)),
    db.Column('web_no', db.String(10)),
    db.Column('user_cd', db.String(1)),
    db.Column('ea_cust_id', db.String(8)),
    db.Column('ea_contract_id', db.String(8)),
    db.Column('appli_cd', db.String(50)),
    db.Column('pw_cd', db.String(50)),
    db.Column('plan_cd', db.String(10)),
    db.Column('connect_type', db.String(1)),
    db.Column('modem_cd', db.String(1)),
    db.Column('work_cd', db.String(1)),
    db.Column('zip', db.String(8)),
    db.Column('todohuken', db.String(8)),
    db.Column('gun', db.String(40)),
    db.Column('ku', db.String(40)),
    db.Column('area', db.String(40)),
    db.Column('chome', db.String(10)),
    db.Column('banchi', db.String(40)),
    db.Column('build_name', db.String(150)),
    db.Column('contract_telno', db.String(13)),
    db.Column('telno', db.String(13)),
    db.Column('toi_telno', db.String(13)),
    db.Column('email', db.String(120)),
    db.Column('ntt_cd', db.String(50)),
    db.Column('line_kind', db.String(1)),
    db.Column('line_name', db.String(60)),
    db.Column('analog_cd', db.String(1)),
    db.Column('linechg_cd', db.String(1)),
    db.Column('facility_cd', db.String(1)),
    db.Column('linein_cd', db.String(1)),
    db.Column('result_date', db.DateTime),
    db.Column('ntt_result', db.String(1)),
    db.Column('ntt_ng_rsn', db.String(2)),
    db.Column('trans_status', db.String(4)),
    db.Column('bill_date', db.DateTime),
    db.Column('change_date', db.DateTime),
    db.Column('work_date', db.DateTime),
    db.Column('campaign_cd', db.String(15)),
    db.Column('agency_cd', db.String(12)),
    db.Column('create_date', db.DateTime, nullable=False),
    db.Column('renew_date', db.DateTime, nullable=False),
    db.Column('operate_cd', db.String(128), nullable=False),
    db.Column('c_flag', db.String(1)),
    db.Column('remark', db.String(80)),
    db.Column('acca_isp_order_no', db.String(20))
)


t_ex_em_cont = db.Table(
    'ex_em_cont',
    db.Column('ex_em_cont_seq', db.Integer, nullable=False, server_default=db.FetchedValue()),
    db.Column('contract_no', db.String(12), nullable=False, index=True),
    db.Column('renew_date', db.DateTime, nullable=False),
    db.Column('create_date', db.DateTime, nullable=False),
    db.Column('operate_cd', db.String(128), nullable=False),
    db.Column('c_flag', db.String(1)),
    db.Column('send_zip', db.String(7), nullable=False),
    db.Column('send_todohuken', db.String(8), nullable=False),
    db.Column('send_addr1', db.String(40)),
    db.Column('send_addr2', db.String(50)),
    db.Column('send_addr3', db.String(50)),
    db.Column('send_addr4', db.String(40)),
    db.Column('send_build_name', db.String(80)),
    db.Column('send_name', db.String(60), nullable=False),
    db.Column('send_telno', db.String(11)),
    db.Column('user_telno', db.String(11)),
    db.Column('imei', db.String(15)),
    db.Column('iccid', db.String(19)),
    db.Column('msisdn', db.String(11)),
    db.Column('em_cont_cd', db.String(10)),
    db.Column('append_cancel_no', db.String(4)),
    db.Column('em_note', db.String(20)),
    db.Column('note1', db.String(100))
)


t_ex_em_dat = db.Table(
    'ex_em_dat',
    db.Column('ex_em_dat_seq', db.Integer, nullable=False, server_default=db.FetchedValue()),
    db.Column('ws_common_id', db.String(20), nullable=False, index=True),
    db.Column('ws_common_renbn', db.String(2), nullable=False),
    db.Column('contract_no', db.String(12), nullable=False),
    db.Column('renew_date', db.DateTime, nullable=False),
    db.Column('create_date', db.DateTime, nullable=False),
    db.Column('operate_cd', db.String(128), nullable=False),
    db.Column('c_flag', db.String(1)),
    db.Column('remark', db.String(80)),
    db.Column('apply_date', db.DateTime),
    db.Column('apply_kind', db.String(4), nullable=False),
    db.Column('prog_status', db.String(2), nullable=False),
    db.Column('send_plan_date', db.DateTime),
    db.Column('send_date', db.DateTime),
    db.Column('send_flg', db.String(1)),
    db.Column('isp_order_no', db.String(14)),
    db.Column('item_cd', db.String(10)),
    db.Column('item_num', db.Numeric(4, 0)),
    db.Column('item_opt', db.String(2)),
    db.Column('arrival_plan_date', db.DateTime),
    db.Column('arrival_plan_time', db.String(1)),
    db.Column('em_campaign_cd', db.String(6)),
    db.Column('ship_date', db.DateTime),
    db.Column('slip_no', db.String(20)),
    db.Column('ship_decision_date', db.DateTime),
    db.Column('arrival_date', db.DateTime),
    db.Column('ship_comp_date', db.DateTime),
    db.Column('send_status', db.String(2))
)


t_ex_enduser = db.Table(
    'ex_enduser',
    db.Column('ex_enduser_seq', db.Integer, nullable=False, server_default=db.FetchedValue()),
    db.Column('contbase_no', db.String(10), nullable=False, index=True),
    db.Column('enduser_flag', db.String(1)),
    db.Column('enduser_firstname', db.String(20)),
    db.Column('enduser_firstname_k', db.String(20)),
    db.Column('enduser_lastname', db.String(50)),
    db.Column('enduser_lastname_k', db.String(100)),
    db.Column('enduser_sex', db.String(1)),
    db.Column('enduser_birth', db.DateTime),
    db.Column('enduser_addr_flag', db.String(1)),
    db.Column('enduser_zip', db.String(7)),
    db.Column('enduser_addr1', db.String(4)),
    db.Column('enduser_addr2', db.String(50)),
    db.Column('enduser_addr3', db.String(50)),
    db.Column('renew_date', db.DateTime, nullable=False),
    db.Column('create_date', db.DateTime, nullable=False),
    db.Column('operate_cd', db.String(128), nullable=False),
    db.Column('tid', db.String(16)),
    db.Column('identified_date', db.DateTime)
)


t_ex_goods_dat = db.Table(
    'ex_goods_dat',
    db.Column('ex_goods_dat_seq', db.Integer, nullable=False, server_default=db.FetchedValue()),
    db.Column('ws_common_id', db.String(20), nullable=False, index=True),
    db.Column('ws_common_renbn', db.String(2), nullable=False),
    db.Column('contract_no', db.String(12), nullable=False),
    db.Column('renew_date', db.DateTime, nullable=False),
    db.Column('create_date', db.DateTime, nullable=False),
    db.Column('operate_cd', db.String(128), nullable=False),
    db.Column('remark', db.String(80)),
    db.Column('apply_date', db.DateTime),
    db.Column('apply_kind', db.String(4), nullable=False),
    db.Column('prog_status', db.String(2), nullable=False),
    db.Column('send_plan_date', db.DateTime),
    db.Column('send_date', db.DateTime),
    db.Column('model_number', db.String(64), nullable=False),
    db.Column('order_no', db.String(16), nullable=False),
    db.Column('deliver_date', db.DateTime),
    db.Column('deliver_time', db.String(2)),
    db.Column('deliver_firstname', db.String(20)),
    db.Column('deliver_lastname', db.String(50), nullable=False),
    db.Column('deliver_chgdept', db.String(50)),
    db.Column('deliver_chgpost', db.String(20)),
    db.Column('deliver_chgname', db.String(20)),
    db.Column('deliver_zip', db.String(8), nullable=False),
    db.Column('deliver_todohuken', db.String(8), nullable=False),
    db.Column('deliver_gun', db.String(40)),
    db.Column('deliver_ku', db.String(40)),
    db.Column('deliver_area', db.String(40)),
    db.Column('deliver_chome', db.String(10)),
    db.Column('deliver_banchi', db.String(40)),
    db.Column('deliver_build_name', db.String(150)),
    db.Column('search_id', db.String(14)),
    db.Column('lot_cd', db.String(6)),
    db.Column('deliver_start_date', db.DateTime),
    db.Column('deliver_end_date', db.DateTime),
    db.Column('deliver_status', db.String(2))
)


t_ex_goods_remainder = db.Table(
    'ex_goods_remainder',
    db.Column('ex_goods_remainder_seq', db.Integer, nullable=False, server_default=db.FetchedValue()),
    db.Column('contract_no', db.String(12), nullable=False, index=True),
    db.Column('create_date', db.DateTime, nullable=False),
    db.Column('renew_date', db.DateTime, nullable=False),
    db.Column('operate_cd', db.String(128), nullable=False),
    db.Column('installment_cd', db.String(3), nullable=False),
    db.Column('order_no', db.String(16)),
    db.Column('start_month', db.Date),
    db.Column('end_plan_month', db.Date),
    db.Column('goods_cost', db.Numeric(8, 0)),
    db.Column('end_month', db.Date),
    db.Column('remaining_month', db.Date),
    db.Column('remaining_cost', db.Numeric(8, 0)),
    db.Column('demand_count', db.Numeric(2, 0), nullable=False, server_default=db.FetchedValue()),
    db.Column('demand_cost', db.Numeric(8, 0))
)


t_ex_hbm_dat = db.Table(
    'ex_hbm_dat',
    db.Column('ex_hbm_dat_seq', db.Integer, nullable=False, server_default=db.FetchedValue()),
    db.Column('ws_common_id', db.String(20), nullable=False, index=True),
    db.Column('ws_common_renbn', db.String(2), nullable=False),
    db.Column('contract_no', db.String(12), nullable=False),
    db.Column('opt_contract_no', db.Numeric(10, 0)),
    db.Column('isp_order_no', db.String(20), nullable=False),
    db.Column('renew_date', db.DateTime, nullable=False),
    db.Column('create_date', db.DateTime, nullable=False),
    db.Column('operate_cd', db.String(128), nullable=False),
    db.Column('c_flag', db.String(1)),
    db.Column('remark', db.String(80)),
    db.Column('apply_date', db.DateTime),
    db.Column('apply_kind', db.String(4), nullable=False),
    db.Column('prog_status', db.String(2), nullable=False),
    db.Column('send_plan_date', db.DateTime),
    db.Column('send_date', db.DateTime),
    db.Column('hbm_status', db.String(1)),
    db.Column('imei', db.String(15)),
    db.Column('iccid', db.String(19)),
    db.Column('msisdn', db.String(11)),
    db.Column('send_name', db.String(120), nullable=False),
    db.Column('send_zip', db.String(7), nullable=False),
    db.Column('send_todohuken', db.String(8), nullable=False),
    db.Column('send_addr1', db.String(100), nullable=False),
    db.Column('send_addr2', db.String(100)),
    db.Column('send_build_name', db.String(80)),
    db.Column('send_telno', db.String(11)),
    db.Column('arrival_plan_date', db.DateTime),
    db.Column('arrival_plan_time', db.String(1)),
    db.Column('ship_no', db.String(20)),
    db.Column('direct_date', db.DateTime),
    db.Column('ship_decision_date', db.DateTime),
    db.Column('ship_comp_date', db.DateTime),
    db.Column('send_status', db.String(2)),
    db.Column('item_cd', db.String(10)),
    db.Column('return_limit_date', db.DateTime),
    db.Column('return_flg', db.String(1)),
    db.Column('return_date', db.DateTime),
    db.Column('return_kit_reg_date', db.DateTime),
    db.Column('return_send_date', db.DateTime),
    db.Column('org_ws_common_id', db.String(20)),
    db.Column('sim_acct_stop_date', db.DateTime),
    db.Column('lost_opt_contract_no', db.Numeric(10, 0)),
    db.Column('user_name_k', db.String(100)),
    db.Column('user_sex', db.String(1)),
    db.Column('user_birth', db.DateTime),
    db.Column('device_cd', db.String(2)),
    db.Column('mnp_number', db.String(10)),
    db.Column('mnp_telno', db.String(11)),
    db.Column('mnp_expire_date', db.DateTime),
    db.Column('mnp_line_name', db.String(100)),
    db.Column('mnp_line_name_k', db.String(100)),
    db.Column('pt2_account_status', db.String(1)),
    db.Column('charge_date', db.DateTime),
    db.Column('portable_tel_flg', db.String(1)),
    db.Column('mnp_out_number', db.String(10)),
    db.Column('mnp_out_status', db.String(1)),
    db.Column('mnp_out_apply_date', db.DateTime),
    db.Column('mnp_out_order_date', db.DateTime),
    db.Column('mnp_out_order_comp_date', db.DateTime),
    db.Column('mnp_out_expire_date', db.DateTime),
    db.Column('mnp_out_end_date', db.DateTime),
    db.Column('mnp_out_line_lastname_k', db.String(80)),
    db.Column('mnp_out_line_firstname_k', db.String(40)),
    db.Column('mnp_out_line_lastname', db.String(40)),
    db.Column('mnp_out_line_firstname', db.String(20)),
    db.Column('mnp_out_line_birth', db.DateTime),
    db.Column('semiblack_add_status', db.String(1)),
    db.Column('semiblack_add_reserve_date', db.DateTime),
    db.Column('semiblack_add_apply_date', db.DateTime),
    db.Column('semiblack_add_comp_date', db.DateTime),
    db.Column('semiblack_add_error_msg', db.String(100)),
    db.Column('issue_error_msg', db.String(500)),
    db.Column('issue_touser_error_msg', db.String(500)),
    db.Column('notdelivered_date', db.DateTime),
    db.Column('tcard_issue', db.String(1)),
    db.Column('channel_flg', db.String(1)),
    db.Column('changevoice_flg', db.String(1)),
    db.Column('quota_carryover_date', db.DateTime),
    db.Column('pt2_flg', db.String(1)),
    db.Column('warranty_start_date', db.DateTime)
)


t_ex_icracked_cont = db.Table(
    'ex_icracked_cont',
    db.Column('ex_icracked_cont_seq', db.Integer, nullable=False, server_default=db.FetchedValue()),
    db.Column('imei', db.String(15), nullable=False),
    db.Column('contract_no', db.String(12), nullable=False),
    db.Column('opt_contract_no', db.Numeric(10, 0), nullable=False),
    db.Column('imei_create_date', db.Date),
    db.Column('service_start_date', db.Date),
    db.Column('repair_date', db.Date),
    db.Column('repair_content', db.String(2)),
    db.Column('renew_date', db.DateTime, nullable=False),
    db.Column('create_date', db.DateTime, nullable=False),
    db.Column('operate_cd', db.String(128), nullable=False),
    db.Column('c_flag', db.String(1)),
    db.Column('diff_flag', db.String(1)),
    db.Column('prog_status', db.String(2), nullable=False),
    db.Index('idx_ex_icracked_cont_key', 'imei', 'contract_no', 'opt_contract_no')
)


t_ex_installment_mst = db.Table(
    'ex_installment_mst',
    db.Column('ex_installment_mst_seq', db.Integer, nullable=False, server_default=db.FetchedValue()),
    db.Column('installment_cd', db.String(3), nullable=False, index=True),
    db.Column('create_date', db.DateTime, nullable=False),
    db.Column('renew_date', db.DateTime, nullable=False),
    db.Column('operate_cd', db.String(128), nullable=False),
    db.Column('plan_cd', db.String(8), nullable=False),
    db.Column('split_count', db.Numeric(2, 0), nullable=False),
    db.Column('first_cost', db.Numeric(8, 0), nullable=False),
    db.Column('regular_cost', db.Numeric(8, 0), nullable=False),
    db.Column('june_extra_cost', db.Numeric(8, 0), nullable=False),
    db.Column('december_extra_cost', db.Numeric(8, 0), nullable=False)
)


t_ex_kddi_cont = db.Table(
    'ex_kddi_cont',
    db.Column('ex_kddi_cont_seq', db.Integer, nullable=False, server_default=db.FetchedValue()),
    db.Column('contract_no', db.String(12), nullable=False),
    db.Column('kddi_mng_no', db.Numeric(10, 0), nullable=False, index=True),
    db.Column('renew_date', db.DateTime, nullable=False),
    db.Column('create_date', db.DateTime, nullable=False),
    db.Column('operate_cd', db.String(128), nullable=False),
    db.Column('c_flag', db.String(1)),
    db.Column('remark', db.String(80)),
    db.Column('kddi_cont_no', db.String(10)),
    db.Column('isp_order_no', db.String(20), nullable=False),
    db.Column('kddi_create_date', db.DateTime),
    db.Column('line_plan_date', db.DateTime),
    db.Column('line_start_date', db.DateTime),
    db.Column('tel_pre_service_num', db.Numeric(1, 0), nullable=False, server_default=db.FetchedValue()),
    db.Column('tel_service_num', db.Numeric(1, 0), nullable=False, server_default=db.FetchedValue()),
    db.Column('tv_pre_service_num', db.Numeric(1, 0), nullable=False, server_default=db.FetchedValue()),
    db.Column('tv_service_num', db.Numeric(1, 0), nullable=False, server_default=db.FetchedValue()),
    db.Column('kddi_use_end_date', db.DateTime),
    db.Column('kddi_cont_end_date', db.DateTime),
    db.Column('service_kind', db.String(1)),
    db.Column('service_state_flg', db.String(1)),
    db.Column('design_comp_date', db.DateTime),
    db.Column('outside_comp_date', db.DateTime),
    db.Column('work_stay_reason', db.String(120)),
    db.Column('provide_date', db.DateTime),
    db.Column('provide_flg', db.String(1)),
    db.Column('provide_ng_reason', db.String(120)),
    db.Column('work_plan_date', db.DateTime),
    db.Column('work_end_date', db.DateTime),
    db.Column('counting_start_month', db.Date)
)


t_ex_kddi_cont_opt = db.Table(
    'ex_kddi_cont_opt',
    db.Column('ex_kddi_cont_opt_seq', db.Integer, nullable=False, server_default=db.FetchedValue()),
    db.Column('kddi_cont_no', db.String(10), nullable=False),
    db.Column('service_cont_no', db.String(8), nullable=False),
    db.Column('renew_date', db.DateTime, nullable=False),
    db.Column('create_date', db.DateTime, nullable=False),
    db.Column('operate_cd', db.String(128), nullable=False),
    db.Column('c_flag', db.String(1)),
    db.Column('remark', db.String(80)),
    db.Column('service_kbn', db.String(1), nullable=False),
    db.Column('telno', db.String(11)),
    db.Column('portable_flg', db.String(1)),
    db.Column('portable_prog_flg', db.String(1)),
    db.Column('kddi_apply_date', db.DateTime),
    db.Column('bill_start_date', db.DateTime),
    db.Column('use_end_date', db.DateTime),
    db.Column('cont_end_date', db.DateTime),
    db.Column('talkie_flg', db.String(1)),
    db.Column('talkie_no', db.String(11)),
    db.Index('idx_ex_kddi_cont_opt_key', 'kddi_cont_no', 'service_cont_no')
)


t_ex_kddi_dat = db.Table(
    'ex_kddi_dat',
    db.Column('ex_kddi_dat_seq', db.Integer, nullable=False, server_default=db.FetchedValue()),
    db.Column('kddi_mng_no', db.Numeric(10, 0), nullable=False),
    db.Column('seq_no', db.Numeric(2, 0), nullable=False),
    db.Column('renew_date', db.DateTime, nullable=False),
    db.Column('create_date', db.DateTime, nullable=False),
    db.Column('operate_cd', db.String(128), nullable=False),
    db.Column('c_flag', db.String(1)),
    db.Column('remark', db.String(80)),
    db.Column('apply_date', db.DateTime),
    db.Column('service_kbn', db.String(1), nullable=False),
    db.Column('apply_kind', db.String(4), nullable=False),
    db.Column('prog_status', db.String(2)),
    db.Column('send_plan_date', db.DateTime),
    db.Column('send_date', db.DateTime),
    db.Column('cancel_plan_date', db.DateTime),
    db.Column('tel_no', db.String(11)),
    db.Column('ntt_return_kbn', db.String(1)),
    db.Column('tel_talkie_flg', db.String(1)),
    db.Column('tel_talkie_no', db.String(11)),
    db.Index('idx_ex_kddi_dat_key', 'kddi_mng_no', 'seq_no')
)


t_ex_kddi_dmd = db.Table(
    'ex_kddi_dmd',
    db.Column('ex_kddi_dmd_seq', db.Integer, nullable=False, server_default=db.FetchedValue()),
    db.Column('kddi_mng_no', db.Numeric(10, 0), nullable=False, index=True),
    db.Column('renew_date', db.DateTime, nullable=False),
    db.Column('create_date', db.DateTime, nullable=False),
    db.Column('operate_cd', db.String(128), nullable=False),
    db.Column('c_flag', db.String(1)),
    db.Column('remark', db.String(80)),
    db.Column('kddi_dmd_shift_flg', db.String(1)),
    db.Column('kddi_dmd_kind', db.String(1)),
    db.Column('au_cont_telno', db.String(11)),
    db.Column('au_cont_birth', db.DateTime),
    db.Column('au_cont_name', db.String(60)),
    db.Column('au_cont_name_k', db.String(60)),
    db.Column('au_cont_sign_flg', db.String(1)),
    db.Column('auonenet_cont_cd', db.String(10)),
    db.Column('auonenet_cont_name', db.String(60)),
    db.Column('auonenet_cont_name_k', db.String(60)),
    db.Column('auonenet_sign_flg', db.String(1)),
    db.Column('kotei_telno', db.String(10)),
    db.Column('kotei_cont_name', db.String(60)),
    db.Column('kotei_cont_name_k', db.String(60)),
    db.Column('kotei_sign_flg', db.String(1)),
    db.Column('kddi_dmd_name', db.String(60)),
    db.Column('kddi_dmd_name_k', db.String(60)),
    db.Column('kddi_dmd_sign_flg', db.String(1)),
    db.Column('kddi_pay_name', db.String(60)),
    db.Column('kddi_pay_name_k', db.String(60)),
    db.Column('pay_sign_flg', db.String(1)),
    db.Column('pledge_name_flg', db.String(1)),
    db.Column('apply_sign_flg', db.String(1)),
    db.Column('apply_pledge_flg', db.String(1)),
    db.Column('paper_bill_flg', db.String(1)),
    db.Column('kddi_payment_kbn', db.String(1)),
    db.Column('kddi_payment_shift_kbn', db.String(1)),
    db.Column('myline_acount', db.String(10)),
    db.Column('kddi_email_apply_flag', db.String(1)),
    db.Column('auonenet_email', db.String(129)),
    db.Column('kddi_dmd_result_kbn', db.String(1)),
    db.Column('kddi_dmd_method', db.String(1)),
    db.Column('kddi_dmd_first_month', db.String(6)),
    db.Column('kddi_dmd_error_cd', db.String(4)),
    db.Column('kddi_dmd_error_msg', db.String(200)),
    db.Column('kddi_dmd_receipt_date', db.DateTime),
    db.Column('kddi_claim_cont_cd', db.String(1)),
    db.Column('kddi_claim_close_reserve_cd', db.String(1)),
    db.Column('servicestop_file_date', db.DateTime)
)


t_ex_kddi_info = db.Table(
    'ex_kddi_info',
    db.Column('ex_kddi_info_seq', db.Integer, nullable=False, server_default=db.FetchedValue()),
    db.Column('kddi_mng_no', db.Numeric(10, 0), nullable=False, index=True),
    db.Column('renew_date', db.DateTime, nullable=False),
    db.Column('create_date', db.DateTime, nullable=False),
    db.Column('operate_cd', db.String(128), nullable=False),
    db.Column('c_flag', db.String(1)),
    db.Column('remark', db.String(80)),
    db.Column('kddi_order_no', db.String(10)),
    db.Column('kddi_jit_bumon_cd', db.String(4)),
    db.Column('kddi_tyoku_kbn', db.String(1)),
    db.Column('kddi_agency_cd', db.String(10)),
    db.Column('cont_zip', db.String(7)),
    db.Column('cont_todohuken', db.String(8)),
    db.Column('cont_shiku', db.String(60)),
    db.Column('cont_area_chome_banchi', db.String(60)),
    db.Column('cont_build_name', db.String(100)),
    db.Column('cont_telno1', db.String(11)),
    db.Column('cont_telno2', db.String(11)),
    db.Column('email', db.String(129)),
    db.Column('est_place_flg', db.String(1)),
    db.Column('est_zip', db.String(7)),
    db.Column('est_todohuken', db.String(8)),
    db.Column('est_shiku', db.String(60)),
    db.Column('est_area_chome_banchi', db.String(60)),
    db.Column('est_build_name', db.String(100)),
    db.Column('dest_place_flg', db.String(1)),
    db.Column('dest_name', db.String(60)),
    db.Column('dest_name_k', db.String(60)),
    db.Column('dest_zip', db.String(7)),
    db.Column('dest_todohuken', db.String(8)),
    db.Column('dest_shiku', db.String(60)),
    db.Column('dest_area_chome_banchi', db.String(60)),
    db.Column('dest_build_name', db.String(100)),
    db.Column('dest_telno', db.String(11)),
    db.Column('cont_group_no', db.String(10)),
    db.Column('article_no', db.String(8)),
    db.Column('ridge_id', db.String(2)),
    db.Column('room_no', db.String(5)),
    db.Column('modular_board_num', db.String(1)),
    db.Column('line1_no', db.String(11)),
    db.Column('line1_status', db.String(1)),
    db.Column('line2_no', db.String(11)),
    db.Column('line2_status', db.String(1)),
    db.Column('taxfree_user_cd', db.String(1)),
    db.Column('hikari_plus_tel_flg', db.String(1)),
    db.Column('portable_tel_flg', db.String(1)),
    db.Column('telno_050_flg', db.String(1)),
    db.Column('portable_tel', db.String(11)),
    db.Column('ntt_name', db.String(60)),
    db.Column('ntt_name_k', db.String(60)),
    db.Column('interrupt_call_flg', db.String(1)),
    db.Column('caller_id_display_flg', db.String(1)),
    db.Column('notice_telno_flg', db.String(1)),
    db.Column('nuisance_call_repulse_flg', db.String(1)),
    db.Column('caller_id_notice_flg', db.String(1)),
    db.Column('caller_id_notice_cd', db.String(1)),
    db.Column('detail_output_flg', db.String(1)),
    db.Column('number_guidance_flg', db.String(1)),
    db.Column('hellopage_flg', db.String(1)),
    db.Column('hikari_plus_tv_flg', db.String(1)),
    db.Column('stb_cd', db.String(4)),
    db.Column('filter_flg', db.String(1)),
    db.Column('filter_cd', db.String(4)),
    db.Column('kaketuke_support_flg', db.String(1)),
    db.Column('campain_apply_date', db.DateTime),
    db.Column('interrupt_number_flg', db.String(1)),
    db.Column('arrival_plan_date', db.DateTime),
    db.Column('dest_addr_change_flg', db.String(1)),
    db.Column('musen_lan_rental_cd', db.String(4)),
    db.Column('musen_lan_rental_num', db.String(2)),
    db.Column('add_hgw_cd', db.String(4)),
    db.Column('add_hgw_num', db.String(2)),
    db.Column('add_stb_cd', db.String(4)),
    db.Column('add_stb_num', db.String(2)),
    db.Column('entering_plan_date', db.DateTime),
    db.Column('redirect_call_flg', db.String(1)),
    db.Column('house_cd', db.String(1)),
    db.Column('possession_cd', db.String(1)),
    db.Column('isp_cd', db.String(3)),
    db.Column('incoming_notice_flg', db.String(1)),
    db.Column('au_term_telno1', db.String(11)),
    db.Column('au_term_telno2', db.String(11)),
    db.Column('au_term_telno3', db.String(11)),
    db.Column('ntt_line_cd', db.String(2)),
    db.Column('kddi_memo', db.String(16)),
    db.Column('same_0abj_telno', db.String(11)),
    db.Column('exist_line_flg', db.String(1)),
    db.Column('important_notice', db.String(100)),
    db.Column('ntt_zip', db.String(7)),
    db.Column('ntt_todohuken', db.String(8)),
    db.Column('ntt_shiku', db.String(60)),
    db.Column('ntt_area_chome_banchi', db.String(60)),
    db.Column('ntt_build_name', db.String(100)),
    db.Column('speed_kbn', db.String(1)),
    db.Column('musen_lan_rental_cd2', db.String(4)),
    db.Column('musen_lan_rental_num2', db.String(2)),
    db.Column('musen_lan_rental_cd3', db.String(4)),
    db.Column('musen_lan_rental_num3', db.String(2)),
    db.Column('musen_lan_rental_cd4', db.String(4)),
    db.Column('musen_lan_rental_num4', db.String(2)),
    db.Column('musen_lan_rental_cd5', db.String(4)),
    db.Column('musen_lan_rental_num5', db.String(2)),
    db.Column('work_date_id', db.String(10)),
    db.Column('monthly_item01', db.String(4)),
    db.Column('monthly_item02', db.String(4)),
    db.Column('monthly_item03', db.String(4)),
    db.Column('monthly_item04', db.String(4)),
    db.Column('monthly_item05', db.String(4)),
    db.Column('monthly_item06', db.String(4)),
    db.Column('monthly_item07', db.String(4)),
    db.Column('monthly_item08', db.String(4)),
    db.Column('monthly_item09', db.String(4)),
    db.Column('monthly_item10', db.String(4)),
    db.Column('monthly_item11', db.String(4)),
    db.Column('monthly_item12', db.String(4)),
    db.Column('pre_voip_co_cd', db.String(4)),
    db.Column('pre_voip_co_cd2', db.String(4)),
    db.Column('est_floors', db.String(3)),
    db.Column('cont_room_no', db.String(40)),
    db.Column('owner_name', db.String(60)),
    db.Column('owner_address', db.String(100)),
    db.Column('owner_telno', db.String(11)),
    db.Column('owner_kbn', db.String(1)),
    db.Column('est_telno', db.String(11)),
    db.Column('kddi3m_au_smart_val_cd', db.String(15)),
    db.Column('kddi3m_multi_campaign_kbn', db.String(1), server_default=db.FetchedValue()),
    db.Column('kddi3m_campaign_flg', db.String(1)),
    db.Column('kddi3m_applyprint_no', db.String(9))
)


t_ex_lf_cont = db.Table(
    'ex_lf_cont',
    db.Column('ex_lf_cont_seq', db.Integer, nullable=False, server_default=db.FetchedValue()),
    db.Column('contract_no', db.String(12), nullable=False),
    db.Column('opt_contract_no', db.Numeric(10, 0)),
    db.Column('isp_user_id', db.String(20), nullable=False, index=True),
    db.Column('renew_date', db.DateTime, nullable=False),
    db.Column('create_date', db.DateTime, nullable=False),
    db.Column('operate_cd', db.String(128), nullable=False),
    db.Column('remark', db.String(80)),
    db.Column('unext_id', db.String(10)),
    db.Column('license_key1', db.String(50)),
    db.Column('license_key2', db.String(50)),
    db.Column('license_key3', db.String(50)),
    db.Column('license_key4', db.String(50)),
    db.Column('license_key5', db.String(50)),
    db.Column('license_key6', db.String(50)),
    db.Column('license_key7', db.String(50)),
    db.Column('apply_request_date', db.Date),
    db.Column('apply_process_date', db.Date),
    db.Column('end_request_date', db.Date),
    db.Column('end_process_date', db.Date)
)


t_ex_lf_dat = db.Table(
    'ex_lf_dat',
    db.Column('ex_lf_dat_seq', db.Integer, nullable=False, server_default=db.FetchedValue()),
    db.Column('ws_common_id', db.String(20), nullable=False, index=True),
    db.Column('ws_common_renbn', db.String(2), nullable=False),
    db.Column('contract_no', db.String(12), nullable=False),
    db.Column('create_date', db.DateTime, nullable=False),
    db.Column('renew_date', db.DateTime, nullable=False),
    db.Column('operate_cd', db.String(128), nullable=False),
    db.Column('remark', db.String(80)),
    db.Column('apply_kind', db.String(4), nullable=False),
    db.Column('prog_status', db.String(2), nullable=False),
    db.Column('apply_date', db.DateTime, nullable=False),
    db.Column('send_plan_date', db.DateTime),
    db.Column('send_date', db.DateTime),
    db.Column('opt_contract_no', db.Numeric(10, 0)),
    db.Column('firstname', db.String(20)),
    db.Column('firstname_k', db.String(20)),
    db.Column('lastname', db.String(50)),
    db.Column('lastname_k', db.String(100)),
    db.Column('lf_sex', db.String(1)),
    db.Column('lf_birth', db.DateTime),
    db.Column('lf_telno', db.String(20)),
    db.Column('lf_mobile', db.String(20)),
    db.Column('lf_zip', db.String(7)),
    db.Column('lf_todohuken', db.String(4)),
    db.Column('lf_shiku_area_chome', db.String(50)),
    db.Column('lf_banchi', db.String(50)),
    db.Column('lf_build_name', db.String(40)),
    db.Column('lf_email', db.String(128)),
    db.Column('plan_type', db.String(1))
)


t_ex_lte_dat = db.Table(
    'ex_lte_dat',
    db.Column('ex_lte_dat_seq', db.Integer, nullable=False, server_default=db.FetchedValue()),
    db.Column('ws_common_id', db.String(20), nullable=False, index=True),
    db.Column('ws_common_renbn', db.String(2), nullable=False),
    db.Column('contract_no', db.String(12), nullable=False),
    db.Column('opt_contract_no', db.Numeric(10, 0)),
    db.Column('renew_date', db.DateTime, nullable=False),
    db.Column('create_date', db.DateTime, nullable=False),
    db.Column('operate_cd', db.String(128), nullable=False),
    db.Column('c_flag', db.String(1)),
    db.Column('remark', db.String(80)),
    db.Column('apply_date', db.DateTime),
    db.Column('apply_kind', db.String(4), nullable=False),
    db.Column('prog_status', db.String(2), nullable=False),
    db.Column('send_plan_date', db.DateTime),
    db.Column('send_date', db.DateTime),
    db.Column('lte_user_id', db.String(10), nullable=False),
    db.Column('imei', db.String(15)),
    db.Column('iccid', db.String(19)),
    db.Column('msisdn', db.String(11)),
    db.Column('lte_machin_meker', db.String(50)),
    db.Column('lte_machin_model', db.String(50)),
    db.Column('send_name', db.String(100), nullable=False),
    db.Column('send_name_kana', db.String(100), nullable=False),
    db.Column('send_zip', db.String(7), nullable=False),
    db.Column('send_todohuken', db.String(8), nullable=False),
    db.Column('send_addr1', db.String(40)),
    db.Column('send_addr2', db.String(50)),
    db.Column('send_addr3', db.String(50)),
    db.Column('send_addr4', db.String(40)),
    db.Column('send_build_name', db.String(80)),
    db.Column('send_telno', db.String(13)),
    db.Column('arrival_plan_date', db.DateTime),
    db.Column('arrival_plan_time', db.String(1)),
    db.Column('ship_no', db.String(20)),
    db.Column('direct_date', db.DateTime),
    db.Column('ship_plan_date', db.DateTime),
    db.Column('ship_decision_date', db.DateTime),
    db.Column('ship_comp_date', db.DateTime),
    db.Column('id_renbn', db.Numeric(2, 0), nullable=False)
)


t_ex_mopita_info = db.Table(
    'ex_mopita_info',
    db.Column('ex_mopita_info_seq', db.Integer, nullable=False, server_default=db.FetchedValue()),
    db.Column('contbase_no', db.String(10), nullable=False, index=True),
    db.Column('mopita_acct_id', db.String(12)),
    db.Column('mopita_status', db.String(2)),
    db.Column('mopita_pwd', db.String(7)),
    db.Column('mopita_reg_date', db.DateTime),
    db.Column('mopita_user_id', db.String(32)),
    db.Column('mopita_end_date', db.DateTime),
    db.Column('create_date', db.DateTime, nullable=False),
    db.Column('renew_date', db.DateTime, nullable=False),
    db.Column('operate_cd', db.String(128), nullable=False),
    db.Column('c_flag', db.String(1)),
    db.Column('mti_pin_cd', db.String(12))
)


t_ex_necat_dat = db.Table(
    'ex_necat_dat',
    db.Column('ex_necat_dat_seq', db.Integer, nullable=False, server_default=db.FetchedValue()),
    db.Column('ws_common_id', db.String(20), nullable=False, index=True),
    db.Column('ws_common_renbn', db.String(2), nullable=False),
    db.Column('contract_no', db.String(12), nullable=False),
    db.Column('opt_contract_no', db.Numeric(10, 0)),
    db.Column('isp_order_no', db.String(14), nullable=False),
    db.Column('status', db.String(1), nullable=False),
    db.Column('apply_kind', db.String(4)),
    db.Column('syori_status', db.String(2)),
    db.Column('syohin_cd', db.String(20)),
    db.Column('product_no', db.String(20)),
    db.Column('mac_address', db.String(12)),
    db.Column('invoice_no', db.String(20)),
    db.Column('plan_cd', db.String(10)),
    db.Column('zip', db.String(8)),
    db.Column('addr1', db.String(4)),
    db.Column('addr2', db.String(50)),
    db.Column('addr3', db.String(50)),
    db.Column('apply_date', db.DateTime),
    db.Column('send_plan_date', db.DateTime),
    db.Column('send_date', db.DateTime),
    db.Column('arrival_plan_date', db.DateTime),
    db.Column('arrival_plan_time', db.String(2)),
    db.Column('ship_date', db.DateTime),
    db.Column('arrival_date', db.DateTime),
    db.Column('arv_info_recv_date', db.DateTime),
    db.Column('arv_info_no', db.Numeric(2, 0)),
    db.Column('arv_ng_cd', db.String(2)),
    db.Column('cont_start_date', db.DateTime),
    db.Column('cont_end_date', db.DateTime),
    db.Column('iad_customer_id', db.String(30), nullable=False),
    db.Column('create_date', db.DateTime, nullable=False),
    db.Column('renew_date', db.DateTime, nullable=False),
    db.Column('operate_cd', db.String(128), nullable=False),
    db.Column('c_flag', db.String(1)),
    db.Column('remark', db.String(80))
)


t_ex_nicos_carddb = db.Table(
    'ex_nicos_carddb',
    db.Column('ex_nicos_carddb_seq', db.Integer, nullable=False, server_default=db.FetchedValue()),
    db.Column('card_mng_no', db.String(12), nullable=False),
    db.Column('recurring_id', db.String(15), nullable=False),
    db.Column('card_status', db.String(2)),
    db.Column('cardno', db.String(16)),
    db.Column('cardvalid', db.String(6)),
    db.Column('result_cd', db.String(3)),
    db.Column('create_date', db.DateTime, nullable=False),
    db.Column('renew_date', db.DateTime, nullable=False),
    db.Column('operate_cd', db.String(128), nullable=False),
    db.Index('idx_ex_nicos_carddb_key', 'card_mng_no', 'recurring_id')
)


t_ex_ntt_cor_add_cont = db.Table(
    'ex_ntt_cor_add_cont',
    db.Column('ex_ntt_cor_add_cont_seq', db.Integer, nullable=False, server_default=db.FetchedValue()),
    db.Column('contract_code', db.String(13), nullable=False),
    db.Column('add_contract_code', db.String(13)),
    db.Column('opt_contract_no', db.Numeric(10, 0), index=True),
    db.Column('ntt_ew_kind', db.String(1), nullable=False),
    db.Column('renew_date', db.DateTime, nullable=False),
    db.Column('create_date', db.DateTime, nullable=False),
    db.Column('operate_cd', db.String(128), nullable=False),
    db.Column('c_flag', db.String(1)),
    db.Column('service_kind', db.String(1), nullable=False),
    db.Column('service_name', db.String(90)),
    db.Column('order_class', db.String(4), nullable=False),
    db.Column('order_status', db.String(2)),
    db.Column('application_pername', db.String(90)),
    db.Column('contact_phone', db.String(90)),
    db.Column('applied_date', db.DateTime),
    db.Column('appoint_date', db.DateTime),
    db.Column('change_date', db.DateTime),
    db.Column('serv_start_day', db.DateTime),
    db.Column('serv_end_day', db.DateTime),
    db.Column('plan_name', db.String(128)),
    db.Column('operator_ent_name', db.String(40)),
    db.Column('operator_cor_branch_name', db.String(70)),
    db.Column('operator_cor_section_name', db.String(70)),
    db.Column('operator_cor_charge_name', db.String(128)),
    db.Column('operator_cor_phone', db.String(13)),
    db.Column('operator_cor_fax', db.String(13)),
    db.Column('sales_ent_name', db.String(40)),
    db.Column('sales_cor_branch_name', db.String(70)),
    db.Column('sales_cor_section_name', db.String(70)),
    db.Column('sales_cor_chargen_ame', db.String(128)),
    db.Column('sales_cor_phone', db.String(13)),
    db.Column('sales_cor_fax', db.String(13)),
    db.Column('date_renewed', db.DateTime),
    db.Column('add_phone_no', db.String(13)),
    db.Column('service_code', db.String(8)),
    db.Column('add_phone_kbn', db.String(1))
)


t_ex_ntt_cor_add_dat = db.Table(
    'ex_ntt_cor_add_dat',
    db.Column('ex_ntt_cor_add_dat_seq', db.Integer, nullable=False, server_default=db.FetchedValue()),
    db.Column('ws_common_id', db.String(20), nullable=False, index=True),
    db.Column('ws_common_renbn', db.String(2), nullable=False),
    db.Column('contract_code', db.String(13), nullable=False),
    db.Column('add_contract_code', db.String(13)),
    db.Column('create_date', db.DateTime, nullable=False),
    db.Column('renew_date', db.DateTime, nullable=False),
    db.Column('operate_cd', db.String(128), nullable=False),
    db.Column('c_flag', db.String(1)),
    db.Column('remark', db.String(80)),
    db.Column('apply_kind', db.String(4), nullable=False),
    db.Column('prog_status', db.String(2), nullable=False),
    db.Column('apply_date', db.DateTime, nullable=False),
    db.Column('send_plan_date', db.DateTime),
    db.Column('send_date', db.DateTime),
    db.Column('service_kbn', db.String(1)),
    db.Column('service_code', db.String(8)),
    db.Column('telno', db.String(13)),
    db.Column('opt_contract_no', db.Numeric(10, 0))
)


t_ex_ntt_cor_charge_dat = db.Table(
    'ex_ntt_cor_charge_dat',
    db.Column('ex_ntt_cor_charge_dat_seq', db.Integer, nullable=False, server_default=db.FetchedValue()),
    db.Column('contract_no', db.String(12), nullable=False),
    db.Column('renbn', db.String(3), nullable=False),
    db.Column('rating_name', db.String(64)),
    db.Column('price', db.Numeric(14, 4)),
    db.Column('count', db.Numeric(10, 0)),
    db.Column('renew_date', db.DateTime, nullable=False),
    db.Column('create_date', db.DateTime, nullable=False),
    db.Column('operate_cd', db.String(128), nullable=False),
    db.Column('c_flag', db.String(1)),
    db.Index('idx_ex_ntt_cor_charge_dat_key', 'contract_no', 'renbn')
)


t_ex_ntt_cor_cont = db.Table(
    'ex_ntt_cor_cont',
    db.Column('ex_ntt_cor_cont_seq', db.Integer, nullable=False, server_default=db.FetchedValue()),
    db.Column('contract_no', db.String(12), nullable=False, index=True),
    db.Column('isp_order_no', db.String(20)),
    db.Column('renew_date', db.DateTime, nullable=False),
    db.Column('create_date', db.DateTime, nullable=False),
    db.Column('operate_cd', db.String(128), nullable=False),
    db.Column('c_flag', db.String(1)),
    db.Column('business_name', db.String(3)),
    db.Column('contract_code', db.String(13)),
    db.Column('divert_consent_no', db.String(11)),
    db.Column('partner_code', db.String(18)),
    db.Column('service_name', db.String(50)),
    db.Column('service_item', db.String(256)),
    db.Column('so', db.String(4)),
    db.Column('so_stat', db.String(2)),
    db.Column('contractor_name', db.String(128)),
    db.Column('contractor_kname', db.String(256)),
    db.Column('cur_user_addr_code', db.String(802)),
    db.Column('applicationper_name', db.String(128)),
    db.Column('contact_phone', db.String(13)),
    db.Column('applied_date', db.DateTime),
    db.Column('appoint_date', db.DateTime),
    db.Column('change_date', db.DateTime),
    db.Column('business_contract_start_date', db.DateTime),
    db.Column('contract_end_date', db.DateTime),
    db.Column('flets_contract_start_date', db.DateTime),
    db.Column('ftv_trans_business_name', db.String(3)),
    db.Column('indoor_stem_wiring_div', db.String(64)),
    db.Column('ftv_business_cont_start_date', db.DateTime),
    db.Column('ftv_business_cont_end_date', db.DateTime),
    db.Column('regular_charge_div', db.String(8)),
    db.Column('service_change_code', db.String(13)),
    db.Column('operator_ent_name', db.String(40)),
    db.Column('operator_cor_branch_name', db.String(70)),
    db.Column('operator_cor_section_name', db.String(70)),
    db.Column('operator_cor_charge_name', db.String(128)),
    db.Column('operator_cor_phone', db.String(13)),
    db.Column('operator_cor_fax', db.String(13)),
    db.Column('sales_ent_name', db.String(40)),
    db.Column('sales_cor_branch_name', db.String(70)),
    db.Column('sales_cor_section_name', db.String(70)),
    db.Column('sales_cor_chargen_ame', db.String(80)),
    db.Column('sales_cor_phone', db.String(13)),
    db.Column('sales_cor_fax', db.String(12)),
    db.Column('accident_reason', db.String(256)),
    db.Column('accident_reason_sub', db.String(48)),
    db.Column('date_renewed', db.DateTime),
    db.Column('ritei_status', db.String(50)),
    db.Column('ritei_start_date', db.DateTime),
    db.Column('order_no', db.String(18)),
    db.Column('arena_so_no', db.String(20)),
    db.Column('access_key', db.String(8)),
    db.Column('survery_appoint_date', db.DateTime),
    db.Column('survery_appoint_time', db.String(256)),
    db.Column('appoint_am_pm', db.String(256)),
    db.Column('dispatch_div', db.String(256)),
    db.Column('aldivert_flg', db.String(1)),
    db.Column('vcast_business_name', db.String(30)),
    db.Column('ftvdivertflg', db.String(1)),
    db.Column('repflg', db.String(1)),
    db.Column('repbusinessname', db.String(3)),
    db.Column('repdivertflg', db.String(1)),
    db.Column('repbusinessstartdate', db.DateTime),
    db.Column('repbusinessenddate', db.DateTime),
    db.Column('terminal_item_list', db.Text),
    db.Column('charge_list', db.Text),
    db.Column('contact_hope_time_kbn', db.String(2))
)


t_ex_ntt_cor_dat = db.Table(
    'ex_ntt_cor_dat',
    db.Column('ex_ntt_cor_dat_seq', db.Integer, nullable=False, server_default=db.FetchedValue()),
    db.Column('ws_common_id', db.String(20), nullable=False, index=True),
    db.Column('ws_common_renbn', db.String(2), nullable=False),
    db.Column('contract_no', db.String(12), nullable=False, index=True),
    db.Column('renew_date', db.DateTime, nullable=False),
    db.Column('create_date', db.DateTime, nullable=False),
    db.Column('operate_cd', db.String(128), nullable=False),
    db.Column('c_flag', db.String(1)),
    db.Column('remark', db.String(80)),
    db.Column('apply_date', db.DateTime),
    db.Column('apply_kind', db.String(4), nullable=False),
    db.Column('prog_status', db.String(2), nullable=False),
    db.Column('send_plan_date', db.DateTime),
    db.Column('send_date', db.DateTime),
    db.Column('service_item', db.String(256)),
    db.Column('user_zip', db.String(7)),
    db.Column('user_addr', db.String(802)),
    db.Column('iten_plan_date', db.DateTime)
)


t_ex_ntt_cor_tmn_dat = db.Table(
    'ex_ntt_cor_tmn_dat',
    db.Column('ex_ntt_cor_tmn_dat_seq', db.Integer, nullable=False, server_default=db.FetchedValue()),
    db.Column('contract_no', db.String(12), nullable=False),
    db.Column('renbn', db.String(3), nullable=False),
    db.Column('terminal_name', db.String(128)),
    db.Column('install_date', db.DateTime),
    db.Column('renew_date', db.DateTime, nullable=False),
    db.Column('create_date', db.DateTime, nullable=False),
    db.Column('operate_cd', db.String(128), nullable=False),
    db.Column('c_flag', db.String(1)),
    db.Index('idx_ex_ntt_cor_tmn_dat_key', 'contract_no', 'renbn')
)


t_ex_ntt_dat = db.Table(
    'ex_ntt_dat',
    db.Column('ex_ntt_dat_seq', db.Integer, nullable=False, server_default=db.FetchedValue()),
    db.Column('ws_common_id', db.String(20), nullable=False, index=True),
    db.Column('ws_common_renbn', db.String(2), nullable=False),
    db.Column('contract_no', db.String(12), nullable=False),
    db.Column('renew_date', db.DateTime, nullable=False),
    db.Column('create_date', db.DateTime, nullable=False),
    db.Column('operate_cd', db.String(128), nullable=False),
    db.Column('c_flag', db.String(1)),
    db.Column('remark', db.String(80)),
    db.Column('apply_date', db.DateTime),
    db.Column('apply_kind', db.String(4), nullable=False),
    db.Column('prog_status', db.String(2), nullable=False),
    db.Column('send_plan_date', db.DateTime),
    db.Column('send_date', db.DateTime),
    db.Column('request_id', db.String(10)),
    db.Column('est_todohuken', db.String(20)),
    db.Column('apply_name', db.String(128)),
    db.Column('operator_name', db.String(128)),
    db.Column('work_plan_date', db.DateTime),
    db.Column('ntt_plan_date', db.DateTime),
    db.Column('ntt_plan_time', db.String(2)),
    db.Column('user_tel1', db.String(13)),
    db.Column('user_tel2', db.String(13)),
    db.Column('user_name', db.String(128)),
    db.Column('relation', db.String(20)),
    db.Column('origin_cd', db.String(2)),
    db.Column('note', db.String(256)),
    db.Column('cancel_flg', db.String(1)),
    db.Column('osm_end_plan_date', db.DateTime),
    db.Column('note2', db.String(16)),
    db.Column('result_cd', db.String(64)),
    db.Column('note3', db.String(256))
)


t_ex_ntt_info = db.Table(
    'ex_ntt_info',
    db.Column('ex_ntt_info_seq', db.Integer, nullable=False, server_default=db.FetchedValue()),
    db.Column('contract_no', db.String(12), nullable=False, index=True),
    db.Column('renew_date', db.DateTime, nullable=False),
    db.Column('create_date', db.DateTime, nullable=False),
    db.Column('operate_cd', db.String(128), nullable=False),
    db.Column('c_flag', db.String(1)),
    db.Column('remark', db.String(80)),
    db.Column('entry_root_cd', db.String(1), nullable=False),
    db.Column('method_cd', db.String(3)),
    db.Column('tran_mng_no', db.String(16)),
    db.Column('work_plan_date', db.DateTime),
    db.Column('work_plan_time', db.String(2)),
    db.Column('consal_plan_date', db.DateTime),
    db.Column('work_date_flg', db.String(1)),
    db.Column('telno', db.String(10)),
    db.Column('ntt_e_cont_id', db.String(16)),
    db.Column('cont_lastname', db.String(20)),
    db.Column('cont_firstname', db.String(20)),
    db.Column('cont_lastname_k', db.String(20)),
    db.Column('cont_firstname_k', db.String(20)),
    db.Column('apply_name', db.String(128)),
    db.Column('apply_name_k', db.String(256)),
    db.Column('apply_cd', db.String(1)),
    db.Column('contact_cd', db.String(1)),
    db.Column('telno2', db.String(11)),
    db.Column('email', db.String(50)),
    db.Column('a_cd', db.String(1)),
    db.Column('b_cd', db.String(1)),
    db.Column('c_cd', db.String(1)),
    db.Column('d_cd', db.String(1)),
    db.Column('note2', db.String(400)),
    db.Column('partner_cd', db.String(10)),
    db.Column('corp_name', db.String(60)),
    db.Column('corp_kana', db.String(60)),
    db.Column('corp_post_name', db.String(60)),
    db.Column('user_zip', db.String(7)),
    db.Column('user_todohuken', db.String(256)),
    db.Column('user_ku', db.String(256)),
    db.Column('user_area', db.String(256)),
    db.Column('user_chome', db.String(256)),
    db.Column('user_banchi', db.String(160)),
    db.Column('user_build_name', db.String(80)),
    db.Column('user_addr_note', db.String(200)),
    db.Column('send_zip', db.String(7)),
    db.Column('send_todohuken', db.String(256)),
    db.Column('send_ku', db.String(256)),
    db.Column('send_area', db.String(256)),
    db.Column('send_chome', db.String(256)),
    db.Column('send_banchi', db.String(160)),
    db.Column('send_build_name', db.String(80)),
    db.Column('send_addr_note', db.String(200)),
    db.Column('send_name', db.String(128)),
    db.Column('send_name_k', db.String(256)),
    db.Column('send_person', db.String(128)),
    db.Column('ntt_branch_name', db.String(64)),
    db.Column('ntt_position_name', db.String(128)),
    db.Column('ntt_sales_agency_cd', db.String(8)),
    db.Column('ntt_charge_name', db.String(128)),
    db.Column('ntt_charge_cd', db.String(8)),
    db.Column('ntt_charge_telno', db.String(13)),
    db.Column('ntt_charge_fax', db.String(13)),
    db.Column('ntt_charge_mail', db.String(60)),
    db.Column('ntt_isp_apply_kbn', db.String(20)),
    db.Column('ntt_service_name', db.String(64)),
    db.Column('ntt_bf_exist_type', db.String(4)),
    db.Column('ntt_isp_user_id', db.String(60)),
    db.Column('ntt_isp_mail', db.String(60)),
    db.Column('banpo_flg', db.String(1)),
    db.Column('double_contract_flag', db.String(64)),
    db.Column('name_admin_flag', db.String(64)),
    db.Column('cont_address_code', db.String(15)),
    db.Column('cont_address_revision', db.String(10)),
    db.Column('fax', db.String(13)),
    db.Column('address_code', db.String(11)),
    db.Column('partner_serial_no', db.String(16)),
    db.Column('user_banchi1', db.String(40)),
    db.Column('user_banchi2', db.String(20)),
    db.Column('user_banchi3', db.String(20)),
    db.Column('work_witness_name', db.String(20)),
    db.Column('work_witness_contact_cd', db.String(1)),
    db.Column('work_witness_telno', db.String(11)),
    db.Column('use_access_line', db.String(1)),
    db.Column('use_ntt_flets_service', db.String(3)),
    db.Column('other_companies_contract', db.String(1)),
    db.Column('other_companies_service', db.String(1)),
    db.Column('interior_wiring_cd', db.String(1)),
    db.Column('wiring_work_cd', db.String(1)),
    db.Column('tel_directory_carry_cd', db.String(1)),
    db.Column('vcast_contractor_sex_type', db.String(1)),
    db.Column('vcast_contractor_birth', db.DateTime),
    db.Column('connect_tv_const', db.String(1)),
    db.Column('tv_set_construct_type', db.String(1)),
    db.Column('cs_channel_pack1', db.String(1)),
    db.Column('cs_digital_tuner1', db.String(1)),
    db.Column('cs_channel_pack2', db.String(1)),
    db.Column('cs_digital_tuner2', db.String(1)),
    db.Column('cs_channel_pack3', db.String(1)),
    db.Column('cs_digital_tuner3', db.String(1)),
    db.Column('possession_cd', db.String(1)),
    db.Column('number_of_house', db.String(1)),
    db.Column('house_cd', db.String(1)),
    db.Column('work_witness_cd', db.String(1)),
    db.Column('ipv6connectmethod', db.String(64)),
    db.Column('adapterinfo', db.String(64)),
    db.Column('fm_possession_cd', db.String(1)),
    db.Column('ntt_birth', db.DateTime),
    db.Column('ntt_sex_type', db.String(1))
)


t_ex_ntt_item_dat = db.Table(
    'ex_ntt_item_dat',
    db.Column('ex_ntt_item_dat_seq', db.Integer, nullable=False, server_default=db.FetchedValue()),
    db.Column('contract_no', db.String(12), nullable=False),
    db.Column('item_no', db.String(2), nullable=False),
    db.Column('renew_date', db.DateTime, nullable=False),
    db.Column('create_date', db.DateTime, nullable=False),
    db.Column('operate_cd', db.String(128), nullable=False),
    db.Column('c_flag', db.String(1)),
    db.Column('apply_flg', db.String(1), nullable=False),
    db.Index('idx_ex_ntt_item_dat_key', 'contract_no', 'item_no')
)


t_ex_ntt_osmdb = db.Table(
    'ex_ntt_osmdb',
    db.Column('ex_ntt_osmdb_seq', db.Integer, nullable=False, server_default=db.FetchedValue()),
    db.Column('contract_no', db.String(12), nullable=False, index=True),
    db.Column('isp_order_no', db.String(16)),
    db.Column('renew_date', db.DateTime, nullable=False),
    db.Column('create_date', db.DateTime, nullable=False),
    db.Column('operate_cd', db.String(128), nullable=False),
    db.Column('c_flag', db.String(1)),
    db.Column('ntt_e_cont_id', db.String(16)),
    db.Column('apply_name', db.String(128)),
    db.Column('telno', db.String(14)),
    db.Column('osm_apply_date', db.DateTime),
    db.Column('item_name', db.String(128)),
    db.Column('item_detail_name', db.String(32)),
    db.Column('item_term_name', db.String(50)),
    db.Column('work_plan_date', db.DateTime),
    db.Column('work_plan_time', db.String(40)),
    db.Column('osm_entry_cd', db.String(10)),
    db.Column('osm_status', db.String(5)),
    db.Column('osm_sub_status', db.String(5)),
    db.Column('osm_start_date', db.DateTime),
    db.Column('osm_end_yyyymm', db.DateTime),
    db.Column('branch_name', db.String(20)),
    db.Column('mainte_plan', db.String(16)),
    db.Column('model_name', db.String(512)),
    db.Column('model_num', db.String(128)),
    db.Column('partner_cd', db.String(10)),
    db.Column('osm_create_date', db.DateTime),
    db.Column('branch_telno', db.String(14)),
    db.Column('consal_plan_date', db.DateTime),
    db.Column('ntt_e_agency_cd', db.String(8)),
    db.Column('sales_store_name', db.String(128)),
    db.Column('section_name', db.String(128)),
    db.Column('charge_cd', db.String(8)),
    db.Column('charge_name', db.String(128)),
    db.Column('osm_renew_date', db.DateTime),
    db.Column('change_item_name', db.String(128)),
    db.Column('application_no', db.String(16)),
    db.Column('ntt_e_cont_start_date', db.DateTime),
    db.Column('outside_bill_start_date', db.DateTime),
    db.Column('inside_bill_start_date', db.DateTime),
    db.Column('outside_work_plan_date', db.DateTime),
    db.Column('inside_work_plan_date', db.DateTime),
    db.Column('accident_reason', db.String(256)),
    db.Column('accident_status', db.String(256)),
    db.Column('cancel_reason', db.String(256)),
    db.Column('mainte_info', db.String(128)),
    db.Column('campaign', db.String(64)),
    db.Column('bill_end_date', db.DateTime),
    db.Column('end_reason', db.String(256)),
    db.Column('osa_set_cd', db.String(2)),
    db.Column('osa_cancel_cd', db.String(256)),
    db.Column('change_item_detail_name', db.String(32)),
    db.Column('change_id_no', db.String(64)),
    db.Column('hgw_mainte_info', db.String(32)),
    db.Column('hgw_model_name', db.String(128)),
    db.Column('item_change_bill_date', db.DateTime),
    db.Column('mng_id', db.String(25)),
    db.Column('cp_start_date', db.DateTime),
    db.Column('cp_end_date', db.DateTime),
    db.Column('bill_start_date', db.DateTime),
    db.Column('consal_status', db.String(50)),
    db.Column('osm_flg', db.String(1)),
    db.Column('osm2_start_date', db.DateTime),
    db.Column('osm2_end_yyyymm', db.DateTime)
)


t_ex_nttplayer_cont = db.Table(
    'ex_nttplayer_cont',
    db.Column('ex_nttplayer_cont_seq', db.Integer, nullable=False, server_default=db.FetchedValue()),
    db.Column('contract_no', db.String(12), nullable=False, index=True),
    db.Column('isp_order_no', db.String(20)),
    db.Column('renew_date', db.DateTime, nullable=False),
    db.Column('create_date', db.DateTime, nullable=False),
    db.Column('operate_cd', db.String(128), nullable=False),
    db.Column('c_flag', db.String(1)),
    db.Column('service_name', db.String(40)),
    db.Column('item_name', db.String(128)),
    db.Column('order_status', db.String(40)),
    db.Column('work_plan_date', db.DateTime),
    db.Column('ntt_e_cont_id_pr', db.String(13)),
    db.Column('item_term_name', db.String(1536)),
    db.Column('apply_kbn', db.String(40)),
    db.Column('ntt_e_cont_id', db.String(13)),
    db.Column('divert_consent_no', db.String(11)),
    db.Column('ntt_ew_kind', db.String(40)),
    db.Column('nttplayer_cont_id', db.String(12)),
    db.Column('user_name', db.String(240)),
    db.Column('user_name_k', db.String(480)),
    db.Column('user_address', db.String(2142)),
    db.Column('isp_name', db.String(60)),
    db.Column('isp_status', db.String(2)),
    db.Column('nttplayer_start_end_date', db.DateTime),
    db.Column('isp_start_end_date', db.DateTime),
    db.Column('nttplayer_cont_name', db.String(60)),
    db.Column('nttplayer_cont_name_k', db.String(100)),
    db.Column('nttplayer_cont_telno', db.String(72)),
    db.Column('nttplayer_cont_telno2', db.String(11)),
    db.Column('nttplayer_cont_zip', db.String(7)),
    db.Column('nttplayer_cont_address', db.String(200)),
    db.Column('nttplayer_cont_birth', db.DateTime),
    db.Column('penalty_cost_flag', db.String(2)),
    db.Column('flets_cont_name', db.String(480)),
    db.Column('flets_cont_telno', db.String(72))
)


t_ex_nttplayer_dat = db.Table(
    'ex_nttplayer_dat',
    db.Column('ex_nttplayer_dat_seq', db.Integer, nullable=False, server_default=db.FetchedValue()),
    db.Column('ws_common_id', db.String(20), nullable=False, index=True),
    db.Column('ws_common_renbn', db.String(2), nullable=False),
    db.Column('contract_no', db.String(12), nullable=False, index=True),
    db.Column('renew_date', db.DateTime, nullable=False),
    db.Column('create_date', db.DateTime, nullable=False),
    db.Column('operate_cd', db.String(128), nullable=False),
    db.Column('c_flag', db.String(1)),
    db.Column('remark', db.String(80)),
    db.Column('apply_date', db.DateTime),
    db.Column('apply_kind', db.String(4), nullable=False),
    db.Column('prog_status', db.String(2), nullable=False),
    db.Column('send_plan_date', db.DateTime),
    db.Column('send_date', db.DateTime),
    db.Column('nttplayer_order_no', db.String(17), nullable=False),
    db.Column('isp_receipt_result', db.String(2)),
    db.Column('isp_receipt_err_cd', db.String(2)),
    db.Column('isp_receipt_err_reason', db.String(1536)),
    db.Column('isp_service_order_status', db.String(2)),
    db.Column('stop_reason', db.String(1536)),
    db.Column('isp_biko', db.String(2)),
    db.Column('isp_confirm_date', db.DateTime)
)


t_ex_plan_mst = db.Table(
    'ex_plan_mst',
    db.Column('ex_plan_mst_seq', db.Integer, nullable=False, server_default=db.FetchedValue()),
    db.Column('plan_cd', db.String(8), nullable=False, index=True),
    db.Column('plan_name', db.String(128), nullable=False),
    db.Column('plan_short', db.String(128)),
    db.Column('plan_kind', db.String(1), nullable=False),
    db.Column('plan_status', db.String(1), nullable=False),
    db.Column('initial_cost', db.Numeric(8, 0)),
    db.Column('first_service_cost', db.Numeric(8, 0)),
    db.Column('service_cost', db.Numeric(8, 0)),
    db.Column('work_cost', db.Numeric(8, 0)),
    db.Column('taxfree_kbn', db.String(1), nullable=False),
    db.Column('dialup', db.String(4)),
    db.Column('roaming', db.String(4)),
    db.Column('mobilepoint', db.String(4)),
    db.Column('service_dmt_name', db.String(128)),
    db.Column('disc_mail_n', db.Numeric(2, 0), nullable=False, server_default=db.FetchedValue()),
    db.Column('disc_cd_mail', db.String(3)),
    db.Column('disc_cd_homepage', db.String(3)),
    db.Column('plan_term', db.Numeric(2, 0)),
    db.Column('create_date', db.DateTime, nullable=False),
    db.Column('renew_date', db.DateTime, nullable=False),
    db.Column('operate_cd', db.String(128), nullable=False),
    db.Column('c_flag', db.String(1)),
    db.Column('penalty_cost', db.Numeric(8, 0)),
    db.Column('max_penalty_month', db.Numeric(2, 0)),
    db.Column('service_cycle_month', db.Numeric(2, 0)),
    db.Column('creditor_cd', db.String(1), nullable=False, server_default=db.FetchedValue()),
    db.Column('creditor_subcd', db.String(3)),
    db.Column('penalty_taxfree_kbn', db.String(1), nullable=False, server_default=db.FetchedValue()),
    db.Column('volume_discount_cd', db.String(2)),
    db.Column('append_penalty_cost', db.Numeric(8, 0), nullable=False, server_default=db.FetchedValue()),
    db.Column('stat_initial_cost', db.Numeric(8, 0)),
    db.Column('stat_service_cost', db.Numeric(8, 0)),
    db.Column('aplus_initial_cost', db.Numeric(8, 0))
)


t_ex_prefix_dat = db.Table(
    'ex_prefix_dat',
    db.Column('ex_prefix_dat_seq', db.Integer, nullable=False, server_default=db.FetchedValue()),
    db.Column('ws_common_id', db.String(20), nullable=False, index=True),
    db.Column('ws_common_renbn', db.String(2), nullable=False),
    db.Column('opt_contract_no', db.Numeric(10, 0), nullable=False),
    db.Column('process_kbn', db.String(6), nullable=False),
    db.Column('msisdn', db.String(11)),
    db.Column('contbase_no', db.String(10), nullable=False),
    db.Column('exec_plan', db.String(1), nullable=False),
    db.Column('prefix_cd', db.String(20)),
    db.Column('apply_kind', db.String(4), nullable=False),
    db.Column('prog_status', db.String(2), nullable=False),
    db.Column('send_plan_date', db.DateTime),
    db.Column('send_date', db.DateTime),
    db.Column('result_cd', db.String(2)),
    db.Column('result_status', db.String(2)),
    db.Column('create_date', db.DateTime, nullable=False),
    db.Column('renew_date', db.DateTime, nullable=False),
    db.Column('operate_cd', db.String(128), nullable=False),
    db.Column('c_flag', db.String(1))
)


t_ex_privilege = db.Table(
    'ex_privilege',
    db.Column('ex_privilege_seq', db.Integer, nullable=False, server_default=db.FetchedValue()),
    db.Column('customer_id', db.String(8), nullable=False, index=True),
    db.Column('grant_date', db.DateTime, nullable=False),
    db.Column('stage', db.String(1), nullable=False),
    db.Column('used', db.String(1), nullable=False),
    db.Column('unchanged', db.String(1), nullable=False),
    db.Column('create_date', db.DateTime, nullable=False),
    db.Column('renew_date', db.DateTime, nullable=False),
    db.Column('operate_cd', db.String(128), nullable=False)
)


t_ex_pt2code_mst = db.Table(
    'ex_pt2code_mst',
    db.Column('ex_pt2code_mst_seq', db.Integer, nullable=False, server_default=db.FetchedValue()),
    db.Column('pt2_plancd', db.String(32), nullable=False, index=True),
    db.Column('quota_size', db.Numeric(10, 0), nullable=False),
    db.Column('quota_carryforward_kbn', db.String(1), nullable=False),
    db.Column('apn', db.String(50), nullable=False),
    db.Column('monthly_charge_kbn', db.String(1), nullable=False),
    db.Column('create_date', db.DateTime, nullable=False),
    db.Column('renew_date', db.DateTime, nullable=False),
    db.Column('operate_cd', db.String(128), nullable=False)
)


t_ex_sales_total = db.Table(
    'ex_sales_total',
    db.Column('ex_sales_total_seq', db.Integer, nullable=False, server_default=db.FetchedValue()),
    db.Column('dmd_no', db.String(13), nullable=False, index=True),
    db.Column('dmd_month', db.String(6)),
    db.Column('dmdto_id', db.String(12)),
    db.Column('taxable_total', db.Numeric(10, 0)),
    db.Column('taxfree_total', db.Numeric(10, 0)),
    db.Column('tax', db.Numeric(10, 0)),
    db.Column('all_total', db.Numeric(10, 0)),
    db.Column('slip_kbn', db.String(1)),
    db.Column('dmd_no2', db.String(13)),
    db.Column('dmd_status', db.String(2)),
    db.Column('demand_kbn', db.String(2), nullable=False),
    db.Column('payment_kbn', db.String(2)),
    db.Column('payment_date', db.DateTime),
    db.Column('result_cd', db.String(2)),
    db.Column('receipt_sts', db.String(1)),
    db.Column('all_receive_mny', db.Numeric(10, 0)),
    db.Column('receive_mny', db.Numeric(10, 0)),
    db.Column('deficiency', db.Numeric(10, 0)),
    db.Column('detail_kbn', db.String(2), nullable=False),
    db.Column('detail_rsn', db.String(255)),
    db.Column('pwd_demandprint_kbn', db.String(1), nullable=False),
    db.Column('cardkind', db.String(2)),
    db.Column('cardno', db.String(16)),
    db.Column('cardvalid', db.String(6)),
    db.Column('verify_no', db.String(8)),
    db.Column('verify_money', db.Numeric(8, 0)),
    db.Column('verify_date', db.DateTime),
    db.Column('agreement', db.String(1)),
    db.Column('pwd_stro_cd', db.String(1)),
    db.Column('trans_bankcd', db.String(4)),
    db.Column('trans_branchcd', db.String(3)),
    db.Column('trans_linecd', db.String(1)),
    db.Column('trans_acckind', db.String(1)),
    db.Column('trans_accno', db.String(7)),
    db.Column('trans_accname', db.String(60)),
    db.Column('kobetu_bankcd', db.String(4)),
    db.Column('kobetu_branchcd', db.String(3)),
    db.Column('kobetu_linecd', db.String(1)),
    db.Column('kobetu_acckind', db.String(1)),
    db.Column('kobetu_accno', db.String(7)),
    db.Column('kobetu_accname', db.String(60)),
    db.Column('dmdto_memo', db.String(128)),
    db.Column('payment_memo', db.String(64)),
    db.Column('slip_reason', db.String(2)),
    db.Column('create_date', db.DateTime, nullable=False),
    db.Column('renew_date', db.DateTime, nullable=False),
    db.Column('operate_cd', db.String(128), nullable=False),
    db.Column('c_flag', db.String(1)),
    db.Column('kddi_taxable_total', db.Numeric(10, 0), server_default=db.FetchedValue()),
    db.Column('kddi_taxfree_total', db.Numeric(10, 0), server_default=db.FetchedValue()),
    db.Column('kddi_tax', db.Numeric(10, 0), server_default=db.FetchedValue()),
    db.Column('collection_taxable_total', db.Numeric(10, 0), server_default=db.FetchedValue()),
    db.Column('collection_taxin_total', db.Numeric(10, 0), server_default=db.FetchedValue()),
    db.Column('ntt_e_taxable_total', db.Numeric(10, 0), nullable=False, server_default=db.FetchedValue()),
    db.Column('ntt_e_taxfree_total', db.Numeric(10, 0), nullable=False, server_default=db.FetchedValue()),
    db.Column('ntt_e_tax_total', db.Numeric(10, 0), nullable=False, server_default=db.FetchedValue()),
    db.Column('ntt_limit_date', db.DateTime),
    db.Column('ntt_w_taxable_total', db.Numeric(10, 0), nullable=False, server_default=db.FetchedValue()),
    db.Column('ntt_w_taxfree_total', db.Numeric(10, 0), nullable=False, server_default=db.FetchedValue()),
    db.Column('ntt_w_tax_total', db.Numeric(10, 0), nullable=False, server_default=db.FetchedValue()),
    db.Column('cvs_service_stop_plan', db.DateTime),
    db.Column('cvs_change_date', db.DateTime),
    db.Column('cvs_payment_mny', db.Numeric(10, 0)),
    db.Column('cvs_payment_date', db.DateTime),
    db.Column('cvs_payment_cancel_date', db.DateTime),
    db.Column('other_taxable_total', db.Numeric(10, 0), nullable=False, server_default=db.FetchedValue()),
    db.Column('other_taxfree_total', db.Numeric(10, 0), nullable=False, server_default=db.FetchedValue()),
    db.Column('other_tax_total', db.Numeric(10, 0), nullable=False, server_default=db.FetchedValue()),
    db.Column('use_aim', db.Numeric(1, 0)),
    db.Column('ec_receipt_no', db.String(22)),
    db.Column('stat_kbn', db.Numeric(1, 0)),
    db.Index('idx_ex_sales_total_01', 'dmd_month', 'dmdto_id', 'result_cd')
)


t_ex_sales_total_df_ng_wk = db.Table(
    'ex_sales_total_df_ng_wk',
    db.Column('ex_sales_total_df_ng_wk_seq', db.Integer, nullable=False, server_default=db.FetchedValue()),
    db.Column('dmd_no', db.String(13), nullable=False, index=True),
    db.Column('dmd_month', db.String(6)),
    db.Column('dmdto_id', db.String(12)),
    db.Column('cst_no', db.String(20)),
    db.Column('all_total', db.Numeric(10, 0)),
    db.Column('dmd_status', db.String(2)),
    db.Column('send_kbn', db.String(2)),
    db.Column('result_cd', db.String(2)),
    db.Column('payment_date', db.DateTime),
    db.Column('cust_user_type', db.String(1), nullable=False),
    db.Column('cardno', db.String(16)),
    db.Column('trans_bankcd', db.String(4)),
    db.Column('trans_branchcd', db.String(3)),
    db.Column('trans_linecd', db.String(1)),
    db.Column('trans_acckind', db.String(1)),
    db.Column('trans_accno', db.String(7)),
    db.Column('trans_accname', db.String(60)),
    db.Column('new_cd', db.String(1)),
    db.Column('statuscd', db.String(1)),
    db.Column('description', db.String(100)),
    db.Column('dtrgetamn_before', db.Numeric(10, 0)),
    db.Column('create_date', db.DateTime, nullable=False),
    db.Column('renew_date', db.DateTime, nullable=False),
    db.Column('operate_cd', db.String(128), nullable=False)
)


t_ex_sales_total_df_wk = db.Table(
    'ex_sales_total_df_wk',
    db.Column('ex_sales_total_df_wk_seq', db.Integer, nullable=False, server_default=db.FetchedValue()),
    db.Column('dmd_no', db.String(13), nullable=False),
    db.Column('dmd_month', db.String(6)),
    db.Column('dmdto_id', db.String(12)),
    db.Column('cst_no', db.String(20)),
    db.Column('all_total', db.Numeric(10, 0)),
    db.Column('dmd_status', db.String(2)),
    db.Column('send_kbn', db.String(2)),
    db.Column('result_cd', db.String(2)),
    db.Column('payment_date', db.DateTime),
    db.Column('cust_user_type', db.String(1), nullable=False),
    db.Column('cardno', db.String(16)),
    db.Column('trans_bankcd', db.String(4)),
    db.Column('trans_branchcd', db.String(3)),
    db.Column('trans_linecd', db.String(1)),
    db.Column('trans_acckind', db.String(1)),
    db.Column('trans_accno', db.String(7)),
    db.Column('trans_accname', db.String(60)),
    db.Column('new_cd', db.String(1)),
    db.Column('statuscd', db.String(1)),
    db.Column('description', db.String(100)),
    db.Column('dtrgetamn_before', db.Numeric(10, 0)),
    db.Column('create_date', db.DateTime, nullable=False),
    db.Column('renew_date', db.DateTime, nullable=False),
    db.Column('operate_cd', db.String(128), nullable=False)
)


t_ex_service = db.Table(
    'ex_service',
    db.Column('ex_service_seq', db.Integer, nullable=False, server_default=db.FetchedValue()),
    db.Column('contbase_no', db.String(10), nullable=False),
    db.Column('idkind_no', db.String(1), nullable=False),
    db.Column('account_id', db.String(64), nullable=False),
    db.Column('initial_pass', db.String(16)),
    db.Column('create_date', db.DateTime, nullable=False),
    db.Column('renew_date', db.DateTime, nullable=False),
    db.Column('operate_cd', db.String(128), nullable=False),
    db.Column('c_flag', db.String(1)),
    db.Column('telno', db.String(11)),
    db.Index('idx_ex_service_key', 'contbase_no', 'idkind_no')
)


t_ex_sim_dat = db.Table(
    'ex_sim_dat',
    db.Column('ex_sim_dat_seq', db.Integer, nullable=False, server_default=db.FetchedValue()),
    db.Column('ws_common_id', db.String(20), nullable=False, index=True),
    db.Column('ws_common_renbn', db.String(2), nullable=False),
    db.Column('contract_no', db.String(12), nullable=False),
    db.Column('opt_contract_no', db.Numeric(10, 0)),
    db.Column('isp_order_no', db.String(20), nullable=False),
    db.Column('renew_date', db.DateTime, nullable=False),
    db.Column('create_date', db.DateTime, nullable=False),
    db.Column('operate_cd', db.String(128), nullable=False),
    db.Column('c_flag', db.String(1)),
    db.Column('remark', db.String(80)),
    db.Column('apply_date', db.DateTime),
    db.Column('apply_kind', db.String(4), nullable=False),
    db.Column('prog_status', db.String(2), nullable=False),
    db.Column('send_plan_date', db.DateTime),
    db.Column('send_date', db.DateTime),
    db.Column('sim_status', db.String(1)),
    db.Column('imei', db.String(15)),
    db.Column('iccid', db.String(19)),
    db.Column('msisdn', db.String(11)),
    db.Column('send_name', db.String(120)),
    db.Column('send_name_k', db.String(240)),
    db.Column('send_zip', db.String(7), nullable=False),
    db.Column('send_todohuken', db.String(8), nullable=False),
    db.Column('send_addr1', db.String(100), nullable=False),
    db.Column('send_addr2', db.String(100)),
    db.Column('send_build_name', db.String(80)),
    db.Column('send_telno', db.String(11)),
    db.Column('arrival_plan_date', db.DateTime),
    db.Column('arrival_plan_time', db.String(1)),
    db.Column('ship_no', db.String(20)),
    db.Column('direct_date', db.DateTime),
    db.Column('ship_decision_date', db.DateTime),
    db.Column('ship_comp_date', db.DateTime),
    db.Column('send_status', db.String(2)),
    db.Column('item_cd', db.String(10)),
    db.Column('return_limit_date', db.DateTime),
    db.Column('return_flg', db.String(1)),
    db.Column('return_date', db.DateTime),
    db.Column('return_kit_reg_date', db.DateTime),
    db.Column('return_send_date', db.DateTime),
    db.Column('org_ws_common_id', db.String(20)),
    db.Column('sim_acct_stop_date', db.DateTime),
    db.Column('lost_opt_contract_no', db.Numeric(10, 0)),
    db.Column('cont_sex', db.String(1)),
    db.Column('cont_birth', db.DateTime),
    db.Column('mnp_number', db.String(10)),
    db.Column('mnp_telno', db.String(11)),
    db.Column('mnp_reserve_date', db.DateTime),
    db.Column('mnp_line_lastname_k', db.String(80)),
    db.Column('mnp_line_firstname_k', db.String(40)),
    db.Column('mnp_line_lastname', db.String(40)),
    db.Column('mnp_line_firstname', db.String(20)),
    db.Column('mnp_line_birth', db.DateTime),
    db.Column('portable_tel_flg', db.String(1)),
    db.Column('send_name_lastname', db.String(60)),
    db.Column('send_name_firstname', db.String(60)),
    db.Column('send_name_lastname_k', db.String(120)),
    db.Column('send_name_firstname_k', db.String(120)),
    db.Column('mnp_out_number', db.String(10)),
    db.Column('mnp_out_status', db.String(1)),
    db.Column('mnp_out_apply_date', db.DateTime),
    db.Column('mnp_out_order_date', db.DateTime),
    db.Column('mnp_out_order_comp_date', db.DateTime),
    db.Column('mnp_out_expire_date', db.DateTime),
    db.Column('mnp_out_end_date', db.DateTime),
    db.Column('mnp_out_line_lastname_k', db.String(80)),
    db.Column('mnp_out_line_firstname_k', db.String(40)),
    db.Column('mnp_out_line_lastname', db.String(40)),
    db.Column('mnp_out_line_firstname', db.String(20)),
    db.Column('mnp_out_line_birth', db.DateTime),
    db.Column('charge_count', db.Numeric(10, 0)),
    db.Column('charge_mb', db.Numeric(10, 0)),
    db.Column('charge_date', db.DateTime),
    db.Column('quota_code', db.String(128)),
    db.Column('semiblack_add_status', db.String(1)),
    db.Column('semiblack_add_reserve_date', db.DateTime),
    db.Column('semiblack_add_apply_date', db.DateTime),
    db.Column('semiblack_add_comp_date', db.DateTime),
    db.Column('semiblack_add_error_msg', db.String(100)),
    db.Column('quota_carryover_mb', db.Numeric(10, 0)),
    db.Column('quota_carryover_date', db.DateTime),
    db.Column('rent_device_cd', db.String(20)),
    db.Column('rent_lost_opt_contract_no', db.Numeric(10, 0)),
    db.Column('rent_return_limit_date', db.DateTime),
    db.Column('rent_return_flg', db.String(1)),
    db.Column('rent_return_date', db.DateTime)
)


t_ex_tepco_dat = db.Table(
    'ex_tepco_dat',
    db.Column('ex_tepco_dat_seq', db.Integer, nullable=False, server_default=db.FetchedValue()),
    db.Column('ws_common_id', db.String(20), nullable=False, index=True),
    db.Column('ws_common_renbn', db.String(2)),
    db.Column('contract_no', db.String(12)),
    db.Column('isp_order_no', db.String(20), nullable=False),
    db.Column('apply_date', db.DateTime, nullable=False),
    db.Column('send_plan_date', db.DateTime),
    db.Column('send_date', db.DateTime),
    db.Column('apply_kind', db.String(4)),
    db.Column('prog_status', db.String(2)),
    db.Column('syori_kind', db.String(2)),
    db.Column('syori_status', db.String(1)),
    db.Column('username', db.String(32)),
    db.Column('domainname', db.String(32)),
    db.Column('tpc_no', db.String(14)),
    db.Column('user_cd', db.String(1)),
    db.Column('zip', db.String(8), nullable=False),
    db.Column('todohuken', db.String(8)),
    db.Column('gun', db.String(20)),
    db.Column('ku', db.String(20)),
    db.Column('area', db.String(40)),
    db.Column('chome', db.String(10)),
    db.Column('banchi', db.String(20)),
    db.Column('build_name', db.String(80)),
    db.Column('telno', db.String(13)),
    db.Column('toi_telno', db.String(13)),
    db.Column('email', db.String(80)),
    db.Column('house_cd1', db.String(1)),
    db.Column('house_cd2', db.String(1)),
    db.Column('house_cd22', db.String(1)),
    db.Column('lead_in', db.String(1)),
    db.Column('ftth_cd', db.String(1)),
    db.Column('house_floor', db.String(1)),
    db.Column('tpc_user_cd', db.String(1)),
    db.Column('line_cd', db.String(1)),
    db.Column('work_flag', db.String(2)),
    db.Column('tpc_service_cd', db.String(1)),
    db.Column('tpc_kari_date', db.DateTime),
    db.Column('tpc_date', db.DateTime),
    db.Column('start_date', db.DateTime),
    db.Column('closed_date', db.DateTime),
    db.Column('check_date', db.DateTime),
    db.Column('check_time', db.String(1)),
    db.Column('work_date', db.DateTime),
    db.Column('work_time', db.String(1)),
    db.Column('work_end_date', db.DateTime),
    db.Column('cash_cd', db.String(1)),
    db.Column('lump_sum', db.String(30)),
    db.Column('apart_cd', db.String(13)),
    db.Column('opt_flag', db.String(30)),
    db.Column('vdsl_model', db.String(8)),
    db.Column('voip_model', db.String(8)),
    db.Column('musen_model', db.String(8)),
    db.Column('tpc_result', db.String(3)),
    db.Column('tpc_details', db.String(160)),
    db.Column('isp_notes', db.String(160)),
    db.Column('tpc_notes', db.String(160)),
    db.Column('campaign_cd', db.String(15)),
    db.Column('agency_cd', db.String(12)),
    db.Column('create_date', db.DateTime, nullable=False),
    db.Column('renew_date', db.DateTime, nullable=False),
    db.Column('operate_cd', db.String(128), nullable=False),
    db.Column('c_flag', db.String(1)),
    db.Column('remark', db.String(80))
)


t_ex_tg_set_info = db.Table(
    'ex_tg_set_info',
    db.Column('ex_tg_set_info_seq', db.Integer, nullable=False, server_default=db.FetchedValue()),
    db.Column('contract_no', db.String(12), nullable=False, index=True),
    db.Column('isp_order_no', db.String(20), nullable=False),
    db.Column('renew_date', db.DateTime, nullable=False),
    db.Column('create_date', db.DateTime, nullable=False),
    db.Column('operate_cd', db.String(128), nullable=False),
    db.Column('c_flag', db.String(1)),
    db.Column('apply_date', db.DateTime, nullable=False),
    db.Column('tg_set_camp_status', db.String(2), nullable=False),
    db.Column('tg_set_appy_available', db.String(1)),
    db.Column('tg_set_appy_ng_reason', db.String(1)),
    db.Column('tg_set_appy_result_date', db.DateTime),
    db.Column('tg_cont_no', db.String(13)),
    db.Column('tg_set_cont_no', db.String(13)),
    db.Column('tg_toss_cont_no', db.Numeric(8, 0)),
    db.Column('tg_customer_name', db.String(142)),
    db.Column('tg_customer_kname', db.String(142)),
    db.Column('tg_cont_status_gas', db.String(40)),
    db.Column('tg_start_date_gas', db.DateTime),
    db.Column('tg_cont_status_electric', db.String(40)),
    db.Column('tg_start_date_electric', db.DateTime),
    db.Column('tg_set_camp_available', db.String(1)),
    db.Column('tg_set_camp_ng_reason', db.String(1)),
    db.Column('removal_flag', db.String(1)),
    db.Column('yobi01', db.String(100))
)


t_ex_tone_prefix_dat = db.Table(
    'ex_tone_prefix_dat',
    db.Column('ex_tone_prefix_dat_seq', db.Integer, nullable=False, server_default=db.FetchedValue()),
    db.Column('ws_common_id', db.String(20), nullable=False, index=True),
    db.Column('ws_common_renbn', db.String(2), nullable=False),
    db.Column('opt_contract_no', db.Numeric(10, 0), nullable=False),
    db.Column('process_kbn', db.String(6), nullable=False),
    db.Column('msisdn', db.String(11)),
    db.Column('contbase_no', db.String(10), nullable=False),
    db.Column('exec_plan', db.String(1), nullable=False),
    db.Column('prefix_cd', db.String(20)),
    db.Column('apply_kind', db.String(4), nullable=False),
    db.Column('prog_status', db.String(2), nullable=False),
    db.Column('send_plan_date', db.DateTime),
    db.Column('send_date', db.DateTime),
    db.Column('result_receive_date', db.DateTime),
    db.Column('result_cd', db.String(2)),
    db.Column('result_status', db.String(2)),
    db.Column('create_date', db.DateTime, nullable=False),
    db.Column('renew_date', db.DateTime, nullable=False),
    db.Column('operate_cd', db.String(128), nullable=False),
    db.Column('c_flag', db.String(1))
)


t_ex_uname_dat = db.Table(
    'ex_uname_dat',
    db.Column('ex_uname_dat_seq', db.Integer, nullable=False, server_default=db.FetchedValue()),
    db.Column('ws_common_id', db.String(20), nullable=False, index=True),
    db.Column('ws_common_renbn', db.Numeric(2, 0), nullable=False),
    db.Column('contract_no', db.String(12), nullable=False),
    db.Column('create_date', db.DateTime, nullable=False),
    db.Column('renew_date', db.DateTime, nullable=False),
    db.Column('operate_cd', db.String(128), nullable=False),
    db.Column('c_flag', db.String(1)),
    db.Column('remark', db.String(80)),
    db.Column('second_lv_domain', db.String(64), nullable=False),
    db.Column('top_lv_domain', db.String(3), nullable=False),
    db.Column('domain_status', db.Numeric(2, 0), nullable=False),
    db.Column('domain_start_date', db.DateTime, nullable=False),
    db.Column('domain_end_date', db.DateTime),
    db.Column('domain_exp_date', db.DateTime, nullable=False),
    db.Column('owner_j_last_name', db.String(50)),
    db.Column('owner_e_last_name', db.String(50)),
    db.Column('owner_j_first_name', db.String(50)),
    db.Column('owner_e_first_name', db.String(50)),
    db.Column('owner_user_type', db.String(1)),
    db.Column('owner_j_org_name', db.String(100)),
    db.Column('owner_e_org_name', db.String(100)),
    db.Column('owner_zip', db.String(16)),
    db.Column('owner_j_addr1', db.Numeric(2, 0)),
    db.Column('owner_e_addr1', db.String(20)),
    db.Column('owner_j_addr2', db.String(50)),
    db.Column('owner_e_addr2', db.String(50)),
    db.Column('owner_j_addr3', db.String(50)),
    db.Column('owner_e_addr3', db.String(50)),
    db.Column('owner_j_addr4', db.String(50)),
    db.Column('owner_e_addr4', db.String(50)),
    db.Column('owner_telno', db.String(20)),
    db.Column('owner_faxno', db.String(20)),
    db.Column('owner_email', db.String(100)),
    db.Column('admin_j_last_name', db.String(50)),
    db.Column('admin_e_last_name', db.String(50)),
    db.Column('admin_j_first_name', db.String(50)),
    db.Column('admin_e_first_name', db.String(50)),
    db.Column('admin_user_type', db.String(1)),
    db.Column('admin_j_org_name', db.String(100)),
    db.Column('admin_e_org_name', db.String(100)),
    db.Column('admin_zip', db.String(16)),
    db.Column('admin_j_addr1', db.Numeric(2, 0)),
    db.Column('admin_e_addr1', db.String(20)),
    db.Column('admin_j_addr2', db.String(50)),
    db.Column('admin_e_addr2', db.String(50)),
    db.Column('admin_j_addr3', db.String(50)),
    db.Column('admin_e_addr3', db.String(50)),
    db.Column('admin_j_addr4', db.String(50)),
    db.Column('admin_e_addr4', db.String(50)),
    db.Column('admin_telno', db.String(20)),
    db.Column('admin_faxno', db.String(20)),
    db.Column('admin_email', db.String(100)),
    db.Column('tech_j_last_name', db.String(50)),
    db.Column('tech_e_last_name', db.String(50)),
    db.Column('tech_j_first_name', db.String(50)),
    db.Column('tech_e_first_name', db.String(50)),
    db.Column('tech_user_type', db.String(1)),
    db.Column('tech_j_org_name', db.String(100)),
    db.Column('tech_e_org_name', db.String(100)),
    db.Column('tech_zip', db.String(16)),
    db.Column('tech_j_addr1', db.Numeric(2, 0)),
    db.Column('tech_e_addr1', db.String(20)),
    db.Column('tech_j_addr2', db.String(50)),
    db.Column('tech_e_addr2', db.String(50)),
    db.Column('tech_j_addr3', db.String(50)),
    db.Column('tech_e_addr3', db.String(50)),
    db.Column('tech_j_addr4', db.String(50)),
    db.Column('tech_e_addr4', db.String(50)),
    db.Column('tech_telno', db.String(20)),
    db.Column('tech_faxno', db.String(20)),
    db.Column('tech_email', db.String(100)),
    db.Column('acc_j_last_name', db.String(50)),
    db.Column('acc_e_last_name', db.String(50)),
    db.Column('acc_j_first_name', db.String(50)),
    db.Column('acc_e_first_name', db.String(50)),
    db.Column('acc_user_type', db.String(1)),
    db.Column('acc_j_org_name', db.String(100)),
    db.Column('acc_e_org_name', db.String(100)),
    db.Column('acc_zip', db.String(16)),
    db.Column('acc_j_addr1', db.Numeric(2, 0)),
    db.Column('acc_e_addr1', db.String(20)),
    db.Column('acc_j_addr2', db.String(50)),
    db.Column('acc_e_addr2', db.String(50)),
    db.Column('acc_j_addr3', db.String(50)),
    db.Column('acc_e_addr3', db.String(50)),
    db.Column('acc_j_addr4', db.String(50)),
    db.Column('acc_e_addr4', db.String(50)),
    db.Column('acc_telno', db.String(20)),
    db.Column('acc_faxno', db.String(20)),
    db.Column('acc_email', db.String(100)),
    db.Column('gmo_id', db.String(18)),
    db.Column('gmo_pass', db.String(18)),
    db.Column('release_apply_date', db.DateTime),
    db.Column('domain_pending_id', db.String(18))
)


t_ex_voip_c_dat = db.Table(
    'ex_voip_c_dat',
    db.Column('ex_voip_c_dat_seq', db.Integer, nullable=False, server_default=db.FetchedValue()),
    db.Column('ws_common_id', db.String(20), nullable=False, index=True),
    db.Column('ws_common_renbn', db.String(2)),
    db.Column('contract_no', db.String(12), nullable=False),
    db.Column('opt_contract_no', db.Numeric(10, 0)),
    db.Column('isp_order_no', db.String(20), nullable=False),
    db.Column('isp_opt_order_no', db.String(20)),
    db.Column('enduser_id', db.String(20)),
    db.Column('apply_date', db.DateTime),
    db.Column('send_plan_date', db.DateTime),
    db.Column('send_date', db.DateTime),
    db.Column('apply_kind', db.String(4)),
    db.Column('prog_status', db.String(2)),
    db.Column('apply_brand', db.String(2)),
    db.Column('order_no', db.String(10)),
    db.Column('acca_no', db.String(60)),
    db.Column('business_cd', db.String(2)),
    db.Column('action', db.String(2)),
    db.Column('option_kind', db.String(2)),
    db.Column('line_name', db.String(60)),
    db.Column('zip', db.String(8)),
    db.Column('todohuken', db.String(8)),
    db.Column('gun', db.String(30)),
    db.Column('ku', db.String(30)),
    db.Column('area', db.String(30)),
    db.Column('banchi', db.String(50)),
    db.Column('build_name', db.String(120)),
    db.Column('telno', db.String(13)),
    db.Column('toi_telno', db.String(13)),
    db.Column('email', db.String(90)),
    db.Column('cpe_provider', db.String(1)),
    db.Column('cpe_installer', db.String(1)),
    db.Column('cpe_kind', db.String(3)),
    db.Column('vo_user_id', db.String(40)),
    db.Column('vo_passwd', db.String(20)),
    db.Column('vo_telno', db.String(15)),
    db.Column('vo_server', db.String(50)),
    db.Column('vo_domain', db.String(50)),
    db.Column('isp_circuit_no', db.String(20)),
    db.Column('ntt_work_date', db.DateTime),
    db.Column('billing_date', db.DateTime),
    db.Column('change_date', db.DateTime),
    db.Column('cancel_date', db.DateTime),
    db.Column('agency_cd', db.String(12)),
    db.Column('create_date', db.DateTime, nullable=False),
    db.Column('renew_date', db.DateTime, nullable=False),
    db.Column('operate_cd', db.String(128), nullable=False),
    db.Column('c_flag', db.String(1)),
    db.Column('remark', db.String(80))
)


t_ex_voip_c_num_mst = db.Table(
    'ex_voip_c_num_mst',
    db.Column('ex_voip_c_num_mst_seq', db.Integer, nullable=False, server_default=db.FetchedValue()),
    db.Column('telno', db.String(13), nullable=False, index=True),
    db.Column('sip_user_id', db.String(40)),
    db.Column('sip_password', db.String(20)),
    db.Column('sip_server', db.String(50)),
    db.Column('status', db.String(1), nullable=False),
    db.Column('pr_order_line_date', db.DateTime),
    db.Column('start_date', db.DateTime),
    db.Column('end_date', db.DateTime),
    db.Column('create_date', db.DateTime, nullable=False),
    db.Column('renew_date', db.DateTime, nullable=False),
    db.Column('operate_cd', db.String(128), nullable=False)
)


t_ex_voip_f_dat = db.Table(
    'ex_voip_f_dat',
    db.Column('ex_voip_f_dat_seq', db.Integer, nullable=False, server_default=db.FetchedValue()),
    db.Column('ws_common_id', db.String(20), nullable=False, index=True),
    db.Column('ws_common_renbn', db.String(2)),
    db.Column('contract_no', db.String(12), nullable=False),
    db.Column('opt_contract_no', db.Numeric(10, 0)),
    db.Column('isp_portable_userid', db.String(12)),
    db.Column('isp_userid', db.String(15)),
    db.Column('isp_order_no', db.String(12), nullable=False),
    db.Column('apply_date', db.DateTime, nullable=False),
    db.Column('send_plan_date', db.DateTime),
    db.Column('send_date', db.DateTime),
    db.Column('apply_kind', db.String(4)),
    db.Column('prog_status', db.String(2)),
    db.Column('master_status', db.String(2)),
    db.Column('business_cd', db.String(2)),
    db.Column('telno_050', db.String(32)),
    db.Column('telno_0abj', db.String(32)),
    db.Column('portable_tel', db.String(15)),
    db.Column('portable_cd', db.String(1)),
    db.Column('account_050', db.String(32)),
    db.Column('password_050', db.String(32)),
    db.Column('password_0abj', db.String(32)),
    db.Column('ppp_name', db.String(128)),
    db.Column('rental_cd', db.String(1)),
    db.Column('iad_type', db.String(1)),
    db.Column('plan_cd', db.String(8)),
    db.Column('use_change_date', db.DateTime),
    db.Column('ip_start_date', db.DateTime),
    db.Column('ip_end_date', db.DateTime),
    db.Column('suspend_date', db.DateTime),
    db.Column('re_suspend_date', db.DateTime),
    db.Column('iad_status', db.String(1)),
    db.Column('dl_start_date', db.DateTime),
    db.Column('dl_term_date', db.DateTime),
    db.Column('dl_comp_date', db.DateTime),
    db.Column('dl_remind_no', db.Numeric(1, 0)),
    db.Column('start_0abj', db.DateTime),
    db.Column('end_0abj', db.DateTime),
    db.Column('portable_work_date', db.DateTime),
    db.Column('ftth_start_date', db.DateTime),
    db.Column('portable_date', db.DateTime),
    db.Column('portable_ng_cd', db.String(80)),
    db.Column('portable_ng', db.String(256)),
    db.Column('portable_remind_no', db.Numeric(1, 0)),
    db.Column('portable_ng_date', db.DateTime),
    db.Column('bill_flag', db.String(8)),
    db.Column('unnotify_ref_status', db.String(1)),
    db.Column('refusal_number_status', db.String(1)),
    db.Column('catch_status', db.String(1)),
    db.Column('portable_status', db.String(1)),
    db.Column('status_104', db.String(1)),
    db.Column('user_name', db.String(40)),
    db.Column('user_kana', db.String(72)),
    db.Column('zip', db.String(8)),
    db.Column('todohuken', db.String(8)),
    db.Column('gun', db.String(50)),
    db.Column('ku', db.String(40)),
    db.Column('area', db.String(40)),
    db.Column('chome', db.String(10)),
    db.Column('banchi', db.String(40)),
    db.Column('build_name', db.String(126)),
    db.Column('ntt_name', db.String(90)),
    db.Column('ntt_kana', db.String(180)),
    db.Column('ntt_zip', db.String(8)),
    db.Column('ntt_todohuken', db.String(8)),
    db.Column('ntt_gun', db.String(40)),
    db.Column('ntt_ku', db.String(40)),
    db.Column('ntt_area', db.String(40)),
    db.Column('ntt_chome', db.String(10)),
    db.Column('ntt_banchi', db.String(40)),
    db.Column('ntt_build_name', db.String(80)),
    db.Column('toi_telno', db.String(13)),
    db.Column('direct_name', db.String(128)),
    db.Column('direct_kana', db.String(240)),
    db.Column('direct_zip', db.String(8)),
    db.Column('direct_todohuken', db.String(8)),
    db.Column('direct_gun', db.String(40)),
    db.Column('direct_ku', db.String(40)),
    db.Column('direct_area', db.String(40)),
    db.Column('direct_chome', db.String(10)),
    db.Column('direct_banchi', db.String(40)),
    db.Column('direct_build_name', db.String(80)),
    db.Column('build_kind', db.String(1)),
    db.Column('user_cd', db.String(1)),
    db.Column('note1', db.String(32)),
    db.Column('note2', db.String(256)),
    db.Column('campaign_cd', db.String(15)),
    db.Column('agency_cd', db.String(12)),
    db.Column('mansion_id', db.String(13)),
    db.Column('sip_server_address', db.String(50)),
    db.Column('create_date', db.DateTime, nullable=False),
    db.Column('renew_date', db.DateTime, nullable=False),
    db.Column('operate_cd', db.String(128), nullable=False),
    db.Column('c_flag', db.String(1)),
    db.Column('no_return_kbn', db.String(1)),
    db.Column('entry_cd', db.String(13)),
    db.Column('remark', db.String(80))
)


t_ex_voip_f_ref_telno_info = db.Table(
    'ex_voip_f_ref_telno_info',
    db.Column('ex_voip_f_ref_telno_info_seq', db.Integer, nullable=False, server_default=db.FetchedValue()),
    db.Column('ip_telno', db.String(11), nullable=False, index=True),
    db.Column('ref_telno_01', db.String(11)),
    db.Column('ref_telno_02', db.String(11)),
    db.Column('ref_telno_03', db.String(11)),
    db.Column('ref_telno_04', db.String(11)),
    db.Column('ref_telno_05', db.String(11)),
    db.Column('ref_telno_06', db.String(11)),
    db.Column('ref_telno_07', db.String(11)),
    db.Column('ref_telno_08', db.String(11)),
    db.Column('ref_telno_09', db.String(11)),
    db.Column('ref_telno_10', db.String(11)),
    db.Column('ref_telno_11', db.String(11)),
    db.Column('ref_telno_12', db.String(11)),
    db.Column('ref_telno_13', db.String(11)),
    db.Column('ref_telno_14', db.String(11)),
    db.Column('ref_telno_15', db.String(11)),
    db.Column('ref_telno_16', db.String(11)),
    db.Column('ref_telno_17', db.String(11)),
    db.Column('ref_telno_18', db.String(11)),
    db.Column('ref_telno_19', db.String(11)),
    db.Column('ref_telno_20', db.String(11)),
    db.Column('ref_telno_21', db.String(11)),
    db.Column('ref_telno_22', db.String(11)),
    db.Column('ref_telno_23', db.String(11)),
    db.Column('ref_telno_24', db.String(11)),
    db.Column('ref_telno_25', db.String(11)),
    db.Column('ref_telno_26', db.String(11)),
    db.Column('ref_telno_27', db.String(11)),
    db.Column('ref_telno_28', db.String(11)),
    db.Column('ref_telno_29', db.String(11)),
    db.Column('ref_telno_30', db.String(11)),
    db.Column('create_date', db.DateTime, nullable=False),
    db.Column('renew_date', db.DateTime, nullable=False),
    db.Column('operate_cd', db.String(128), nullable=False),
    db.Column('c_flag', db.String(1))
)


t_ex_voip_p_dat = db.Table(
    'ex_voip_p_dat',
    db.Column('ex_voip_p_dat_seq', db.Integer, nullable=False, server_default=db.FetchedValue()),
    db.Column('ws_common_id', db.String(20), nullable=False, index=True),
    db.Column('ws_common_renbn', db.String(2)),
    db.Column('contract_no', db.String(12)),
    db.Column('opt_contract_no', db.Numeric(10, 0)),
    db.Column('apply_date', db.DateTime, nullable=False),
    db.Column('send_plan_date', db.DateTime),
    db.Column('send_date', db.DateTime),
    db.Column('apply_kind', db.String(4)),
    db.Column('prog_status', db.String(2)),
    db.Column('oem_id', db.String(4), nullable=False),
    db.Column('oem_key', db.String(32)),
    db.Column('phone_user_id', db.String(128)),
    db.Column('isp_num', db.String(3)),
    db.Column('telno', db.String(13)),
    db.Column('sip_user_id', db.String(40)),
    db.Column('sip_password', db.String(20)),
    db.Column('sip_server', db.String(50)),
    db.Column('remark', db.String(80)),
    db.Column('create_date', db.DateTime, nullable=False),
    db.Column('renew_date', db.DateTime, nullable=False),
    db.Column('operate_cd', db.String(128), nullable=False),
    db.Column('c_flag', db.String(1))
)


t_ex_wimax_dat = db.Table(
    'ex_wimax_dat',
    db.Column('ex_wimax_dat_seq', db.Integer, nullable=False, server_default=db.FetchedValue()),
    db.Column('ws_common_id', db.String(20), nullable=False, index=True),
    db.Column('ws_common_renbn', db.String(2), nullable=False),
    db.Column('contract_no', db.String(12), nullable=False),
    db.Column('opt_contract_no', db.Numeric(10, 0)),
    db.Column('renew_date', db.DateTime, nullable=False),
    db.Column('create_date', db.DateTime, nullable=False),
    db.Column('operate_cd', db.String(128), nullable=False),
    db.Column('c_flag', db.String(1)),
    db.Column('remark', db.String(80)),
    db.Column('apply_date', db.DateTime),
    db.Column('apply_kind', db.String(4), nullable=False),
    db.Column('prog_status', db.String(2), nullable=False),
    db.Column('send_plan_date', db.DateTime),
    db.Column('send_date', db.DateTime),
    db.Column('wimax_user_id', db.String(10), nullable=False),
    db.Column('cui', db.String(20)),
    db.Column('uq_issue_date', db.DateTime),
    db.Column('uq_cont_start_date', db.DateTime),
    db.Column('mac_address', db.String(12)),
    db.Column('serial_no', db.String(25)),
    db.Column('send_name', db.String(100), nullable=False),
    db.Column('send_name_kana', db.String(100), nullable=False),
    db.Column('send_zip', db.String(7), nullable=False),
    db.Column('send_todohuken', db.String(8), nullable=False),
    db.Column('send_addr1', db.String(50), nullable=False),
    db.Column('send_addr2', db.String(60)),
    db.Column('send_build_name', db.String(80)),
    db.Column('send_telno', db.String(13)),
    db.Column('arrival_plan_date', db.DateTime),
    db.Column('arrival_plan_time', db.String(1)),
    db.Column('ship_no', db.String(20)),
    db.Column('direct_date', db.DateTime),
    db.Column('ship_plan_date', db.DateTime),
    db.Column('ship_decision_date', db.DateTime),
    db.Column('id_renbn', db.Numeric(2, 0), nullable=False, server_default=db.FetchedValue()),
    db.Column('equipment_info', db.String(8)),
    db.Column('send_status', db.String(2)),
    db.Column('ship_comp_date', db.DateTime),
    db.Column('iccid', db.String(19)),
    db.Column('ccode', db.String(11)),
    db.Column('uq_apply_no', db.String(9)),
    db.Column('uq_user_cd', db.String(8)),
    db.Column('user_birth', db.DateTime),
    db.Column('shop_accept_date', db.DateTime),
    db.Column('user_sex', db.String(1)),
    db.Column('policy_cd', db.String(40)),
    db.Column('uq_apply_date', db.DateTime),
    db.Column('mvno_plan_cd', db.String(3))
)


t_ex_xtyle_info = db.Table(
    'ex_xtyle_info',
    db.Column('ex_xtyle_info_seq', db.Integer, nullable=False, server_default=db.FetchedValue()),
    db.Column('opt_contract_no', db.Numeric(10, 0), nullable=False, index=True),
    db.Column('prog_status', db.String(2), nullable=False),
    db.Column('send_date', db.DateTime),
    db.Column('form_no', db.String(20)),
    db.Column('serial_no', db.String(9)),
    db.Column('id', db.String(7)),
    db.Column('create_date', db.DateTime, nullable=False),
    db.Column('renew_date', db.DateTime, nullable=False),
    db.Column('operate_cd', db.String(128), nullable=False),
    db.Column('c_flag', db.String(1))
)


class FlTariffMst(db.Model):
    __tablename__ = 'fl_tariff_mst'

    stage = db.Column(db.Numeric(1, 0), primary_key=True, nullable=False)
    lower_limit_traffic = db.Column(db.Numeric(19, 0), primary_key=True, nullable=False)
    unit_cost = db.Column(db.Numeric(10, 0), nullable=False)
    unit_name = db.Column(db.String(10))
    create_date = db.Column(db.DateTime, nullable=False)
    renew_date = db.Column(db.DateTime, nullable=False)
    operate_cd = db.Column(db.String(128), nullable=False)


class FlTrafficInfo(db.Model):
    __tablename__ = 'fl_traffic_info'

    bill_month = db.Column(db.String(6), primary_key=True, nullable=False)
    line_no = db.Column(db.Numeric(7, 0), primary_key=True, nullable=False)
    account_id = db.Column(db.String(256), nullable=False)
    sum_month = db.Column(db.String(6))
    total_traffic = db.Column(db.Numeric(19, 0), nullable=False)
    up_traffic = db.Column(db.Numeric(19, 0))
    down_traffic = db.Column(db.Numeric(19, 0))
    create_date = db.Column(db.DateTime, nullable=False)
    renew_date = db.Column(db.DateTime, nullable=False)
    operate_cd = db.Column(db.String(128), nullable=False)


class FusionOprMst(db.Model):
    __tablename__ = 'fusion_opr_mst'

    apply_kind_cd = db.Column(db.String(4), primary_key=True)
    apply_kind_name = db.Column(db.String(80))
    opr_apply_kind_cd = db.Column(db.String(3), nullable=False)
    opr_apply_kind_name = db.Column(db.String(60))
    data_cd = db.Column(db.String(5))
    create_date = db.Column(db.DateTime, nullable=False)
    renew_date = db.Column(db.DateTime, nullable=False)
    operate_cd = db.Column(db.String(128), nullable=False)
    c_flag = db.Column(db.String(1))


class GoodsDat(db.Model):
    __tablename__ = 'goods_dat'

    ws_common_id = db.Column(db.String(20), primary_key=True)
    ws_common_renbn = db.Column(db.String(2), nullable=False)
    contract_no = db.Column(db.String(12), nullable=False, index=True)
    renew_date = db.Column(db.DateTime, nullable=False)
    create_date = db.Column(db.DateTime, nullable=False)
    operate_cd = db.Column(db.String(128), nullable=False)
    remark = db.Column(db.String(80))
    apply_date = db.Column(db.DateTime)
    apply_kind = db.Column(db.String(4), nullable=False)
    prog_status = db.Column(db.String(2), nullable=False)
    send_plan_date = db.Column(db.DateTime)
    send_date = db.Column(db.DateTime)
    model_number = db.Column(db.String(64), nullable=False)
    order_no = db.Column(db.String(16), nullable=False, index=True)
    deliver_date = db.Column(db.DateTime)
    deliver_time = db.Column(db.String(2))
    deliver_firstname = db.Column(db.String(20))
    deliver_lastname = db.Column(db.String(50), nullable=False)
    deliver_chgdept = db.Column(db.String(50))
    deliver_chgpost = db.Column(db.String(20))
    deliver_chgname = db.Column(db.String(20))
    deliver_zip = db.Column(db.String(8), nullable=False)
    deliver_todohuken = db.Column(db.String(8), nullable=False)
    deliver_gun = db.Column(db.String(40))
    deliver_ku = db.Column(db.String(40))
    deliver_area = db.Column(db.String(40))
    deliver_chome = db.Column(db.String(10))
    deliver_banchi = db.Column(db.String(40))
    deliver_build_name = db.Column(db.String(150))
    search_id = db.Column(db.String(14))
    lot_cd = db.Column(db.String(6))
    deliver_start_date = db.Column(db.DateTime)
    deliver_end_date = db.Column(db.DateTime)
    deliver_status = db.Column(db.String(2))


class GoodsRemainder(db.Model):
    __tablename__ = 'goods_remainder'

    contract_no = db.Column(db.String(12), primary_key=True)
    create_date = db.Column(db.DateTime, nullable=False)
    renew_date = db.Column(db.DateTime, nullable=False)
    operate_cd = db.Column(db.String(128), nullable=False)
    installment_cd = db.Column(db.String(3), nullable=False)
    order_no = db.Column(db.String(16))
    start_month = db.Column(db.Date)
    end_plan_month = db.Column(db.Date)
    goods_cost = db.Column(db.Numeric(8, 0))
    end_month = db.Column(db.Date)
    remaining_month = db.Column(db.Date)
    remaining_cost = db.Column(db.Numeric(8, 0))
    demand_count = db.Column(db.Numeric(2, 0), nullable=False, server_default=db.FetchedValue())
    demand_cost = db.Column(db.Numeric(8, 0))


class HbmBillInfo(db.Model):
    __tablename__ = 'hbm_bill_info'

    msisdn = db.Column(db.String(11), primary_key=True, nullable=False)
    used_month = db.Column(db.Date, primary_key=True, nullable=False)
    capacity = db.Column(db.Numeric(9, 0), primary_key=True, nullable=False)
    create_date = db.Column(db.DateTime, nullable=False)
    renew_date = db.Column(db.DateTime, nullable=False)
    operate_cd = db.Column(db.String(128), nullable=False)
    bill_month = db.Column(db.Date, nullable=False, index=True)
    unit_cost = db.Column(db.Numeric(10, 4), nullable=False)
    quantity = db.Column(db.Numeric(19, 0), nullable=False)


class HbmDat(db.Model):
    __tablename__ = 'hbm_dat'

    ws_common_id = db.Column(db.String(20), primary_key=True)
    ws_common_renbn = db.Column(db.String(2), nullable=False)
    contract_no = db.Column(db.String(12), nullable=False, index=True)
    opt_contract_no = db.Column(db.Numeric(10, 0))
    isp_order_no = db.Column(db.String(20), nullable=False, index=True)
    renew_date = db.Column(db.DateTime, nullable=False)
    create_date = db.Column(db.DateTime, nullable=False)
    operate_cd = db.Column(db.String(128), nullable=False)
    c_flag = db.Column(db.String(1))
    remark = db.Column(db.String(80))
    apply_date = db.Column(db.DateTime)
    apply_kind = db.Column(db.String(4), nullable=False)
    prog_status = db.Column(db.String(2), nullable=False)
    send_plan_date = db.Column(db.DateTime)
    send_date = db.Column(db.DateTime)
    hbm_status = db.Column(db.String(1))
    imei = db.Column(db.String(15), index=True)
    iccid = db.Column(db.String(19))
    msisdn = db.Column(db.String(11), index=True)
    send_name = db.Column(db.String(120), nullable=False)
    send_zip = db.Column(db.String(7), nullable=False)
    send_todohuken = db.Column(db.String(8), nullable=False)
    send_addr1 = db.Column(db.String(100), nullable=False)
    send_addr2 = db.Column(db.String(100))
    send_build_name = db.Column(db.String(80))
    send_telno = db.Column(db.String(11))
    arrival_plan_date = db.Column(db.DateTime)
    arrival_plan_time = db.Column(db.String(1))
    ship_no = db.Column(db.String(20))
    direct_date = db.Column(db.DateTime)
    ship_decision_date = db.Column(db.DateTime)
    ship_comp_date = db.Column(db.DateTime)
    send_status = db.Column(db.String(2))
    item_cd = db.Column(db.String(10))
    return_limit_date = db.Column(db.DateTime)
    return_flg = db.Column(db.String(1))
    return_date = db.Column(db.DateTime)
    return_kit_reg_date = db.Column(db.DateTime)
    return_send_date = db.Column(db.DateTime)
    org_ws_common_id = db.Column(db.String(20))
    sim_acct_stop_date = db.Column(db.DateTime)
    lost_opt_contract_no = db.Column(db.Numeric(10, 0))
    user_name_k = db.Column(db.String(100))
    user_sex = db.Column(db.String(1))
    user_birth = db.Column(db.DateTime)
    device_cd = db.Column(db.String(2))
    mnp_number = db.Column(db.String(10))
    mnp_telno = db.Column(db.String(11))
    mnp_expire_date = db.Column(db.DateTime)
    mnp_line_name = db.Column(db.String(100))
    mnp_line_name_k = db.Column(db.String(100))
    pt2_account_status = db.Column(db.String(1))
    charge_date = db.Column(db.DateTime)
    portable_tel_flg = db.Column(db.String(1))
    mnp_out_number = db.Column(db.String(10))
    mnp_out_status = db.Column(db.String(1))
    mnp_out_apply_date = db.Column(db.DateTime)
    mnp_out_order_date = db.Column(db.DateTime)
    mnp_out_order_comp_date = db.Column(db.DateTime)
    mnp_out_expire_date = db.Column(db.DateTime)
    mnp_out_end_date = db.Column(db.DateTime)
    mnp_out_line_lastname_k = db.Column(db.String(80))
    mnp_out_line_firstname_k = db.Column(db.String(40))
    mnp_out_line_lastname = db.Column(db.String(40))
    mnp_out_line_firstname = db.Column(db.String(20))
    mnp_out_line_birth = db.Column(db.DateTime)
    semiblack_add_status = db.Column(db.String(1))
    semiblack_add_reserve_date = db.Column(db.DateTime)
    semiblack_add_apply_date = db.Column(db.DateTime)
    semiblack_add_comp_date = db.Column(db.DateTime)
    semiblack_add_error_msg = db.Column(db.String(100))
    issue_error_msg = db.Column(db.String(500))
    issue_touser_error_msg = db.Column(db.String(500))
    notdelivered_date = db.Column(db.DateTime)
    tcard_issue = db.Column(db.String(1))
    channel_flg = db.Column(db.String(1))
    changevoice_flg = db.Column(db.String(1))
    quota_carryover_date = db.Column(db.DateTime)
    pt2_flg = db.Column(db.String(1))
    warranty_start_date = db.Column(db.DateTime)


class HibitCollectionInfo(db.Model):
    __tablename__ = 'hibit_collection_info'

    create_date = db.Column(db.DateTime, nullable=False)
    renew_date = db.Column(db.DateTime, nullable=False)
    operate_cd = db.Column(db.String(128), nullable=False)
    c_flag = db.Column(db.String(1))
    unext_id = db.Column(db.String(10), primary_key=True, nullable=False)
    used_month = db.Column(db.Date, primary_key=True, nullable=False)
    bill_month = db.Column(db.Date, nullable=False, index=True)
    service = db.Column(db.String(128), nullable=False)
    base_cost = db.Column(db.Numeric(12, 4), nullable=False)
    jimu_cost = db.Column(db.Numeric(12, 4), nullable=False)
    ppv_cost = db.Column(db.Numeric(12, 4), nullable=False)
    iyaku_cost = db.Column(db.Numeric(12, 4), nullable=False)
    tax_cost = db.Column(db.Numeric(12, 4), nullable=False)
    total_cost = db.Column(db.Numeric(12, 4), nullable=False)


class IcrackedCont(db.Model):
    __tablename__ = 'icracked_cont'

    imei = db.Column(db.String(15), primary_key=True, nullable=False)
    contract_no = db.Column(db.String(12), primary_key=True, nullable=False)
    opt_contract_no = db.Column(db.Numeric(10, 0), primary_key=True, nullable=False)
    imei_create_date = db.Column(db.Date)
    service_start_date = db.Column(db.Date)
    repair_date = db.Column(db.Date)
    repair_content = db.Column(db.String(2))
    renew_date = db.Column(db.DateTime, nullable=False)
    create_date = db.Column(db.DateTime, nullable=False)
    operate_cd = db.Column(db.String(128), nullable=False)
    c_flag = db.Column(db.String(1))
    diff_flag = db.Column(db.String(1))
    prog_status = db.Column(db.String(2), nullable=False)


class InstallmentMst(db.Model):
    __tablename__ = 'installment_mst'

    installment_cd = db.Column(db.String(3), primary_key=True)
    create_date = db.Column(db.DateTime, nullable=False)
    renew_date = db.Column(db.DateTime, nullable=False)
    operate_cd = db.Column(db.String(128), nullable=False)
    plan_cd = db.Column(db.String(8), nullable=False)
    split_count = db.Column(db.Numeric(2, 0), nullable=False)
    first_cost = db.Column(db.Numeric(8, 0), nullable=False)
    regular_cost = db.Column(db.Numeric(8, 0), nullable=False)
    june_extra_cost = db.Column(db.Numeric(8, 0), nullable=False)
    december_extra_cost = db.Column(db.Numeric(8, 0), nullable=False)


class IpNumMst(db.Model):
    __tablename__ = 'ip_num_mst'

    ip_telno = db.Column(db.String(11), primary_key=True)
    use_status = db.Column(db.String(2))
    start_date = db.Column(db.DateTime)
    end_date = db.Column(db.DateTime)
    entry_cd = db.Column(db.String(13))
    plan_cd = db.Column(db.String(8))
    create_date = db.Column(db.DateTime, nullable=False)
    renew_date = db.Column(db.DateTime, nullable=False)
    operate_cd = db.Column(db.String(128), nullable=False)
    c_flag = db.Column(db.String(1))


class KddiBillRemainder(db.Model):
    __tablename__ = 'kddi_bill_remainder'

    create_date = db.Column(db.DateTime, nullable=False)
    renew_date = db.Column(db.DateTime, nullable=False)
    operate_cd = db.Column(db.String(128), nullable=False)
    kddi_cont_no = db.Column(db.String(10), primary_key=True, nullable=False)
    used_month = db.Column(db.Date, primary_key=True, nullable=False)
    kddi_plan_cd = db.Column(db.String(10), primary_key=True, nullable=False)
    remainder_kind = db.Column(db.String(1), primary_key=True, nullable=False)
    remainder_status = db.Column(db.String(1), nullable=False)
    bill_month = db.Column(db.Date, nullable=False)
    plan_bill_month = db.Column(db.Date, index=True)
    kddi_plan_name = db.Column(db.String(90), nullable=False)
    cost = db.Column(db.Numeric(12, 4), nullable=False)
    taxfree_kbn = db.Column(db.String(1), nullable=False)
    creditor_cd = db.Column(db.String(1), nullable=False)
    creditor_subcd = db.Column(db.String(3))
    tax_percent = db.Column(db.Numeric(4, 1))


class KddiCollectionInfo(db.Model):
    __tablename__ = 'kddi_collection_info'

    create_date = db.Column(db.DateTime, nullable=False)
    renew_date = db.Column(db.DateTime, nullable=False)
    operate_cd = db.Column(db.String(128), nullable=False)
    c_flag = db.Column(db.String(1))
    kddi_cont_no = db.Column(db.String(10), primary_key=True, nullable=False)
    used_month = db.Column(db.Date, primary_key=True, nullable=False)
    kddi_plan_cd = db.Column(db.String(10), primary_key=True, nullable=False)
    bill_month = db.Column(db.Date, nullable=False, index=True)
    kddi_plan_name = db.Column(db.String(90), nullable=False)
    cost = db.Column(db.Numeric(12, 4), nullable=False)
    taxfree_kbn = db.Column(db.String(1), nullable=False)
    creditor_cd = db.Column(db.String(1), nullable=False)
    creditor_subcd = db.Column(db.String(3))
    tax_percent = db.Column(db.Numeric(4, 1), primary_key=True, nullable=False)


class KddiCollectionSum(db.Model):
    __tablename__ = 'kddi_collection_sum'

    create_date = db.Column(db.DateTime, nullable=False)
    renew_date = db.Column(db.DateTime, nullable=False)
    operate_cd = db.Column(db.String(128), nullable=False)
    c_flag = db.Column(db.String(1))
    kddi_cont_no = db.Column(db.String(10), primary_key=True, nullable=False)
    used_month = db.Column(db.Date, primary_key=True, nullable=False)
    bill_month = db.Column(db.Date, nullable=False, index=True)
    kddi_taxable_total = db.Column(db.Numeric(12, 4), nullable=False, server_default=db.FetchedValue())
    kddi_taxfree_total = db.Column(db.Numeric(12, 4), nullable=False, server_default=db.FetchedValue())
    collection_taxable_total = db.Column(db.Numeric(12, 4), nullable=False, server_default=db.FetchedValue())
    collection_taxin_total = db.Column(db.Numeric(12, 4), nullable=False, server_default=db.FetchedValue())
    taxable_total = db.Column(db.Numeric(12, 4), nullable=False, server_default=db.FetchedValue())
    taxfree_total = db.Column(db.Numeric(12, 4), nullable=False, server_default=db.FetchedValue())
    tax_total = db.Column(db.Numeric(12, 4), nullable=False, server_default=db.FetchedValue())
    all_total = db.Column(db.Numeric(12, 4), nullable=False, server_default=db.FetchedValue())
    plan_bill_month = db.Column(db.Date)


class KddiCont(db.Model):
    __tablename__ = 'kddi_cont'

    contract_no = db.Column(db.String(12), nullable=False, index=True)
    kddi_mng_no = db.Column(db.Numeric(10, 0), primary_key=True)
    renew_date = db.Column(db.DateTime, nullable=False)
    create_date = db.Column(db.DateTime, nullable=False)
    operate_cd = db.Column(db.String(128), nullable=False)
    c_flag = db.Column(db.String(1))
    remark = db.Column(db.String(80))
    kddi_cont_no = db.Column(db.String(10), index=True)
    isp_order_no = db.Column(db.String(20), nullable=False)
    kddi_create_date = db.Column(db.DateTime)
    line_plan_date = db.Column(db.DateTime)
    line_start_date = db.Column(db.DateTime)
    tel_pre_service_num = db.Column(db.Numeric(1, 0), nullable=False, server_default=db.FetchedValue())
    tel_service_num = db.Column(db.Numeric(1, 0), nullable=False, server_default=db.FetchedValue())
    tv_pre_service_num = db.Column(db.Numeric(1, 0), nullable=False, server_default=db.FetchedValue())
    tv_service_num = db.Column(db.Numeric(1, 0), nullable=False, server_default=db.FetchedValue())
    kddi_use_end_date = db.Column(db.DateTime)
    kddi_cont_end_date = db.Column(db.DateTime)
    service_kind = db.Column(db.String(1))
    service_state_flg = db.Column(db.String(1))
    design_comp_date = db.Column(db.DateTime)
    outside_comp_date = db.Column(db.DateTime)
    work_stay_reason = db.Column(db.String(120))
    provide_date = db.Column(db.DateTime)
    provide_flg = db.Column(db.String(1))
    provide_ng_reason = db.Column(db.String(120))
    work_plan_date = db.Column(db.DateTime)
    work_end_date = db.Column(db.DateTime)
    counting_start_month = db.Column(db.Date)


class KddiContOpt(db.Model):
    __tablename__ = 'kddi_cont_opt'

    kddi_cont_no = db.Column(db.String(10), primary_key=True, nullable=False)
    service_cont_no = db.Column(db.String(8), primary_key=True, nullable=False)
    renew_date = db.Column(db.DateTime, nullable=False)
    create_date = db.Column(db.DateTime, nullable=False)
    operate_cd = db.Column(db.String(128), nullable=False)
    c_flag = db.Column(db.String(1))
    remark = db.Column(db.String(80))
    service_kbn = db.Column(db.String(1), nullable=False)
    telno = db.Column(db.String(11), index=True)
    portable_flg = db.Column(db.String(1))
    portable_prog_flg = db.Column(db.String(1))
    kddi_apply_date = db.Column(db.DateTime)
    bill_start_date = db.Column(db.DateTime)
    use_end_date = db.Column(db.DateTime)
    cont_end_date = db.Column(db.DateTime)
    talkie_flg = db.Column(db.String(1))
    talkie_no = db.Column(db.String(11))


class KddiDat(db.Model):
    __tablename__ = 'kddi_dat'

    kddi_mng_no = db.Column(db.Numeric(10, 0), primary_key=True, nullable=False)
    seq_no = db.Column(db.Numeric(2, 0), primary_key=True, nullable=False)
    renew_date = db.Column(db.DateTime, nullable=False)
    create_date = db.Column(db.DateTime, nullable=False)
    operate_cd = db.Column(db.String(128), nullable=False)
    c_flag = db.Column(db.String(1))
    remark = db.Column(db.String(80))
    apply_date = db.Column(db.DateTime)
    service_kbn = db.Column(db.String(1), nullable=False)
    apply_kind = db.Column(db.String(4), nullable=False)
    prog_status = db.Column(db.String(2))
    send_plan_date = db.Column(db.DateTime)
    send_date = db.Column(db.DateTime)
    cancel_plan_date = db.Column(db.DateTime)
    tel_no = db.Column(db.String(11), index=True)
    ntt_return_kbn = db.Column(db.String(1))
    tel_talkie_flg = db.Column(db.String(1))
    tel_talkie_no = db.Column(db.String(11))


class KddiDmd(db.Model):
    __tablename__ = 'kddi_dmd'

    kddi_mng_no = db.Column(db.Numeric(10, 0), primary_key=True)
    renew_date = db.Column(db.DateTime, nullable=False)
    create_date = db.Column(db.DateTime, nullable=False)
    operate_cd = db.Column(db.String(128), nullable=False)
    c_flag = db.Column(db.String(1))
    remark = db.Column(db.String(80))
    kddi_dmd_shift_flg = db.Column(db.String(1))
    kddi_dmd_kind = db.Column(db.String(1))
    au_cont_telno = db.Column(db.String(11))
    au_cont_birth = db.Column(db.DateTime)
    au_cont_name = db.Column(db.String(60))
    au_cont_name_k = db.Column(db.String(60))
    au_cont_sign_flg = db.Column(db.String(1))
    auonenet_cont_cd = db.Column(db.String(10))
    auonenet_cont_name = db.Column(db.String(60))
    auonenet_cont_name_k = db.Column(db.String(60))
    auonenet_sign_flg = db.Column(db.String(1))
    kotei_telno = db.Column(db.String(10))
    kotei_cont_name = db.Column(db.String(60))
    kotei_cont_name_k = db.Column(db.String(60))
    kotei_sign_flg = db.Column(db.String(1))
    kddi_dmd_name = db.Column(db.String(60))
    kddi_dmd_name_k = db.Column(db.String(60))
    kddi_dmd_sign_flg = db.Column(db.String(1))
    kddi_pay_name = db.Column(db.String(60))
    kddi_pay_name_k = db.Column(db.String(60))
    pay_sign_flg = db.Column(db.String(1))
    pledge_name_flg = db.Column(db.String(1))
    apply_sign_flg = db.Column(db.String(1))
    apply_pledge_flg = db.Column(db.String(1))
    paper_bill_flg = db.Column(db.String(1))
    kddi_payment_kbn = db.Column(db.String(1))
    kddi_payment_shift_kbn = db.Column(db.String(1))
    myline_acount = db.Column(db.String(10))
    kddi_email_apply_flag = db.Column(db.String(1))
    auonenet_email = db.Column(db.String(129))
    kddi_dmd_result_kbn = db.Column(db.String(1))
    kddi_dmd_method = db.Column(db.String(1))
    kddi_dmd_first_month = db.Column(db.String(6))
    kddi_dmd_error_cd = db.Column(db.String(4))
    kddi_dmd_error_msg = db.Column(db.String(200))
    kddi_dmd_receipt_date = db.Column(db.DateTime)
    kddi_claim_cont_cd = db.Column(db.String(1))
    kddi_claim_close_reserve_cd = db.Column(db.String(1))
    servicestop_file_date = db.Column(db.DateTime)


class KddiInfo(db.Model):
    __tablename__ = 'kddi_info'

    kddi_mng_no = db.Column(db.Numeric(10, 0), primary_key=True)
    renew_date = db.Column(db.DateTime, nullable=False)
    create_date = db.Column(db.DateTime, nullable=False)
    operate_cd = db.Column(db.String(128), nullable=False)
    c_flag = db.Column(db.String(1))
    remark = db.Column(db.String(80))
    kddi_order_no = db.Column(db.String(10))
    kddi_jit_bumon_cd = db.Column(db.String(4))
    kddi_tyoku_kbn = db.Column(db.String(1))
    kddi_agency_cd = db.Column(db.String(10))
    cont_zip = db.Column(db.String(7))
    cont_todohuken = db.Column(db.String(8))
    cont_shiku = db.Column(db.String(60))
    cont_area_chome_banchi = db.Column(db.String(60))
    cont_build_name = db.Column(db.String(100))
    cont_telno1 = db.Column(db.String(11), index=True)
    cont_telno2 = db.Column(db.String(11), index=True)
    email = db.Column(db.String(129))
    est_place_flg = db.Column(db.String(1))
    est_zip = db.Column(db.String(7))
    est_todohuken = db.Column(db.String(8))
    est_shiku = db.Column(db.String(60))
    est_area_chome_banchi = db.Column(db.String(60))
    est_build_name = db.Column(db.String(100))
    dest_place_flg = db.Column(db.String(1))
    dest_name = db.Column(db.String(60))
    dest_name_k = db.Column(db.String(60))
    dest_zip = db.Column(db.String(7))
    dest_todohuken = db.Column(db.String(8))
    dest_shiku = db.Column(db.String(60))
    dest_area_chome_banchi = db.Column(db.String(60))
    dest_build_name = db.Column(db.String(100))
    dest_telno = db.Column(db.String(11), index=True)
    cont_group_no = db.Column(db.String(10))
    article_no = db.Column(db.String(8))
    ridge_id = db.Column(db.String(2))
    room_no = db.Column(db.String(5))
    modular_board_num = db.Column(db.String(1))
    line1_no = db.Column(db.String(11), index=True)
    line1_status = db.Column(db.String(1))
    line2_no = db.Column(db.String(11), index=True)
    line2_status = db.Column(db.String(1))
    taxfree_user_cd = db.Column(db.String(1))
    hikari_plus_tel_flg = db.Column(db.String(1))
    portable_tel_flg = db.Column(db.String(1))
    telno_050_flg = db.Column(db.String(1))
    portable_tel = db.Column(db.String(11), index=True)
    ntt_name = db.Column(db.String(60))
    ntt_name_k = db.Column(db.String(60))
    interrupt_call_flg = db.Column(db.String(1))
    caller_id_display_flg = db.Column(db.String(1))
    notice_telno_flg = db.Column(db.String(1))
    nuisance_call_repulse_flg = db.Column(db.String(1))
    caller_id_notice_flg = db.Column(db.String(1))
    caller_id_notice_cd = db.Column(db.String(1))
    detail_output_flg = db.Column(db.String(1))
    number_guidance_flg = db.Column(db.String(1))
    hellopage_flg = db.Column(db.String(1))
    hikari_plus_tv_flg = db.Column(db.String(1))
    stb_cd = db.Column(db.String(4))
    filter_flg = db.Column(db.String(1))
    filter_cd = db.Column(db.String(4))
    kaketuke_support_flg = db.Column(db.String(1))
    campain_apply_date = db.Column(db.DateTime)
    interrupt_number_flg = db.Column(db.String(1))
    arrival_plan_date = db.Column(db.DateTime)
    dest_addr_change_flg = db.Column(db.String(1))
    musen_lan_rental_cd = db.Column(db.String(4))
    musen_lan_rental_num = db.Column(db.String(2))
    add_hgw_cd = db.Column(db.String(4))
    add_hgw_num = db.Column(db.String(2))
    add_stb_cd = db.Column(db.String(4))
    add_stb_num = db.Column(db.String(2))
    entering_plan_date = db.Column(db.DateTime)
    redirect_call_flg = db.Column(db.String(1))
    house_cd = db.Column(db.String(1))
    possession_cd = db.Column(db.String(1))
    isp_cd = db.Column(db.String(3))
    incoming_notice_flg = db.Column(db.String(1))
    au_term_telno1 = db.Column(db.String(11))
    au_term_telno2 = db.Column(db.String(11))
    au_term_telno3 = db.Column(db.String(11))
    ntt_line_cd = db.Column(db.String(2))
    kddi_memo = db.Column(db.String(16))
    same_0abj_telno = db.Column(db.String(11))
    exist_line_flg = db.Column(db.String(1))
    important_notice = db.Column(db.String(100))
    ntt_zip = db.Column(db.String(7))
    ntt_todohuken = db.Column(db.String(8))
    ntt_shiku = db.Column(db.String(60))
    ntt_area_chome_banchi = db.Column(db.String(60))
    ntt_build_name = db.Column(db.String(100))
    speed_kbn = db.Column(db.String(1))
    musen_lan_rental_cd2 = db.Column(db.String(4))
    musen_lan_rental_num2 = db.Column(db.String(2))
    musen_lan_rental_cd3 = db.Column(db.String(4))
    musen_lan_rental_num3 = db.Column(db.String(2))
    musen_lan_rental_cd4 = db.Column(db.String(4))
    musen_lan_rental_num4 = db.Column(db.String(2))
    musen_lan_rental_cd5 = db.Column(db.String(4))
    musen_lan_rental_num5 = db.Column(db.String(2))
    work_date_id = db.Column(db.String(10))
    monthly_item01 = db.Column(db.String(4))
    monthly_item02 = db.Column(db.String(4))
    monthly_item03 = db.Column(db.String(4))
    monthly_item04 = db.Column(db.String(4))
    monthly_item05 = db.Column(db.String(4))
    monthly_item06 = db.Column(db.String(4))
    monthly_item07 = db.Column(db.String(4))
    monthly_item08 = db.Column(db.String(4))
    monthly_item09 = db.Column(db.String(4))
    monthly_item10 = db.Column(db.String(4))
    monthly_item11 = db.Column(db.String(4))
    monthly_item12 = db.Column(db.String(4))
    pre_voip_co_cd = db.Column(db.String(4))
    pre_voip_co_cd2 = db.Column(db.String(4))
    est_floors = db.Column(db.String(3))
    cont_room_no = db.Column(db.String(40))
    owner_name = db.Column(db.String(60))
    owner_address = db.Column(db.String(100))
    owner_telno = db.Column(db.String(11))
    owner_kbn = db.Column(db.String(1))
    est_telno = db.Column(db.String(11))
    kddi3m_au_smart_val_cd = db.Column(db.String(15))
    kddi3m_multi_campaign_kbn = db.Column(db.String(1), nullable=False, server_default=db.FetchedValue())
    kddi3m_campaign_flg = db.Column(db.String(1))
    kddi3m_applyprint_no = db.Column(db.String(9))


class KddiLiquidationInfo(db.Model):
    __tablename__ = 'kddi_liquidation_info'

    create_date = db.Column(db.DateTime, nullable=False)
    renew_date = db.Column(db.DateTime, nullable=False)
    operate_cd = db.Column(db.String(128), nullable=False)
    c_flag = db.Column(db.String(1))
    kddi_cont_no = db.Column(db.String(10), primary_key=True, nullable=False)
    used_month = db.Column(db.Date, primary_key=True, nullable=False)
    kddi_plan_cd = db.Column(db.String(10), primary_key=True, nullable=False)
    bill_month = db.Column(db.Date, nullable=False, index=True)
    kddi_plan_name = db.Column(db.String(90), nullable=False)
    cost = db.Column(db.Numeric(12, 4), nullable=False)
    taxfree_kbn = db.Column(db.String(1), nullable=False)
    creditor_cd = db.Column(db.String(1), nullable=False)
    creditor_subcd = db.Column(db.String(3))
    tax_percent = db.Column(db.Numeric(4, 1), primary_key=True, nullable=False)


class L2CallLog(db.Model):
    __tablename__ = 'l2_call_log'

    used_month = db.Column(db.Date, primary_key=True, nullable=False)
    line_no = db.Column(db.Numeric(7, 0), primary_key=True, nullable=False)
    telno = db.Column(db.String(16), nullable=False, index=True)
    record_no = db.Column(db.String(6))
    call_date = db.Column(db.String(8))
    call_time = db.Column(db.String(6))
    telno_dialed = db.Column(db.String(32))
    dist_type = db.Column(db.String(11))
    dist_detail = db.Column(db.String(44))
    call_duration = db.Column(db.String(7))
    call_charge = db.Column(db.Numeric(8, 2))
    time_period = db.Column(db.String(24))
    discount = db.Column(db.String(24))
    call_classification_1 = db.Column(db.String(24))
    call_classification_2 = db.Column(db.String(24))
    call_classification_3 = db.Column(db.String(24))
    bill_month = db.Column(db.Date, nullable=False)
    contract_no = db.Column(db.String(12), index=True)
    user_charge = db.Column(db.Numeric(6, 0))
    bill_kbn_cd = db.Column(db.String(2))
    create_date = db.Column(db.DateTime, nullable=False)
    renew_date = db.Column(db.DateTime, nullable=False)
    operate_cd = db.Column(db.String(128), nullable=False)
    user_duration = db.Column(db.String(7))


class LfCont(db.Model):
    __tablename__ = 'lf_cont'

    contract_no = db.Column(db.String(12), nullable=False)
    opt_contract_no = db.Column(db.Numeric(10, 0))
    isp_user_id = db.Column(db.String(20), primary_key=True)
    renew_date = db.Column(db.DateTime, nullable=False)
    create_date = db.Column(db.DateTime, nullable=False)
    operate_cd = db.Column(db.String(128), nullable=False)
    remark = db.Column(db.String(80))
    unext_id = db.Column(db.String(10))
    license_key1 = db.Column(db.String(50))
    license_key2 = db.Column(db.String(50))
    license_key3 = db.Column(db.String(50))
    license_key4 = db.Column(db.String(50))
    license_key5 = db.Column(db.String(50))
    license_key6 = db.Column(db.String(50))
    license_key7 = db.Column(db.String(50))
    apply_request_date = db.Column(db.Date)
    apply_process_date = db.Column(db.Date)
    end_request_date = db.Column(db.Date)
    end_process_date = db.Column(db.Date)


class LfDat(db.Model):
    __tablename__ = 'lf_dat'

    ws_common_id = db.Column(db.String(20), primary_key=True)
    ws_common_renbn = db.Column(db.String(2), nullable=False)
    contract_no = db.Column(db.String(12), nullable=False)
    create_date = db.Column(db.DateTime, nullable=False)
    renew_date = db.Column(db.DateTime, nullable=False)
    operate_cd = db.Column(db.String(128), nullable=False)
    remark = db.Column(db.String(80))
    apply_kind = db.Column(db.String(4), nullable=False)
    prog_status = db.Column(db.String(2), nullable=False)
    apply_date = db.Column(db.DateTime, nullable=False)
    send_plan_date = db.Column(db.DateTime)
    send_date = db.Column(db.DateTime)
    opt_contract_no = db.Column(db.Numeric(10, 0))
    firstname = db.Column(db.String(20))
    firstname_k = db.Column(db.String(20))
    lastname = db.Column(db.String(50))
    lastname_k = db.Column(db.String(100))
    lf_sex = db.Column(db.String(1))
    lf_birth = db.Column(db.DateTime)
    lf_telno = db.Column(db.String(20))
    lf_mobile = db.Column(db.String(20))
    lf_zip = db.Column(db.String(7))
    lf_todohuken = db.Column(db.String(4))
    lf_shiku_area_chome = db.Column(db.String(50))
    lf_banchi = db.Column(db.String(50))
    lf_build_name = db.Column(db.String(40))
    lf_email = db.Column(db.String(128))
    plan_type = db.Column(db.String(1))


class LteDat(db.Model):
    __tablename__ = 'lte_dat'

    ws_common_id = db.Column(db.String(20), primary_key=True)
    ws_common_renbn = db.Column(db.String(2), nullable=False)
    contract_no = db.Column(db.String(12), nullable=False, index=True)
    opt_contract_no = db.Column(db.Numeric(10, 0))
    renew_date = db.Column(db.DateTime, nullable=False)
    create_date = db.Column(db.DateTime, nullable=False)
    operate_cd = db.Column(db.String(128), nullable=False)
    c_flag = db.Column(db.String(1))
    remark = db.Column(db.String(80))
    apply_date = db.Column(db.DateTime)
    apply_kind = db.Column(db.String(4), nullable=False)
    prog_status = db.Column(db.String(2), nullable=False)
    send_plan_date = db.Column(db.DateTime)
    send_date = db.Column(db.DateTime)
    lte_user_id = db.Column(db.String(10), nullable=False)
    imei = db.Column(db.String(15))
    iccid = db.Column(db.String(19))
    msisdn = db.Column(db.String(11))
    lte_machin_meker = db.Column(db.String(50))
    lte_machin_model = db.Column(db.String(50))
    send_name = db.Column(db.String(100), nullable=False)
    send_name_kana = db.Column(db.String(100), nullable=False)
    send_zip = db.Column(db.String(7), nullable=False)
    send_todohuken = db.Column(db.String(8), nullable=False)
    send_addr1 = db.Column(db.String(40))
    send_addr2 = db.Column(db.String(50))
    send_addr3 = db.Column(db.String(50))
    send_addr4 = db.Column(db.String(40))
    send_build_name = db.Column(db.String(80))
    send_telno = db.Column(db.String(13))
    arrival_plan_date = db.Column(db.DateTime)
    arrival_plan_time = db.Column(db.String(1))
    ship_no = db.Column(db.String(20))
    direct_date = db.Column(db.DateTime)
    ship_plan_date = db.Column(db.DateTime)
    ship_decision_date = db.Column(db.DateTime)
    ship_comp_date = db.Column(db.DateTime)
    id_renbn = db.Column(db.Numeric(2, 0), nullable=False)


class MeasuredMst(db.Model):
    __tablename__ = 'measured_mst'

    measured_cd = db.Column(db.String(4), primary_key=True)
    measured_name = db.Column(db.String(32), nullable=False)
    rate = db.Column(db.Numeric(10, 4), nullable=False)
    measured_unit = db.Column(db.Numeric(3, 0), nullable=False)
    measured_start = db.Column(db.Numeric(3, 0), nullable=False)
    measured_limit = db.Column(db.Numeric(8, 0))
    taxfree_kbn = db.Column(db.String(1), nullable=False)
    unit_name = db.Column(db.String(10))
    create_date = db.Column(db.DateTime, nullable=False)
    renew_date = db.Column(db.DateTime, nullable=False)
    operate_cd = db.Column(db.String(128), nullable=False)
    c_flag = db.Column(db.String(1))


class Monitor(db.Model):
    __tablename__ = 'monitor'

    monitor_type = db.Column(db.String(2), primary_key=True, nullable=False)
    contract_no = db.Column(db.String(12), primary_key=True, nullable=False)
    cont_cancel_date = db.Column(db.DateTime)


class MopitaInfo(db.Model):
    __tablename__ = 'mopita_info'

    contbase_no = db.Column(db.String(10), primary_key=True)
    mopita_acct_id = db.Column(db.String(12))
    mopita_status = db.Column(db.String(2))
    mopita_pwd = db.Column(db.String(7))
    mopita_reg_date = db.Column(db.DateTime)
    mopita_user_id = db.Column(db.String(32))
    mopita_end_date = db.Column(db.DateTime)
    create_date = db.Column(db.DateTime, nullable=False)
    renew_date = db.Column(db.DateTime, nullable=False)
    operate_cd = db.Column(db.String(128), nullable=False)
    c_flag = db.Column(db.String(1))
    mti_pin_cd = db.Column(db.String(12))


class MtiPinMst(db.Model):
    __tablename__ = 'mti_pin_mst'

    pin_cd = db.Column(db.String(12), primary_key=True)
    expire_date = db.Column(db.DateTime, nullable=False)
    use_status = db.Column(db.String(1), nullable=False)
    renew_date = db.Column(db.DateTime, nullable=False)
    create_date = db.Column(db.DateTime, nullable=False)
    operate_cd = db.Column(db.String(128), nullable=False)
    c_flag = db.Column(db.String(1))


class NecatDat(db.Model):
    __tablename__ = 'necat_dat'

    ws_common_id = db.Column(db.String(20), primary_key=True)
    ws_common_renbn = db.Column(db.String(2), nullable=False)
    contract_no = db.Column(db.String(12), nullable=False)
    opt_contract_no = db.Column(db.Numeric(10, 0))
    isp_order_no = db.Column(db.String(14), nullable=False)
    status = db.Column(db.String(1), nullable=False)
    apply_kind = db.Column(db.String(4))
    syori_status = db.Column(db.String(2))
    syohin_cd = db.Column(db.String(20))
    product_no = db.Column(db.String(20))
    mac_address = db.Column(db.String(12))
    invoice_no = db.Column(db.String(20))
    plan_cd = db.Column(db.String(10))
    zip = db.Column(db.String(8))
    addr1 = db.Column(db.String(4))
    addr2 = db.Column(db.String(50))
    addr3 = db.Column(db.String(50))
    apply_date = db.Column(db.DateTime)
    send_plan_date = db.Column(db.DateTime)
    send_date = db.Column(db.DateTime)
    arrival_plan_date = db.Column(db.DateTime)
    arrival_plan_time = db.Column(db.String(2))
    ship_date = db.Column(db.DateTime)
    arrival_date = db.Column(db.DateTime)
    arv_info_recv_date = db.Column(db.DateTime)
    arv_info_no = db.Column(db.Numeric(2, 0))
    arv_ng_cd = db.Column(db.String(2))
    cont_start_date = db.Column(db.DateTime)
    cont_end_date = db.Column(db.DateTime)
    iad_customer_id = db.Column(db.String(30), nullable=False)
    create_date = db.Column(db.DateTime, nullable=False)
    renew_date = db.Column(db.DateTime, nullable=False)
    operate_cd = db.Column(db.String(128), nullable=False)
    c_flag = db.Column(db.String(1))
    remark = db.Column(db.String(80))


class NicosCarddb(db.Model):
    __tablename__ = 'nicos_carddb'

    card_mng_no = db.Column(db.String(12), primary_key=True, nullable=False)
    recurring_id = db.Column(db.String(15), primary_key=True, nullable=False)
    card_status = db.Column(db.String(2))
    cardno = db.Column(db.String(16))
    cardvalid = db.Column(db.String(6))
    result_cd = db.Column(db.String(3))
    create_date = db.Column(db.DateTime, nullable=False)
    renew_date = db.Column(db.DateTime, nullable=False)
    operate_cd = db.Column(db.String(128), nullable=False)


class NicosDemandTran(db.Model):
    __tablename__ = 'nicos_demand_trans'

    dmdto_id = db.Column(db.String(12), primary_key=True)
    nicos_trans_cd = db.Column(db.String(9), nullable=False)
    create_date = db.Column(db.DateTime, nullable=False)
    renew_date = db.Column(db.DateTime, nullable=False)
    operate_cd = db.Column(db.String(128), nullable=False)


class NttCollectionInfo(db.Model):
    __tablename__ = 'ntt_collection_info'

    create_date = db.Column(db.DateTime, nullable=False)
    renew_date = db.Column(db.DateTime, nullable=False)
    operate_cd = db.Column(db.String(128), nullable=False)
    ntt_e_cont_id = db.Column(db.String(16), nullable=False)
    used_month = db.Column(db.Date, primary_key=True, nullable=False)
    ntt_plan_cd = db.Column(db.String(10), primary_key=True, nullable=False)
    isp_order_no = db.Column(db.String(16), primary_key=True, nullable=False)
    bill_month = db.Column(db.Date, nullable=False, index=True)
    plan_bill_month = db.Column(db.Date)
    ntt_plan_name = db.Column(db.String(160), nullable=False)
    cost = db.Column(db.Numeric(12, 4), nullable=False)
    taxfree_kbn = db.Column(db.String(1), nullable=False)
    creditor_cd = db.Column(db.String(1), nullable=False)
    used_start_date = db.Column(db.DateTime)
    used_end_date = db.Column(db.DateTime)
    ntt_branch_name = db.Column(db.String(20))
    old_ntt_dmd_no = db.Column(db.String(10))
    charge_back = db.Column(db.String(1))
    ntt_adjust_id = db.Column(db.String(12))
    creditor_subcd = db.Column(db.String(3))


class NttCorAddCont(db.Model):
    __tablename__ = 'ntt_cor_add_cont'

    contract_code = db.Column(db.String(13), nullable=False)
    add_contract_code = db.Column(db.String(13))
    opt_contract_no = db.Column(db.Numeric(10, 0), primary_key=True)
    ntt_ew_kind = db.Column(db.String(1), nullable=False)
    renew_date = db.Column(db.DateTime, nullable=False)
    create_date = db.Column(db.DateTime, nullable=False)
    operate_cd = db.Column(db.String(128), nullable=False)
    c_flag = db.Column(db.String(1))
    service_kind = db.Column(db.String(1), nullable=False)
    service_name = db.Column(db.String(90))
    order_class = db.Column(db.String(4), nullable=False)
    order_status = db.Column(db.String(2), nullable=False)
    application_pername = db.Column(db.String(90))
    contact_phone = db.Column(db.String(90))
    applied_date = db.Column(db.DateTime)
    appoint_date = db.Column(db.DateTime)
    change_date = db.Column(db.DateTime)
    serv_start_day = db.Column(db.DateTime)
    serv_end_day = db.Column(db.DateTime)
    plan_name = db.Column(db.String(128))
    operator_ent_name = db.Column(db.String(40))
    operator_cor_branch_name = db.Column(db.String(70))
    operator_cor_section_name = db.Column(db.String(70))
    operator_cor_charge_name = db.Column(db.String(128))
    operator_cor_phone = db.Column(db.String(13))
    operator_cor_fax = db.Column(db.String(13))
    sales_ent_name = db.Column(db.String(40))
    sales_cor_branch_name = db.Column(db.String(70))
    sales_cor_section_name = db.Column(db.String(70))
    sales_cor_chargen_ame = db.Column(db.String(128))
    sales_cor_phone = db.Column(db.String(13))
    sales_cor_fax = db.Column(db.String(13))
    date_renewed = db.Column(db.DateTime)
    add_phone_no = db.Column(db.String(13))
    service_code = db.Column(db.String(8), nullable=False)
    add_phone_kbn = db.Column(db.String(1))


class NttCorAddDat(db.Model):
    __tablename__ = 'ntt_cor_add_dat'

    ws_common_id = db.Column(db.String(20), primary_key=True)
    ws_common_renbn = db.Column(db.String(2), nullable=False)
    contract_code = db.Column(db.String(13), nullable=False)
    add_contract_code = db.Column(db.String(13))
    create_date = db.Column(db.DateTime, nullable=False)
    renew_date = db.Column(db.DateTime, nullable=False)
    operate_cd = db.Column(db.String(128), nullable=False)
    c_flag = db.Column(db.String(1))
    remark = db.Column(db.String(80))
    apply_kind = db.Column(db.String(4), nullable=False)
    prog_status = db.Column(db.String(2), nullable=False)
    apply_date = db.Column(db.DateTime, nullable=False)
    send_plan_date = db.Column(db.DateTime)
    send_date = db.Column(db.DateTime)
    service_kbn = db.Column(db.String(1))
    service_code = db.Column(db.String(8))
    telno = db.Column(db.String(13))
    opt_contract_no = db.Column(db.Numeric(10, 0))


class NttCorBillDtl(db.Model):
    __tablename__ = 'ntt_cor_bill_dtl'

    bill_month = db.Column(db.Date, primary_key=True, nullable=False)
    ws_kbn = db.Column(db.String(2), primary_key=True, nullable=False)
    data_renbn = db.Column(db.Numeric(7, 0), primary_key=True, nullable=False)
    contract_code = db.Column(db.String(13))
    giji_dmd_dtlcd = db.Column(db.String(4))
    dtl_name = db.Column(db.String(320))
    ws_price = db.Column(db.Numeric(7, 1))
    tax_kbn = db.Column(db.String(2))
    dmd_month = db.Column(db.String(6))
    use_start_date = db.Column(db.DateTime)
    use_end_date = db.Column(db.DateTime)
    used_month = db.Column(db.Date, nullable=False)
    contract_no = db.Column(db.String(12))
    user_charge = db.Column(db.Numeric(7, 1))
    taxfree_kbn = db.Column(db.String(1))
    bill_kbn_cd = db.Column(db.String(2))
    opt_plan_cd = db.Column(db.String(8))
    create_date = db.Column(db.DateTime, nullable=False)
    renew_date = db.Column(db.DateTime, nullable=False)
    operate_cd = db.Column(db.String(128), nullable=False)


class NttCorBillMst(db.Model):
    __tablename__ = 'ntt_cor_bill_mst'

    giji_dmd_dtlcd = db.Column(db.String(4), primary_key=True)
    bill_flag = db.Column(db.String(1), nullable=False)
    selling_rate = db.Column(db.Numeric(4, 2))
    bill_kbn_cd = db.Column(db.String(2))
    dtl_context = db.Column(db.String(128))
    create_date = db.Column(db.DateTime, nullable=False)
    renew_date = db.Column(db.DateTime, nullable=False)
    operate_cd = db.Column(db.String(128), nullable=False)


class NttCorChargeDat(db.Model):
    __tablename__ = 'ntt_cor_charge_dat'

    contract_no = db.Column(db.String(12), primary_key=True, nullable=False)
    renbn = db.Column(db.String(3), primary_key=True, nullable=False)
    rating_name = db.Column(db.String(64))
    price = db.Column(db.Numeric(14, 4))
    count = db.Column(db.Numeric(10, 0))
    renew_date = db.Column(db.DateTime, nullable=False)
    create_date = db.Column(db.DateTime, nullable=False)
    operate_cd = db.Column(db.String(128), nullable=False)
    c_flag = db.Column(db.String(1))


class NttCorCont(db.Model):
    __tablename__ = 'ntt_cor_cont'

    contract_no = db.Column(db.String(12), primary_key=True)
    isp_order_no = db.Column(db.String(20))
    renew_date = db.Column(db.DateTime, nullable=False)
    create_date = db.Column(db.DateTime, nullable=False)
    operate_cd = db.Column(db.String(128), nullable=False)
    c_flag = db.Column(db.String(1))
    business_name = db.Column(db.String(3))
    contract_code = db.Column(db.String(13))
    divert_consent_no = db.Column(db.String(11))
    partner_code = db.Column(db.String(18))
    service_name = db.Column(db.String(50))
    service_item = db.Column(db.String(256))
    so = db.Column(db.String(4))
    so_stat = db.Column(db.String(2))
    contractor_name = db.Column(db.String(128))
    contractor_kname = db.Column(db.String(256))
    cur_user_addr_code = db.Column(db.String(802))
    applicationper_name = db.Column(db.String(128))
    contact_phone = db.Column(db.String(13))
    applied_date = db.Column(db.DateTime)
    appoint_date = db.Column(db.DateTime)
    change_date = db.Column(db.DateTime)
    business_contract_start_date = db.Column(db.DateTime)
    contract_end_date = db.Column(db.DateTime)
    flets_contract_start_date = db.Column(db.DateTime)
    ftv_trans_business_name = db.Column(db.String(3))
    indoor_stem_wiring_div = db.Column(db.String(64))
    ftv_business_cont_start_date = db.Column(db.DateTime)
    ftv_business_cont_end_date = db.Column(db.DateTime)
    regular_charge_div = db.Column(db.String(8))
    service_change_code = db.Column(db.String(13))
    operator_ent_name = db.Column(db.String(40))
    operator_cor_branch_name = db.Column(db.String(70))
    operator_cor_section_name = db.Column(db.String(70))
    operator_cor_charge_name = db.Column(db.String(128))
    operator_cor_phone = db.Column(db.String(13))
    operator_cor_fax = db.Column(db.String(13))
    sales_ent_name = db.Column(db.String(40))
    sales_cor_branch_name = db.Column(db.String(70))
    sales_cor_section_name = db.Column(db.String(70))
    sales_cor_chargen_ame = db.Column(db.String(80))
    sales_cor_phone = db.Column(db.String(13))
    sales_cor_fax = db.Column(db.String(12))
    accident_reason = db.Column(db.String(256))
    accident_reason_sub = db.Column(db.String(48))
    date_renewed = db.Column(db.DateTime)
    ritei_status = db.Column(db.String(50))
    ritei_start_date = db.Column(db.DateTime)
    order_no = db.Column(db.String(18))
    arena_so_no = db.Column(db.String(20))
    access_key = db.Column(db.String(8))
    survery_appoint_date = db.Column(db.DateTime)
    survery_appoint_time = db.Column(db.String(256))
    appoint_am_pm = db.Column(db.String(256))
    dispatch_div = db.Column(db.String(256))
    aldivert_flg = db.Column(db.String(1))
    vcast_business_name = db.Column(db.String(30))
    ftvdivertflg = db.Column(db.String(1))
    repflg = db.Column(db.String(1))
    repbusinessname = db.Column(db.String(3))
    repdivertflg = db.Column(db.String(1))
    repbusinessstartdate = db.Column(db.DateTime)
    repbusinessenddate = db.Column(db.DateTime)
    terminal_item_list = db.Column(db.Text)
    charge_list = db.Column(db.Text)
    contact_hope_time_kbn = db.Column(db.String(2))


class NttCorDat(db.Model):
    __tablename__ = 'ntt_cor_dat'

    ws_common_id = db.Column(db.String(20), primary_key=True)
    ws_common_renbn = db.Column(db.String(2), nullable=False)
    contract_no = db.Column(db.String(12), nullable=False, index=True)
    renew_date = db.Column(db.DateTime, nullable=False)
    create_date = db.Column(db.DateTime, nullable=False)
    operate_cd = db.Column(db.String(128), nullable=False)
    c_flag = db.Column(db.String(1))
    remark = db.Column(db.String(80))
    apply_date = db.Column(db.DateTime)
    apply_kind = db.Column(db.String(4), nullable=False)
    prog_status = db.Column(db.String(2), nullable=False)
    send_plan_date = db.Column(db.DateTime)
    send_date = db.Column(db.DateTime)
    service_item = db.Column(db.String(256))
    user_zip = db.Column(db.String(7))
    user_addr = db.Column(db.String(802))
    iten_plan_date = db.Column(db.DateTime)


class NttCorPhoneDtlMst(db.Model):
    __tablename__ = 'ntt_cor_phone_dtl_mst'

    ntt_plan_cd = db.Column(db.String(5), primary_key=True, nullable=False)
    ntt_call_type = db.Column(db.String(4), primary_key=True, nullable=False)
    bill_flag = db.Column(db.String(1), nullable=False)
    selling_rate = db.Column(db.Numeric(4, 2))
    bill_kbn_cd = db.Column(db.String(2))
    create_date = db.Column(db.DateTime, nullable=False)
    renew_date = db.Column(db.DateTime, nullable=False)
    operate_cd = db.Column(db.String(128), nullable=False)


class NttCorTmnDat(db.Model):
    __tablename__ = 'ntt_cor_tmn_dat'

    contract_no = db.Column(db.String(12), primary_key=True, nullable=False)
    renbn = db.Column(db.String(3), primary_key=True, nullable=False)
    terminal_name = db.Column(db.String(128))
    install_date = db.Column(db.DateTime)
    renew_date = db.Column(db.DateTime, nullable=False)
    create_date = db.Column(db.DateTime, nullable=False)
    operate_cd = db.Column(db.String(128), nullable=False)
    c_flag = db.Column(db.String(1))


class NttDat(db.Model):
    __tablename__ = 'ntt_dat'

    ws_common_id = db.Column(db.String(20), primary_key=True)
    ws_common_renbn = db.Column(db.String(2), nullable=False)
    contract_no = db.Column(db.String(12), nullable=False, index=True)
    renew_date = db.Column(db.DateTime, nullable=False)
    create_date = db.Column(db.DateTime, nullable=False)
    operate_cd = db.Column(db.String(128), nullable=False)
    c_flag = db.Column(db.String(1))
    remark = db.Column(db.String(80))
    apply_date = db.Column(db.DateTime)
    apply_kind = db.Column(db.String(4), nullable=False)
    prog_status = db.Column(db.String(2), nullable=False)
    send_plan_date = db.Column(db.DateTime)
    send_date = db.Column(db.DateTime)
    request_id = db.Column(db.String(10))
    est_todohuken = db.Column(db.String(20))
    apply_name = db.Column(db.String(128))
    operator_name = db.Column(db.String(128))
    work_plan_date = db.Column(db.DateTime)
    ntt_plan_date = db.Column(db.DateTime)
    ntt_plan_time = db.Column(db.String(2))
    user_tel1 = db.Column(db.String(13), index=True)
    user_tel2 = db.Column(db.String(13), index=True)
    user_name = db.Column(db.String(128))
    relation = db.Column(db.String(20))
    origin_cd = db.Column(db.String(2))
    note = db.Column(db.String(256))
    cancel_flg = db.Column(db.String(1))
    osm_end_plan_date = db.Column(db.DateTime)
    note2 = db.Column(db.String(16))
    result_cd = db.Column(db.String(64))
    note3 = db.Column(db.String(256))


class NttEwMst(db.Model):
    __tablename__ = 'ntt_ew_mst'

    telno_area = db.Column(db.String(6), primary_key=True, nullable=False)
    telno_pref = db.Column(db.String(4), primary_key=True, nullable=False)
    telno_suff = db.Column(db.String(4), primary_key=True, nullable=False)
    todofuken = db.Column(db.String(8))
    ntt_ew_cd = db.Column(db.String(1))


class NttInfo(db.Model):
    __tablename__ = 'ntt_info'

    contract_no = db.Column(db.String(12), primary_key=True)
    renew_date = db.Column(db.DateTime, nullable=False)
    create_date = db.Column(db.DateTime, nullable=False)
    operate_cd = db.Column(db.String(128), nullable=False)
    c_flag = db.Column(db.String(1))
    remark = db.Column(db.String(80))
    entry_root_cd = db.Column(db.String(1), nullable=False)
    method_cd = db.Column(db.String(3))
    tran_mng_no = db.Column(db.String(16))
    work_plan_date = db.Column(db.DateTime)
    work_plan_time = db.Column(db.String(2))
    consal_plan_date = db.Column(db.DateTime)
    work_date_flg = db.Column(db.String(1))
    telno = db.Column(db.String(10))
    ntt_e_cont_id = db.Column(db.String(16))
    cont_lastname = db.Column(db.String(20))
    cont_firstname = db.Column(db.String(20))
    cont_lastname_k = db.Column(db.String(20))
    cont_firstname_k = db.Column(db.String(20))
    apply_name = db.Column(db.String(128))
    apply_name_k = db.Column(db.String(256))
    apply_cd = db.Column(db.String(1))
    contact_cd = db.Column(db.String(1))
    telno2 = db.Column(db.String(11))
    email = db.Column(db.String(50))
    a_cd = db.Column(db.String(1))
    b_cd = db.Column(db.String(1))
    c_cd = db.Column(db.String(1))
    d_cd = db.Column(db.String(1))
    note2 = db.Column(db.String(400))
    partner_cd = db.Column(db.String(10))
    corp_name = db.Column(db.String(60))
    corp_kana = db.Column(db.String(60))
    corp_post_name = db.Column(db.String(60))
    user_zip = db.Column(db.String(7))
    user_todohuken = db.Column(db.String(256))
    user_ku = db.Column(db.String(256))
    user_area = db.Column(db.String(256))
    user_chome = db.Column(db.String(256))
    user_banchi = db.Column(db.String(160))
    user_build_name = db.Column(db.String(80))
    user_addr_note = db.Column(db.String(200))
    send_zip = db.Column(db.String(7))
    send_todohuken = db.Column(db.String(256))
    send_ku = db.Column(db.String(256))
    send_area = db.Column(db.String(256))
    send_chome = db.Column(db.String(256))
    send_banchi = db.Column(db.String(160))
    send_build_name = db.Column(db.String(80))
    send_addr_note = db.Column(db.String(200))
    send_name = db.Column(db.String(128))
    send_name_k = db.Column(db.String(256))
    send_person = db.Column(db.String(128))
    ntt_branch_name = db.Column(db.String(64))
    ntt_position_name = db.Column(db.String(128))
    ntt_sales_agency_cd = db.Column(db.String(8))
    ntt_charge_name = db.Column(db.String(128))
    ntt_charge_cd = db.Column(db.String(8))
    ntt_charge_telno = db.Column(db.String(13))
    ntt_charge_fax = db.Column(db.String(13))
    ntt_charge_mail = db.Column(db.String(60))
    ntt_isp_apply_kbn = db.Column(db.String(20))
    ntt_service_name = db.Column(db.String(64))
    ntt_bf_exist_type = db.Column(db.String(4))
    ntt_isp_user_id = db.Column(db.String(60))
    ntt_isp_mail = db.Column(db.String(60))
    banpo_flg = db.Column(db.String(1))
    double_contract_flag = db.Column(db.String(64))
    name_admin_flag = db.Column(db.String(64))
    cont_address_code = db.Column(db.String(15))
    cont_address_revision = db.Column(db.String(10))
    fax = db.Column(db.String(13))
    address_code = db.Column(db.String(11))
    partner_serial_no = db.Column(db.String(16))
    user_banchi1 = db.Column(db.String(40))
    user_banchi2 = db.Column(db.String(20))
    user_banchi3 = db.Column(db.String(20))
    work_witness_name = db.Column(db.String(20))
    work_witness_contact_cd = db.Column(db.String(1))
    work_witness_telno = db.Column(db.String(11))
    use_access_line = db.Column(db.String(1))
    use_ntt_flets_service = db.Column(db.String(3))
    other_companies_contract = db.Column(db.String(1))
    other_companies_service = db.Column(db.String(1))
    interior_wiring_cd = db.Column(db.String(1))
    wiring_work_cd = db.Column(db.String(1))
    tel_directory_carry_cd = db.Column(db.String(1))
    vcast_contractor_sex_type = db.Column(db.String(1))
    vcast_contractor_birth = db.Column(db.DateTime)
    connect_tv_const = db.Column(db.String(1))
    tv_set_construct_type = db.Column(db.String(1))
    cs_channel_pack1 = db.Column(db.String(1))
    cs_digital_tuner1 = db.Column(db.String(1))
    cs_channel_pack2 = db.Column(db.String(1))
    cs_digital_tuner2 = db.Column(db.String(1))
    cs_channel_pack3 = db.Column(db.String(1))
    cs_digital_tuner3 = db.Column(db.String(1))
    possession_cd = db.Column(db.String(1))
    number_of_house = db.Column(db.String(1))
    house_cd = db.Column(db.String(1))
    work_witness_cd = db.Column(db.String(1))
    ipv6connectmethod = db.Column(db.String(64))
    adapterinfo = db.Column(db.String(64))
    fm_possession_cd = db.Column(db.String(1))
    ntt_birth = db.Column(db.DateTime)
    ntt_sex_type = db.Column(db.String(1))


class NttItemDat(db.Model):
    __tablename__ = 'ntt_item_dat'

    contract_no = db.Column(db.String(12), primary_key=True, nullable=False)
    item_no = db.Column(db.String(2), primary_key=True, nullable=False)
    renew_date = db.Column(db.DateTime, nullable=False)
    create_date = db.Column(db.DateTime, nullable=False)
    operate_cd = db.Column(db.String(128), nullable=False)
    c_flag = db.Column(db.String(1))
    apply_flg = db.Column(db.String(1), nullable=False)


class NttItemMst(db.Model):
    __tablename__ = 'ntt_item_mst'

    item_no = db.Column(db.String(2), primary_key=True)
    item_name = db.Column(db.String(256), nullable=False)
    use_status = db.Column(db.String(1), nullable=False)
    renew_date = db.Column(db.DateTime, nullable=False)
    create_date = db.Column(db.DateTime, nullable=False)
    operate_cd = db.Column(db.String(128), nullable=False)
    c_flag = db.Column(db.String(1))


class NttOsmdb(db.Model):
    __tablename__ = 'ntt_osmdb'

    contract_no = db.Column(db.String(12), primary_key=True)
    isp_order_no = db.Column(db.String(16))
    renew_date = db.Column(db.DateTime, nullable=False)
    create_date = db.Column(db.DateTime, nullable=False)
    operate_cd = db.Column(db.String(128), nullable=False)
    c_flag = db.Column(db.String(1))
    ntt_e_cont_id = db.Column(db.String(16))
    apply_name = db.Column(db.String(128))
    telno = db.Column(db.String(14), index=True)
    osm_apply_date = db.Column(db.DateTime)
    item_name = db.Column(db.String(128))
    item_detail_name = db.Column(db.String(32))
    item_term_name = db.Column(db.String(50))
    work_plan_date = db.Column(db.DateTime)
    work_plan_time = db.Column(db.String(40))
    osm_entry_cd = db.Column(db.String(10))
    osm_status = db.Column(db.String(5))
    osm_sub_status = db.Column(db.String(5))
    osm_start_date = db.Column(db.DateTime)
    osm_end_yyyymm = db.Column(db.DateTime)
    branch_name = db.Column(db.String(20))
    mainte_plan = db.Column(db.String(16))
    model_name = db.Column(db.String(512))
    model_num = db.Column(db.String(128))
    partner_cd = db.Column(db.String(10))
    osm_create_date = db.Column(db.DateTime)
    branch_telno = db.Column(db.String(14))
    consal_plan_date = db.Column(db.DateTime)
    ntt_e_agency_cd = db.Column(db.String(8))
    sales_store_name = db.Column(db.String(128))
    section_name = db.Column(db.String(128))
    charge_cd = db.Column(db.String(8))
    charge_name = db.Column(db.String(128))
    osm_renew_date = db.Column(db.DateTime)
    change_item_name = db.Column(db.String(128))
    application_no = db.Column(db.String(16))
    ntt_e_cont_start_date = db.Column(db.DateTime)
    outside_bill_start_date = db.Column(db.DateTime)
    inside_bill_start_date = db.Column(db.DateTime)
    outside_work_plan_date = db.Column(db.DateTime)
    inside_work_plan_date = db.Column(db.DateTime)
    accident_reason = db.Column(db.String(256))
    accident_status = db.Column(db.String(256))
    cancel_reason = db.Column(db.String(256))
    mainte_info = db.Column(db.String(128))
    campaign = db.Column(db.String(64))
    bill_end_date = db.Column(db.DateTime)
    end_reason = db.Column(db.String(256))
    osa_set_cd = db.Column(db.String(2))
    osa_cancel_cd = db.Column(db.String(256))
    change_item_detail_name = db.Column(db.String(32))
    change_id_no = db.Column(db.String(64))
    hgw_mainte_info = db.Column(db.String(32))
    hgw_model_name = db.Column(db.String(128))
    item_change_bill_date = db.Column(db.DateTime)
    mng_id = db.Column(db.String(25))
    cp_start_date = db.Column(db.DateTime)
    cp_end_date = db.Column(db.DateTime)
    bill_start_date = db.Column(db.DateTime)
    consal_status = db.Column(db.String(50))
    osm_flg = db.Column(db.String(1))
    osm2_start_date = db.Column(db.DateTime)
    osm2_end_yyyymm = db.Column(db.DateTime)


class NttPartnerMst(db.Model):
    __tablename__ = 'ntt_partner_mst'

    plan_cd = db.Column(db.String(8), primary_key=True, nullable=False)
    partner_cd = db.Column(db.String(10), primary_key=True, nullable=False)
    status = db.Column(db.String(1), nullable=False)


t_ntt_result = db.Table(
    'ntt_result',
    db.Column('dmdto_id', db.String(12), nullable=False),
    db.Column('ntt_result_cre_date', db.DateTime, nullable=False),
    db.Column('create_date', db.DateTime, nullable=False),
    db.Column('renew_date', db.DateTime, nullable=False),
    db.Column('operate_cd', db.String(128), nullable=False),
    db.Column('dmd_no', db.String(13)),
    db.Column('result_kind', db.String(1)),
    db.Column('result_cd', db.String(11)),
    db.Column('ntt_apply_date', db.DateTime)
)


class NttfResultMng(db.Model):
    __tablename__ = 'nttf_result_mng'

    import_date = db.Column(db.String(14), primary_key=True, nullable=False)
    line_no = db.Column(db.Numeric(6, 0), primary_key=True, nullable=False)
    create_date = db.Column(db.DateTime, nullable=False)
    renew_date = db.Column(db.DateTime, nullable=False)
    operate_cd = db.Column(db.String(128), nullable=False)
    collection_kbn = db.Column(db.String(1))
    result_reflect_kbn = db.Column(db.String(1), nullable=False)
    dmd_no = db.Column(db.String(13))
    dmdto_id = db.Column(db.String(12))
    result_flag = db.Column(db.String(2))
    cvs_flag = db.Column(db.String(1), nullable=False, server_default=db.FetchedValue())
    payment_date = db.Column(db.DateTime)
    member_id = db.Column(db.String(12))
    chg_dmdto_valid_date = db.Column(db.DateTime)
    chg_dmd_kbn_flag = db.Column(db.String(1), nullable=False, server_default=db.FetchedValue())
    ng_rsn = db.Column(db.String(3))
    dmd_status = db.Column(db.String(2))
    pay_chg_rsn = db.Column(db.String(2))
    incident_conf_key = db.Column(db.String(15))
    mail_send_key = db.Column(db.String(32))
    document_id = db.Column(db.String(32))
    use_month = db.Column(db.String(30))
    err_proc_status = db.Column(db.String(1), nullable=False, server_default=db.FetchedValue())
    demand_mny = db.Column(db.Numeric(10, 0))


class NttplayerCont(db.Model):
    __tablename__ = 'nttplayer_cont'

    contract_no = db.Column(db.String(12), primary_key=True)
    isp_order_no = db.Column(db.String(20))
    renew_date = db.Column(db.DateTime, nullable=False)
    create_date = db.Column(db.DateTime, nullable=False)
    operate_cd = db.Column(db.String(128), nullable=False)
    c_flag = db.Column(db.String(1))
    service_name = db.Column(db.String(40))
    item_name = db.Column(db.String(128))
    order_status = db.Column(db.String(40))
    work_plan_date = db.Column(db.DateTime)
    ntt_e_cont_id_pr = db.Column(db.String(13))
    item_term_name = db.Column(db.String(1536))
    apply_kbn = db.Column(db.String(40))
    ntt_e_cont_id = db.Column(db.String(13))
    divert_consent_no = db.Column(db.String(11))
    ntt_ew_kind = db.Column(db.String(40))
    nttplayer_cont_id = db.Column(db.String(12))
    user_name = db.Column(db.String(240))
    user_name_k = db.Column(db.String(480))
    user_address = db.Column(db.String(2142))
    isp_name = db.Column(db.String(60))
    isp_status = db.Column(db.String(2))
    nttplayer_start_end_date = db.Column(db.DateTime)
    isp_start_end_date = db.Column(db.DateTime)
    nttplayer_cont_name = db.Column(db.String(60))
    nttplayer_cont_name_k = db.Column(db.String(100))
    nttplayer_cont_telno = db.Column(db.String(72))
    nttplayer_cont_telno2 = db.Column(db.String(11))
    nttplayer_cont_zip = db.Column(db.String(7))
    nttplayer_cont_address = db.Column(db.String(200))
    nttplayer_cont_birth = db.Column(db.DateTime)
    penalty_cost_flag = db.Column(db.String(2))
    flets_cont_name = db.Column(db.String(480))
    flets_cont_telno = db.Column(db.String(72))


class NttplayerDat(db.Model):
    __tablename__ = 'nttplayer_dat'

    ws_common_id = db.Column(db.String(20), primary_key=True)
    ws_common_renbn = db.Column(db.String(2), nullable=False)
    contract_no = db.Column(db.String(12), nullable=False, index=True)
    renew_date = db.Column(db.DateTime, nullable=False)
    create_date = db.Column(db.DateTime, nullable=False)
    operate_cd = db.Column(db.String(128), nullable=False)
    c_flag = db.Column(db.String(1))
    remark = db.Column(db.String(80))
    apply_date = db.Column(db.DateTime)
    apply_kind = db.Column(db.String(4), nullable=False)
    prog_status = db.Column(db.String(2), nullable=False)
    send_plan_date = db.Column(db.DateTime)
    send_date = db.Column(db.DateTime)
    nttplayer_order_no = db.Column(db.String(17), nullable=False)
    isp_receipt_result = db.Column(db.String(2))
    isp_receipt_err_cd = db.Column(db.String(2))
    isp_receipt_err_reason = db.Column(db.String(1536))
    isp_service_order_status = db.Column(db.String(2))
    stop_reason = db.Column(db.String(1536))
    isp_biko = db.Column(db.String(2))
    isp_confirm_date = db.Column(db.DateTime)


class OldIspMst(db.Model):
    __tablename__ = 'old_isp_mst'

    old_isp = db.Column(db.String(3), primary_key=True)
    renew_date = db.Column(db.DateTime, nullable=False)
    create_date = db.Column(db.DateTime, nullable=False)
    operate_cd = db.Column(db.String(128), nullable=False)
    old_isp_name = db.Column(db.String(80))
    old_isp_name_fe = db.Column(db.String(40))


t_operator_auth_mst = db.Table(
    'operator_auth_mst',
    db.Column('task', db.String(128), nullable=False),
    db.Column('auth', db.String(128), nullable=False)
)


class OperatorMst(db.Model):
    __tablename__ = 'operator_mst'

    operator_cd = db.Column(db.String(128), primary_key=True)
    operator_pass = db.Column(db.String(16))
    auth_time = db.Column(db.Numeric(3, 0), nullable=False)
    pass_enddate = db.Column(db.DateTime, nullable=False)
    ope_status = db.Column(db.String(1), nullable=False)
    create_date = db.Column(db.DateTime, nullable=False)
    renew_date = db.Column(db.DateTime, nullable=False)
    operate_cd = db.Column(db.String(128), nullable=False)


t_operator_task_mst = db.Table(
    'operator_task_mst',
    db.Column('operator_cd', db.String(128), nullable=False),
    db.Column('task', db.String(128), nullable=False)
)


class OptPlanRelMst(db.Model):
    __tablename__ = 'opt_plan_rel_mst'

    opt_plan_cd = db.Column(db.String(8), primary_key=True, nullable=False)
    rel_opt_plan_cd = db.Column(db.String(8), primary_key=True, nullable=False)
    rel_opt_flag = db.Column(db.String(1))
    create_date = db.Column(db.DateTime, nullable=False)
    renew_date = db.Column(db.DateTime, nullable=False)
    operate_cd = db.Column(db.String(128), nullable=False)
    c_flag = db.Column(db.String(1))


t_pg_all_foreign_keys = db.Table(
    'pg_all_foreign_keys',
    db.Column('fk_schema_name', db.String),
    db.Column('fk_table_name', db.String),
    db.Column('fk_constraint_name', db.String),
    db.Column('fk_table_oid', db.OID),
    db.Column('fk_columns', db.ARRAY(String())),
    db.Column('pk_schema_name', db.String),
    db.Column('pk_table_name', db.String),
    db.Column('pk_constraint_name', db.String),
    db.Column('pk_table_oid', db.OID),
    db.Column('pk_index_name', db.String),
    db.Column('pk_columns', db.ARRAY(String())),
    db.Column('match_type', db.Text),
    db.Column('on_delete', db.Text),
    db.Column('on_update', db.Text),
    db.Column('is_deferrable', db.Boolean),
    db.Column('is_deferred', db.Boolean)
)


class PlanChgMst(db.Model):
    __tablename__ = 'plan_chg_mst'

    src_plan_cd = db.Column(db.String(8), primary_key=True, nullable=False)
    dst_plan_cd = db.Column(db.String(8), primary_key=True, nullable=False)
    rel_flag = db.Column(db.String(1), nullable=False)
    disc_cd1 = db.Column(db.String(1), nullable=False)
    disc_cd2 = db.Column(db.String(3))
    disc_cd3 = db.Column(db.String(3))
    disc_cd4 = db.Column(db.String(3))
    disc_cd5 = db.Column(db.String(3))
    disc_cd6 = db.Column(db.String(3))
    disc_cd7 = db.Column(db.String(3))
    disc_cd8 = db.Column(db.String(3))
    create_date = db.Column(db.DateTime, nullable=False)
    renew_date = db.Column(db.DateTime, nullable=False)
    operate_cd = db.Column(db.String(128), nullable=False)
    c_flag = db.Column(db.String(1))


class PlanMst(db.Model):
    __tablename__ = 'plan_mst'

    plan_cd = db.Column(db.String(8), primary_key=True)
    plan_name = db.Column(db.String(128), nullable=False)
    plan_short = db.Column(db.String(128))
    plan_kind = db.Column(db.String(1), nullable=False)
    plan_status = db.Column(db.String(1), nullable=False)
    initial_cost = db.Column(db.Numeric(8, 0))
    first_service_cost = db.Column(db.Numeric(8, 0))
    service_cost = db.Column(db.Numeric(8, 0))
    work_cost = db.Column(db.Numeric(8, 0))
    taxfree_kbn = db.Column(db.String(1), nullable=False)
    dialup = db.Column(db.String(4))
    roaming = db.Column(db.String(4))
    mobilepoint = db.Column(db.String(4))
    service_dmt_name = db.Column(db.String(128))
    disc_mail_n = db.Column(db.Numeric(2, 0), nullable=False, server_default=db.FetchedValue())
    disc_cd_mail = db.Column(db.String(3))
    disc_cd_homepage = db.Column(db.String(3))
    plan_term = db.Column(db.Numeric(2, 0))
    create_date = db.Column(db.DateTime, nullable=False)
    renew_date = db.Column(db.DateTime, nullable=False)
    operate_cd = db.Column(db.String(128), nullable=False)
    c_flag = db.Column(db.String(1))
    penalty_cost = db.Column(db.Numeric(8, 0))
    max_penalty_month = db.Column(db.Numeric(2, 0))
    service_cycle_month = db.Column(db.Numeric(2, 0))
    creditor_cd = db.Column(db.String(1), nullable=False, server_default=db.FetchedValue())
    creditor_subcd = db.Column(db.String(3))
    penalty_taxfree_kbn = db.Column(db.String(1), nullable=False, server_default=db.FetchedValue())
    volume_discount_cd = db.Column(db.String(2))
    append_penalty_cost = db.Column(db.Numeric(8, 0), nullable=False, server_default=db.FetchedValue())
    stat_initial_cost = db.Column(db.Numeric(8, 0))
    stat_service_cost = db.Column(db.Numeric(8, 0))
    aplus_initial_cost = db.Column(db.Numeric(8, 0))


class PlanRelMst(db.Model):
    __tablename__ = 'plan_rel_mst'

    plan_cd = db.Column(db.String(8), primary_key=True, nullable=False)
    rel_plan_cd = db.Column(db.String(8), primary_key=True, nullable=False)
    rel_flag = db.Column(db.String(1))
    create_date = db.Column(db.DateTime, nullable=False)
    renew_date = db.Column(db.DateTime, nullable=False)
    operate_cd = db.Column(db.String(128), nullable=False)
    c_flag = db.Column(db.String(1))


class PppInfo(db.Model):
    __tablename__ = 'ppp_info'

    account_id = db.Column(db.String(64), primary_key=True, nullable=False)
    bill_kbn_cd = db.Column(db.String(2), primary_key=True, nullable=False)
    used_month = db.Column(db.Date, primary_key=True, nullable=False)
    bill_month = db.Column(db.Date, nullable=False, index=True)
    use_minute = db.Column(db.Numeric(7, 0))
    use_day = db.Column(db.Numeric(2, 0), nullable=False)
    create_date = db.Column(db.DateTime, nullable=False)
    renew_date = db.Column(db.DateTime, nullable=False)
    operate_cd = db.Column(db.String(128), nullable=False)
    c_flag = db.Column(db.String(1))


class PrefixDat(db.Model):
    __tablename__ = 'prefix_dat'

    ws_common_id = db.Column(db.String(20), primary_key=True)
    ws_common_renbn = db.Column(db.String(2), nullable=False)
    opt_contract_no = db.Column(db.Numeric(10, 0), nullable=False)
    process_kbn = db.Column(db.String(6), nullable=False)
    msisdn = db.Column(db.String(11))
    contbase_no = db.Column(db.String(10), nullable=False)
    exec_plan = db.Column(db.String(1), nullable=False)
    prefix_cd = db.Column(db.String(20))
    apply_kind = db.Column(db.String(4), nullable=False)
    prog_status = db.Column(db.String(2), nullable=False)
    send_plan_date = db.Column(db.DateTime)
    send_date = db.Column(db.DateTime)
    result_cd = db.Column(db.String(2))
    result_status = db.Column(db.String(2))
    create_date = db.Column(db.DateTime, nullable=False)
    renew_date = db.Column(db.DateTime, nullable=False)
    operate_cd = db.Column(db.String(128), nullable=False)
    c_flag = db.Column(db.String(1))


class Privilege(db.Model):
    __tablename__ = 'privilege'

    customer_id = db.Column(db.String(8), primary_key=True)
    grant_date = db.Column(db.DateTime, nullable=False)
    stage = db.Column(db.String(1), nullable=False)
    used = db.Column(db.String(1), nullable=False)
    unchanged = db.Column(db.String(1), nullable=False)
    create_date = db.Column(db.DateTime, nullable=False)
    renew_date = db.Column(db.DateTime, nullable=False)
    operate_cd = db.Column(db.String(128), nullable=False)


class Pt2codeMst(db.Model):
    __tablename__ = 'pt2code_mst'

    pt2_plancd = db.Column(db.String(32), primary_key=True)
    quota_size = db.Column(db.Numeric(10, 0), nullable=False)
    quota_carryforward_kbn = db.Column(db.String(1), nullable=False)
    apn = db.Column(db.String(50), nullable=False)
    monthly_charge_kbn = db.Column(db.String(1), nullable=False)
    create_date = db.Column(db.DateTime, nullable=False)
    renew_date = db.Column(db.DateTime, nullable=False)
    operate_cd = db.Column(db.String(128), nullable=False)


t_sales_customer_total = db.Table(
    'sales_customer_total',
    db.Column('sales_month', db.String(6), nullable=False),
    db.Column('customer_id', db.String(8), nullable=False),
    db.Column('creditor_cd', db.String(1), nullable=False),
    db.Column('creditor_subcd', db.String(3)),
    db.Column('taxable_total', db.Numeric(10, 0), nullable=False, server_default=db.FetchedValue()),
    db.Column('taxfree_total', db.Numeric(10, 0), nullable=False, server_default=db.FetchedValue()),
    db.Column('tax_total', db.Numeric(10, 0), nullable=False, server_default=db.FetchedValue()),
    db.Column('tax_percent', db.Numeric(4, 1), nullable=False),
    db.Index('idx_sales_customer_total_01', 'sales_month', 'customer_id', 'creditor_cd', 'creditor_subcd', 'tax_percent')
)


class SalesDetail(db.Model):
    __tablename__ = 'sales_detail'

    dmd_no = db.Column(db.String(13), primary_key=True, nullable=False)
    dmd_detailno = db.Column(db.Numeric(5, 0), primary_key=True, nullable=False)
    customer_id = db.Column(db.String(8), index=True)
    contract_no = db.Column(db.String(12))
    opt_contract_no = db.Column(db.Numeric(10, 0))
    plan_cd = db.Column(db.String(8))
    disc_type = db.Column(db.String(2))
    disc_cd = db.Column(db.String(3))
    bill_kbn_cd = db.Column(db.String(2))
    plan_content = db.Column(db.String(160))
    quantity = db.Column(db.Numeric(19, 0))
    unit = db.Column(db.String(10))
    unit_cost = db.Column(db.Numeric(10, 4))
    tax_cost = db.Column(db.Numeric(9, 0))
    account_id = db.Column(db.String(64))
    detail_kbn = db.Column(db.String(1))
    adjust_renban = db.Column(db.Numeric(9, 0))
    cost = db.Column(db.Numeric(9, 0), nullable=False)
    taxfree_kbn = db.Column(db.String(1), nullable=False)
    kihon_tuika_kbn = db.Column(db.String(1))
    create_date = db.Column(db.DateTime, nullable=False)
    renew_date = db.Column(db.DateTime, nullable=False)
    operate_cd = db.Column(db.String(128), nullable=False)
    c_flag = db.Column(db.String(1))
    creditor_cd = db.Column(db.String(1), nullable=False)
    kddi_plan_cd = db.Column(db.String(10))
    ntt_plan_cd = db.Column(db.String(10))
    creditor_subcd = db.Column(db.String(3))
    sales_dmd_kbn = db.Column(db.String(1))
    demand_count = db.Column(db.Numeric(2, 0))
    jpayment_trade_no = db.Column(db.String(64))
    bill_start = db.Column(db.DateTime)
    bill_end = db.Column(db.DateTime)
    tax_percent = db.Column(db.Numeric(4, 1))


t_sales_dmdto_total = db.Table(
    'sales_dmdto_total',
    db.Column('dmd_no', db.String(13), nullable=False),
    db.Column('creditor_cd', db.String(1), nullable=False),
    db.Column('creditor_subcd', db.String(3)),
    db.Column('taxable_total', db.Numeric(10, 0), nullable=False, server_default=db.FetchedValue()),
    db.Column('taxfree_total', db.Numeric(10, 0), nullable=False, server_default=db.FetchedValue()),
    db.Column('tax_total', db.Numeric(10, 0), nullable=False, server_default=db.FetchedValue()),
    db.Column('tax_percent', db.Numeric(4, 1), nullable=False),
    db.Index('idx_sales_dmdto_total_01', 'dmd_no', 'creditor_cd', 'creditor_subcd', 'tax_percent')
)


class SalesHeader(db.Model):
    __tablename__ = 'sales_header'
    __table_args__ = (
        db.Index('idx_sales_header_01', 'sales_month', 'dmdto_id'),
    )

    dmd_no = db.Column(db.String(13), primary_key=True)
    sales_month = db.Column(db.String(6), nullable=False)
    dmdto_id = db.Column(db.String(12), nullable=False)
    slip_kbn = db.Column(db.String(1))
    dmd_no2 = db.Column(db.String(13))
    slip_reason = db.Column(db.String(2))


class SalesShiftDetail(db.Model):
    __tablename__ = 'sales_shift_detail'

    create_date = db.Column(db.DateTime, nullable=False)
    renew_date = db.Column(db.DateTime, nullable=False)
    operate_cd = db.Column(db.String(128), nullable=False)
    c_flag = db.Column(db.String(1))
    org_dmd_month = db.Column(db.Date, primary_key=True, nullable=False)
    plan_dmd_month = db.Column(db.Date)
    dmdto_id = db.Column(db.String(12), primary_key=True, nullable=False)
    customer_id = db.Column(db.String(8), primary_key=True, nullable=False)
    contract_no = db.Column(db.String(12), primary_key=True, nullable=False)
    bill_detailno = db.Column(db.Numeric(5, 0), primary_key=True, nullable=False)
    opt_contract_no = db.Column(db.Numeric(10, 0))
    plan_cd = db.Column(db.String(8))
    disc_type = db.Column(db.String(2))
    disc_cd = db.Column(db.String(3))
    bill_kbn_cd = db.Column(db.String(2), nullable=False)
    bill_start = db.Column(db.DateTime, nullable=False)
    bill_end = db.Column(db.DateTime)
    quantity = db.Column(db.Numeric(19, 0))
    unit = db.Column(db.String(10))
    unit_cost = db.Column(db.Numeric(10, 4))
    tax_cost = db.Column(db.Numeric(9, 0))
    account_id = db.Column(db.String(64))
    adjust_renban = db.Column(db.Numeric(9, 0))
    cost = db.Column(db.Numeric(9, 0), nullable=False, server_default=db.FetchedValue())
    taxfree_kbn = db.Column(db.String(1), nullable=False)
    kihon_tuika_kbn = db.Column(db.String(1))
    kddi_plan_cd = db.Column(db.String(10))
    plan_name = db.Column(db.String(128))
    creditor_cd = db.Column(db.String(1), nullable=False, server_default=db.FetchedValue())
    ntt_plan_cd = db.Column(db.String(10))
    creditor_subcd = db.Column(db.String(3))
    tax_percent = db.Column(db.Numeric(4, 1))


class SalesShiftTotal(db.Model):
    __tablename__ = 'sales_shift_total'

    create_date = db.Column(db.DateTime, nullable=False)
    renew_date = db.Column(db.DateTime, nullable=False)
    operate_cd = db.Column(db.String(128), nullable=False)
    c_flag = db.Column(db.String(1))
    contract_no = db.Column(db.String(12), primary_key=True, nullable=False)
    used_month = db.Column(db.Date, primary_key=True, nullable=False)
    org_dmd_month = db.Column(db.Date, nullable=False)
    plan_dmd_month = db.Column(db.Date)
    dmdto_id = db.Column(db.String(12), nullable=False)
    kddi_taxable_total = db.Column(db.Numeric(10, 0), nullable=False, server_default=db.FetchedValue())
    kddi_taxfree_total = db.Column(db.Numeric(10, 0), nullable=False, server_default=db.FetchedValue())
    kddi_tax = db.Column(db.Numeric(10, 0), nullable=False, server_default=db.FetchedValue())
    collection_taxable_total = db.Column(db.Numeric(10, 0), nullable=False, server_default=db.FetchedValue())
    collection_taxin_total = db.Column(db.Numeric(10, 0), nullable=False, server_default=db.FetchedValue())
    ntt_e_taxable_total = db.Column(db.Numeric(10, 0), nullable=False, server_default=db.FetchedValue())
    ntt_e_taxfree_total = db.Column(db.Numeric(10, 0), nullable=False, server_default=db.FetchedValue())
    ntt_e_tax_total = db.Column(db.Numeric(10, 0), nullable=False, server_default=db.FetchedValue())
    ntt_w_taxable_total = db.Column(db.Numeric(10, 0), nullable=False, server_default=db.FetchedValue())
    ntt_w_taxfree_total = db.Column(db.Numeric(10, 0), nullable=False, server_default=db.FetchedValue())
    ntt_w_tax_total = db.Column(db.Numeric(10, 0), nullable=False, server_default=db.FetchedValue())


class SalesTotal(db.Model):
    __tablename__ = 'sales_total'
    __table_args__ = (
        db.Index('idx_sales_total_01', 'dmd_month', 'dmdto_id'),
    )

    dmd_no = db.Column(db.String(13), primary_key=True)
    dmd_month = db.Column(db.String(6))
    dmdto_id = db.Column(db.String(12), index=True)
    taxable_total = db.Column(db.Numeric(10, 0))
    taxfree_total = db.Column(db.Numeric(10, 0))
    tax = db.Column(db.Numeric(10, 0))
    all_total = db.Column(db.Numeric(10, 0))
    slip_kbn = db.Column(db.String(1))
    dmd_no2 = db.Column(db.String(13), index=True)
    dmd_status = db.Column(db.String(2))
    demand_kbn = db.Column(db.String(2), nullable=False)
    payment_kbn = db.Column(db.String(2))
    payment_date = db.Column(db.DateTime)
    result_cd = db.Column(db.String(2))
    receipt_sts = db.Column(db.String(1))
    all_receive_mny = db.Column(db.Numeric(10, 0))
    receive_mny = db.Column(db.Numeric(10, 0))
    deficiency = db.Column(db.Numeric(10, 0))
    detail_kbn = db.Column(db.String(2), nullable=False)
    detail_rsn = db.Column(db.String(255))
    pwd_demandprint_kbn = db.Column(db.String(1), nullable=False)
    cardkind = db.Column(db.String(2))
    cardno = db.Column(db.String(16))
    cardvalid = db.Column(db.String(6))
    verify_no = db.Column(db.String(8))
    verify_money = db.Column(db.Numeric(8, 0))
    verify_date = db.Column(db.DateTime)
    agreement = db.Column(db.String(1))
    pwd_stro_cd = db.Column(db.String(1))
    trans_bankcd = db.Column(db.String(4))
    trans_branchcd = db.Column(db.String(3))
    trans_linecd = db.Column(db.String(1))
    trans_acckind = db.Column(db.String(1))
    trans_accno = db.Column(db.String(7))
    trans_accname = db.Column(db.String(60))
    kobetu_bankcd = db.Column(db.String(4))
    kobetu_branchcd = db.Column(db.String(3))
    kobetu_linecd = db.Column(db.String(1))
    kobetu_acckind = db.Column(db.String(1))
    kobetu_accno = db.Column(db.String(7))
    kobetu_accname = db.Column(db.String(60))
    dmdto_memo = db.Column(db.String(128))
    payment_memo = db.Column(db.String(64))
    slip_reason = db.Column(db.String(2), nullable=False)
    create_date = db.Column(db.DateTime, nullable=False)
    renew_date = db.Column(db.DateTime, nullable=False)
    operate_cd = db.Column(db.String(128), nullable=False)
    c_flag = db.Column(db.String(1))
    kddi_taxable_total = db.Column(db.Numeric(10, 0), nullable=False, server_default=db.FetchedValue())
    kddi_taxfree_total = db.Column(db.Numeric(10, 0), nullable=False, server_default=db.FetchedValue())
    kddi_tax = db.Column(db.Numeric(10, 0), nullable=False, server_default=db.FetchedValue())
    collection_taxable_total = db.Column(db.Numeric(10, 0), nullable=False, server_default=db.FetchedValue())
    collection_taxin_total = db.Column(db.Numeric(10, 0), nullable=False, server_default=db.FetchedValue())
    ntt_e_taxable_total = db.Column(db.Numeric(10, 0), nullable=False, server_default=db.FetchedValue())
    ntt_e_taxfree_total = db.Column(db.Numeric(10, 0), nullable=False, server_default=db.FetchedValue())
    ntt_e_tax_total = db.Column(db.Numeric(10, 0), nullable=False, server_default=db.FetchedValue())
    ntt_limit_date = db.Column(db.DateTime)
    ntt_w_taxable_total = db.Column(db.Numeric(10, 0), nullable=False, server_default=db.FetchedValue())
    ntt_w_taxfree_total = db.Column(db.Numeric(10, 0), nullable=False, server_default=db.FetchedValue())
    ntt_w_tax_total = db.Column(db.Numeric(10, 0), nullable=False, server_default=db.FetchedValue())
    cvs_service_stop_plan = db.Column(db.DateTime)
    cvs_change_date = db.Column(db.DateTime)
    cvs_payment_mny = db.Column(db.Numeric(10, 0))
    cvs_payment_date = db.Column(db.DateTime)
    cvs_payment_cancel_date = db.Column(db.DateTime)
    other_taxable_total = db.Column(db.Numeric(10, 0), nullable=False, server_default=db.FetchedValue())
    other_taxfree_total = db.Column(db.Numeric(10, 0), nullable=False, server_default=db.FetchedValue())
    other_tax_total = db.Column(db.Numeric(10, 0), nullable=False, server_default=db.FetchedValue())
    use_aim = db.Column(db.Numeric(1, 0))
    ec_receipt_no = db.Column(db.String(22))
    stat_kbn = db.Column(db.Numeric(1, 0))


class SalesTotalDfCooperation(db.Model):
    __tablename__ = 'sales_total_df_cooperation'

    dmd_no = db.Column(db.String(13), primary_key=True)
    dmd_month = db.Column(db.String(6))
    dmdto_id = db.Column(db.String(12))
    cst_no = db.Column(db.String(20))
    all_total = db.Column(db.Numeric(10, 0))
    dmd_status = db.Column(db.String(2))
    result_cd = db.Column(db.String(2))
    payment_date = db.Column(db.DateTime)
    receive_mny = db.Column(db.Numeric(10, 0))
    cust_user_type = db.Column(db.String(1), nullable=False)
    cardno = db.Column(db.String(16))
    trans_bankcd = db.Column(db.String(4))
    trans_branchcd = db.Column(db.String(3))
    trans_linecd = db.Column(db.String(1))
    trans_acckind = db.Column(db.String(1))
    trans_accno = db.Column(db.String(7))
    trans_accname = db.Column(db.String(60))
    dfsend_amount = db.Column(db.Numeric(10, 0))
    dtrgetamn_before = db.Column(db.Numeric(10, 0))
    create_date = db.Column(db.DateTime, nullable=False)
    renew_date = db.Column(db.DateTime, nullable=False)
    operate_cd = db.Column(db.String(128), nullable=False)


class SalesTotalDfNgWk(db.Model):
    __tablename__ = 'sales_total_df_ng_wk'

    dmd_no = db.Column(db.String(13), primary_key=True)
    dmd_month = db.Column(db.String(6))
    dmdto_id = db.Column(db.String(12))
    cst_no = db.Column(db.String(20))
    all_total = db.Column(db.Numeric(10, 0))
    dmd_status = db.Column(db.String(2))
    send_kbn = db.Column(db.String(2))
    result_cd = db.Column(db.String(2))
    payment_date = db.Column(db.DateTime)
    cust_user_type = db.Column(db.String(1), nullable=False)
    cardno = db.Column(db.String(16))
    trans_bankcd = db.Column(db.String(4))
    trans_branchcd = db.Column(db.String(3))
    trans_linecd = db.Column(db.String(1))
    trans_acckind = db.Column(db.String(1))
    trans_accno = db.Column(db.String(7))
    trans_accname = db.Column(db.String(60))
    new_cd = db.Column(db.String(1))
    statuscd = db.Column(db.String(1))
    description = db.Column(db.String(100))
    dtrgetamn_before = db.Column(db.Numeric(10, 0))
    create_date = db.Column(db.DateTime, nullable=False)
    renew_date = db.Column(db.DateTime, nullable=False)
    operate_cd = db.Column(db.String(128), nullable=False)


t_sales_total_df_wk = db.Table(
    'sales_total_df_wk',
    db.Column('dmd_no', db.String(13), nullable=False),
    db.Column('dmd_month', db.String(6)),
    db.Column('dmdto_id', db.String(12)),
    db.Column('cst_no', db.String(20)),
    db.Column('all_total', db.Numeric(10, 0)),
    db.Column('dmd_status', db.String(2)),
    db.Column('send_kbn', db.String(2)),
    db.Column('result_cd', db.String(2)),
    db.Column('payment_date', db.DateTime),
    db.Column('cust_user_type', db.String(1), nullable=False),
    db.Column('cardno', db.String(16)),
    db.Column('trans_bankcd', db.String(4)),
    db.Column('trans_branchcd', db.String(3)),
    db.Column('trans_linecd', db.String(1)),
    db.Column('trans_acckind', db.String(1)),
    db.Column('trans_accno', db.String(7)),
    db.Column('trans_accname', db.String(60)),
    db.Column('new_cd', db.String(1)),
    db.Column('statuscd', db.String(1)),
    db.Column('description', db.String(100)),
    db.Column('dtrgetamn_before', db.Numeric(10, 0)),
    db.Column('create_date', db.DateTime, nullable=False),
    db.Column('renew_date', db.DateTime, nullable=False),
    db.Column('operate_cd', db.String(128), nullable=False)
)


class Service(db.Model):
    __tablename__ = 'service'

    contbase_no = db.Column(db.String(10), primary_key=True, nullable=False)
    idkind_no = db.Column(db.String(1), primary_key=True, nullable=False)
    account_id = db.Column(db.String(64), nullable=False)
    initial_pass = db.Column(db.String(16))
    create_date = db.Column(db.DateTime, nullable=False)
    renew_date = db.Column(db.DateTime, nullable=False)
    operate_cd = db.Column(db.String(128), nullable=False)
    c_flag = db.Column(db.String(1))
    telno = db.Column(db.String(11), index=True)


class SimDat(db.Model):
    __tablename__ = 'sim_dat'

    ws_common_id = db.Column(db.String(20), primary_key=True)
    ws_common_renbn = db.Column(db.String(2), nullable=False)
    contract_no = db.Column(db.String(12), nullable=False, index=True)
    opt_contract_no = db.Column(db.Numeric(10, 0))
    isp_order_no = db.Column(db.String(20), nullable=False, index=True)
    renew_date = db.Column(db.DateTime, nullable=False)
    create_date = db.Column(db.DateTime, nullable=False)
    operate_cd = db.Column(db.String(128), nullable=False)
    c_flag = db.Column(db.String(1))
    remark = db.Column(db.String(80))
    apply_date = db.Column(db.DateTime)
    apply_kind = db.Column(db.String(4), nullable=False)
    prog_status = db.Column(db.String(2), nullable=False)
    send_plan_date = db.Column(db.DateTime)
    send_date = db.Column(db.DateTime)
    sim_status = db.Column(db.String(1))
    imei = db.Column(db.String(15))
    iccid = db.Column(db.String(19))
    msisdn = db.Column(db.String(11), index=True)
    send_name = db.Column(db.String(120))
    send_name_k = db.Column(db.String(240))
    send_zip = db.Column(db.String(7), nullable=False)
    send_todohuken = db.Column(db.String(8), nullable=False)
    send_addr1 = db.Column(db.String(100), nullable=False)
    send_addr2 = db.Column(db.String(100))
    send_build_name = db.Column(db.String(80))
    send_telno = db.Column(db.String(11))
    arrival_plan_date = db.Column(db.DateTime)
    arrival_plan_time = db.Column(db.String(1))
    ship_no = db.Column(db.String(20))
    direct_date = db.Column(db.DateTime)
    ship_decision_date = db.Column(db.DateTime)
    ship_comp_date = db.Column(db.DateTime)
    send_status = db.Column(db.String(2))
    item_cd = db.Column(db.String(10))
    return_limit_date = db.Column(db.DateTime)
    return_flg = db.Column(db.String(1))
    return_date = db.Column(db.DateTime)
    return_kit_reg_date = db.Column(db.DateTime)
    return_send_date = db.Column(db.DateTime)
    org_ws_common_id = db.Column(db.String(20))
    sim_acct_stop_date = db.Column(db.DateTime)
    lost_opt_contract_no = db.Column(db.Numeric(10, 0))
    cont_sex = db.Column(db.String(1))
    cont_birth = db.Column(db.DateTime)
    mnp_number = db.Column(db.String(10))
    mnp_telno = db.Column(db.String(11))
    mnp_reserve_date = db.Column(db.DateTime)
    mnp_line_lastname_k = db.Column(db.String(80))
    mnp_line_firstname_k = db.Column(db.String(40))
    mnp_line_lastname = db.Column(db.String(40))
    mnp_line_firstname = db.Column(db.String(20))
    mnp_line_birth = db.Column(db.DateTime)
    portable_tel_flg = db.Column(db.String(1))
    send_name_lastname = db.Column(db.String(60))
    send_name_firstname = db.Column(db.String(60))
    send_name_lastname_k = db.Column(db.String(120))
    send_name_firstname_k = db.Column(db.String(120))
    mnp_out_number = db.Column(db.String(10))
    mnp_out_status = db.Column(db.String(1))
    mnp_out_apply_date = db.Column(db.DateTime)
    mnp_out_order_date = db.Column(db.DateTime)
    mnp_out_order_comp_date = db.Column(db.DateTime)
    mnp_out_expire_date = db.Column(db.DateTime)
    mnp_out_end_date = db.Column(db.DateTime)
    mnp_out_line_lastname_k = db.Column(db.String(80))
    mnp_out_line_firstname_k = db.Column(db.String(40))
    mnp_out_line_lastname = db.Column(db.String(40))
    mnp_out_line_firstname = db.Column(db.String(20))
    mnp_out_line_birth = db.Column(db.DateTime)
    charge_count = db.Column(db.Numeric(10, 0))
    charge_mb = db.Column(db.Numeric(10, 0))
    charge_date = db.Column(db.DateTime)
    quota_code = db.Column(db.String(128))
    semiblack_add_status = db.Column(db.String(1))
    semiblack_add_reserve_date = db.Column(db.DateTime)
    semiblack_add_apply_date = db.Column(db.DateTime)
    semiblack_add_comp_date = db.Column(db.DateTime)
    semiblack_add_error_msg = db.Column(db.String(100))
    quota_carryover_mb = db.Column(db.Numeric(10, 0))
    quota_carryover_date = db.Column(db.DateTime)
    rent_device_cd = db.Column(db.String(20))
    rent_lost_opt_contract_no = db.Column(db.Numeric(10, 0))
    rent_return_limit_date = db.Column(db.DateTime)
    rent_return_flg = db.Column(db.String(1))
    rent_return_date = db.Column(db.DateTime)


class SpCallLog(db.Model):
    __tablename__ = 'sp_call_log'
    __table_args__ = (
        db.Index('idx_sp_call_log_01', 'contbase_no', 'call_start_time'),
    )

    log_date = db.Column(db.String(8), primary_key=True, nullable=False)
    line_no = db.Column(db.Numeric(7, 0), primary_key=True, nullable=False)
    cc_account_id = db.Column(db.Numeric(19, 0), nullable=False)
    contbase_no = db.Column(db.String(10))
    call_start_time = db.Column(db.DateTime)
    call_second = db.Column(db.Numeric(19, 0))
    telno = db.Column(db.String(16))
    partner_telno = db.Column(db.String(16))
    call_type = db.Column(db.String(16))
    oem_charge = db.Column(db.Numeric(6, 0))
    user_charge = db.Column(db.Numeric(6, 0))
    tarrif_code = db.Column(db.String(128))
    tarrif_type = db.Column(db.String(2))
    create_date = db.Column(db.DateTime, nullable=False)
    renew_date = db.Column(db.DateTime, nullable=False)
    operate_cd = db.Column(db.String(128), nullable=False)
    discount_charge = db.Column(db.Numeric(6, 0))
    org_call_second = db.Column(db.Numeric(19, 0))
    org_user_charge = db.Column(db.Numeric(6, 0))


class SpCallLogMng(db.Model):
    __tablename__ = 'sp_call_log_mng'

    error_log_date = db.Column(db.String(8), primary_key=True)
    create_date = db.Column(db.DateTime, nullable=False)
    renew_date = db.Column(db.DateTime, nullable=False)
    operate_cd = db.Column(db.String(128), nullable=False)


class StockholderCdMst(db.Model):
    __tablename__ = 'stockholder_cd_mst'

    stockholder_cd = db.Column(db.String(10), primary_key=True)
    start_date = db.Column(db.DateTime, nullable=False)
    end_date = db.Column(db.DateTime, nullable=False)


t_tap_funky = db.Table(
    'tap_funky',
    db.Column('oid', db.OID),
    db.Column('schema', db.String),
    db.Column('name', db.String),
    db.Column('owner', db.String),
    db.Column('args', db.Text),
    db.Column('returns', db.Text),
    db.Column('langoid', db.OID),
    db.Column('is_strict', db.Boolean),
    db.Column('is_agg', db.Boolean),
    db.Column('is_definer', db.Boolean),
    db.Column('returns_set', db.Boolean),
    db.Column('volatility', db.String(1)),
    db.Column('is_visible', db.Boolean)
)


class TepcoDat(db.Model):
    __tablename__ = 'tepco_dat'

    ws_common_id = db.Column(db.String(20), primary_key=True)
    ws_common_renbn = db.Column(db.String(2))
    contract_no = db.Column(db.String(12), index=True)
    isp_order_no = db.Column(db.String(20), nullable=False, index=True)
    apply_date = db.Column(db.DateTime, nullable=False)
    send_plan_date = db.Column(db.DateTime)
    send_date = db.Column(db.DateTime)
    apply_kind = db.Column(db.String(4))
    prog_status = db.Column(db.String(2))
    syori_kind = db.Column(db.String(2))
    syori_status = db.Column(db.String(1))
    username = db.Column(db.String(32))
    domainname = db.Column(db.String(32))
    tpc_no = db.Column(db.String(14))
    user_cd = db.Column(db.String(1))
    zip = db.Column(db.String(8), nullable=False)
    todohuken = db.Column(db.String(8))
    gun = db.Column(db.String(20))
    ku = db.Column(db.String(20))
    area = db.Column(db.String(40))
    chome = db.Column(db.String(10))
    banchi = db.Column(db.String(20))
    build_name = db.Column(db.String(80))
    telno = db.Column(db.String(13))
    toi_telno = db.Column(db.String(13))
    email = db.Column(db.String(80))
    house_cd1 = db.Column(db.String(1))
    house_cd2 = db.Column(db.String(1))
    house_cd22 = db.Column(db.String(1))
    lead_in = db.Column(db.String(1))
    ftth_cd = db.Column(db.String(1))
    house_floor = db.Column(db.String(1))
    tpc_user_cd = db.Column(db.String(1))
    line_cd = db.Column(db.String(1))
    work_flag = db.Column(db.String(2))
    tpc_service_cd = db.Column(db.String(1))
    tpc_kari_date = db.Column(db.DateTime)
    tpc_date = db.Column(db.DateTime)
    start_date = db.Column(db.DateTime)
    closed_date = db.Column(db.DateTime)
    check_date = db.Column(db.DateTime)
    check_time = db.Column(db.String(1))
    work_date = db.Column(db.DateTime)
    work_time = db.Column(db.String(1))
    work_end_date = db.Column(db.DateTime)
    cash_cd = db.Column(db.String(1))
    lump_sum = db.Column(db.String(30))
    apart_cd = db.Column(db.String(13))
    opt_flag = db.Column(db.String(30))
    vdsl_model = db.Column(db.String(8))
    voip_model = db.Column(db.String(8))
    musen_model = db.Column(db.String(8))
    tpc_result = db.Column(db.String(3))
    tpc_details = db.Column(db.String(160))
    isp_notes = db.Column(db.String(160))
    tpc_notes = db.Column(db.String(160))
    campaign_cd = db.Column(db.String(15))
    agency_cd = db.Column(db.String(12))
    create_date = db.Column(db.DateTime, nullable=False)
    renew_date = db.Column(db.DateTime, nullable=False)
    operate_cd = db.Column(db.String(128), nullable=False)
    c_flag = db.Column(db.String(1))
    remark = db.Column(db.String(80))


class TepcoOprMst(db.Model):
    __tablename__ = 'tepco_opr_mst'

    apply_kind_cd = db.Column(db.String(4), primary_key=True)
    apply_kind_name = db.Column(db.String(80))
    opr_apply_kind_cd = db.Column(db.String(3), nullable=False)
    opr_apply_kind_name = db.Column(db.String(60))
    data_cd = db.Column(db.String(2))
    create_date = db.Column(db.DateTime, nullable=False)
    renew_date = db.Column(db.DateTime, nullable=False)
    operate_cd = db.Column(db.String(128), nullable=False)
    c_flag = db.Column(db.String(1))


class TgSetInfo(db.Model):
    __tablename__ = 'tg_set_info'

    contract_no = db.Column(db.String(12), primary_key=True)
    isp_order_no = db.Column(db.String(20), nullable=False)
    renew_date = db.Column(db.DateTime, nullable=False)
    create_date = db.Column(db.DateTime, nullable=False)
    operate_cd = db.Column(db.String(128), nullable=False)
    c_flag = db.Column(db.String(1))
    apply_date = db.Column(db.DateTime, nullable=False)
    tg_set_camp_status = db.Column(db.String(2), nullable=False)
    tg_set_appy_available = db.Column(db.String(1))
    tg_set_appy_ng_reason = db.Column(db.String(1))
    tg_set_appy_result_date = db.Column(db.DateTime)
    tg_cont_no = db.Column(db.String(13))
    tg_set_cont_no = db.Column(db.String(13))
    tg_toss_cont_no = db.Column(db.Numeric(8, 0))
    tg_customer_name = db.Column(db.String(142))
    tg_customer_kname = db.Column(db.String(142))
    tg_cont_status_gas = db.Column(db.String(40))
    tg_start_date_gas = db.Column(db.DateTime)
    tg_cont_status_electric = db.Column(db.String(40))
    tg_start_date_electric = db.Column(db.DateTime)
    tg_set_camp_available = db.Column(db.String(1))
    tg_set_camp_ng_reason = db.Column(db.String(1))
    removal_flag = db.Column(db.String(1))
    yobi01 = db.Column(db.String(100))


class TonePrefixDat(db.Model):
    __tablename__ = 'tone_prefix_dat'

    ws_common_id = db.Column(db.String(20), primary_key=True)
    ws_common_renbn = db.Column(db.String(2), nullable=False)
    opt_contract_no = db.Column(db.Numeric(10, 0), nullable=False, index=True)
    process_kbn = db.Column(db.String(6), nullable=False)
    msisdn = db.Column(db.String(11))
    contbase_no = db.Column(db.String(10), nullable=False)
    exec_plan = db.Column(db.String(1), nullable=False)
    prefix_cd = db.Column(db.String(20))
    apply_kind = db.Column(db.String(4), nullable=False)
    prog_status = db.Column(db.String(2), nullable=False)
    send_plan_date = db.Column(db.DateTime)
    send_date = db.Column(db.DateTime)
    result_receive_date = db.Column(db.DateTime)
    result_cd = db.Column(db.String(2))
    result_status = db.Column(db.String(2))
    create_date = db.Column(db.DateTime, nullable=False)
    renew_date = db.Column(db.DateTime, nullable=False)
    operate_cd = db.Column(db.String(128), nullable=False)
    c_flag = db.Column(db.String(1))


class ToneSession(db.Model):
    __tablename__ = 'tone_session'

    sid = db.Column(db.String(40), primary_key=True)
    data = db.Column(db.Text)
    expires = db.Column(db.Numeric(10, 0), nullable=False)


class TransMst(db.Model):
    __tablename__ = 'trans_mst'

    type = db.Column(db.String(3), primary_key=True, nullable=False)
    code1 = db.Column(db.String(100), primary_key=True, nullable=False)
    code2 = db.Column(db.String(500), nullable=False)


t_trans_result_error_tmp = db.Table(
    'trans_result_error_tmp',
    db.Column('dmdto_id', db.String(12), nullable=False),
    db.Column('dmd_no', db.String(13), nullable=False, index=True),
    db.Column('result_cd', db.String(2)),
    db.Column('dmd_month', db.String(6), nullable=False),
    db.Column('all_total', db.Numeric(10, 0), nullable=False),
    db.Column('demand_kbn', db.String(2), nullable=False),
    db.Column('valid_date', db.DateTime, nullable=False),
    db.Column('customer_id', db.String(8), nullable=False),
    db.Column('cust_email', db.String(128), nullable=False),
    db.Column('lastname', db.String(50), nullable=False),
    db.Column('firstname', db.String(20)),
    db.Column('trans_result', db.String(2), nullable=False),
    db.Column('year_month', db.String(6), nullable=False),
    db.Column('disp_mmdd', db.String(4), nullable=False),
    db.Column('trans_kind', db.String(1), nullable=False),
    db.Column('create_date', db.DateTime, nullable=False),
    db.Column('current_demand_kbn', db.String(2), nullable=False),
    db.Column('current_valid_date', db.DateTime, nullable=False),
    db.Index('idx_trans_result_error_tmp_02', 'dmdto_id', 'dmd_month')
)


class TransResultTmp(db.Model):
    __tablename__ = 'trans_result_tmp'

    data_cd = db.Column(db.String(1), nullable=False)
    trans_bankcd = db.Column(db.String(4), nullable=False)
    trans_bankkana = db.Column(db.String(30), nullable=False)
    trans_branchcd = db.Column(db.String(3), nullable=False)
    trans_branchkana = db.Column(db.String(30))
    blank = db.Column(db.String(4), nullable=False)
    trans_acckind = db.Column(db.String(1), nullable=False)
    trans_accno = db.Column(db.String(7), nullable=False)
    trans_accname = db.Column(db.String(60), nullable=False)
    trans_money = db.Column(db.String(10), nullable=False)
    new_cd = db.Column(db.String(1), nullable=False)
    fixed_item = db.Column(db.String(6), nullable=False)
    zengin_cst_no = db.Column(db.String(14), primary_key=True)
    trans_result_cd = db.Column(db.String(1), nullable=False)
    trans_kind = db.Column(db.String(1), nullable=False)
    create_date = db.Column(db.DateTime, nullable=False)
    dmdto_id = db.Column(db.String(12))
    dmd_no = db.Column(db.String(13))


t_transfer_serversman_sim = db.Table(
    'transfer_serversman_sim',
    db.Column('dti_customer_id', db.String(8)),
    db.Column('tone_customer_id', db.String(8))
)


class UnameDat(db.Model):
    __tablename__ = 'uname_dat'
    __table_args__ = (
        db.Index('idx_uname_dat_02', 'second_lv_domain', 'top_lv_domain'),
    )

    ws_common_id = db.Column(db.String(20), primary_key=True)
    ws_common_renbn = db.Column(db.Numeric(2, 0), nullable=False)
    contract_no = db.Column(db.String(12), nullable=False, index=True)
    create_date = db.Column(db.DateTime, nullable=False)
    renew_date = db.Column(db.DateTime, nullable=False)
    operate_cd = db.Column(db.String(128), nullable=False)
    c_flag = db.Column(db.String(1))
    remark = db.Column(db.String(80))
    second_lv_domain = db.Column(db.String(64), nullable=False)
    top_lv_domain = db.Column(db.String(3), nullable=False)
    domain_status = db.Column(db.Numeric(2, 0), nullable=False)
    domain_start_date = db.Column(db.DateTime, nullable=False)
    domain_end_date = db.Column(db.DateTime)
    domain_exp_date = db.Column(db.DateTime, nullable=False, index=True)
    owner_j_last_name = db.Column(db.String(50))
    owner_e_last_name = db.Column(db.String(50))
    owner_j_first_name = db.Column(db.String(50))
    owner_e_first_name = db.Column(db.String(50))
    owner_user_type = db.Column(db.String(1))
    owner_j_org_name = db.Column(db.String(100))
    owner_e_org_name = db.Column(db.String(100))
    owner_zip = db.Column(db.String(16))
    owner_j_addr1 = db.Column(db.Numeric(2, 0))
    owner_e_addr1 = db.Column(db.String(20))
    owner_j_addr2 = db.Column(db.String(50))
    owner_e_addr2 = db.Column(db.String(50))
    owner_j_addr3 = db.Column(db.String(50))
    owner_e_addr3 = db.Column(db.String(50))
    owner_j_addr4 = db.Column(db.String(50))
    owner_e_addr4 = db.Column(db.String(50))
    owner_telno = db.Column(db.String(20))
    owner_faxno = db.Column(db.String(20))
    owner_email = db.Column(db.String(100))
    admin_j_last_name = db.Column(db.String(50))
    admin_e_last_name = db.Column(db.String(50))
    admin_j_first_name = db.Column(db.String(50))
    admin_e_first_name = db.Column(db.String(50))
    admin_user_type = db.Column(db.String(1))
    admin_j_org_name = db.Column(db.String(100))
    admin_e_org_name = db.Column(db.String(100))
    admin_zip = db.Column(db.String(16))
    admin_j_addr1 = db.Column(db.Numeric(2, 0))
    admin_e_addr1 = db.Column(db.String(20))
    admin_j_addr2 = db.Column(db.String(50))
    admin_e_addr2 = db.Column(db.String(50))
    admin_j_addr3 = db.Column(db.String(50))
    admin_e_addr3 = db.Column(db.String(50))
    admin_j_addr4 = db.Column(db.String(50))
    admin_e_addr4 = db.Column(db.String(50))
    admin_telno = db.Column(db.String(20))
    admin_faxno = db.Column(db.String(20))
    admin_email = db.Column(db.String(100))
    tech_j_last_name = db.Column(db.String(50))
    tech_e_last_name = db.Column(db.String(50))
    tech_j_first_name = db.Column(db.String(50))
    tech_e_first_name = db.Column(db.String(50))
    tech_user_type = db.Column(db.String(1))
    tech_j_org_name = db.Column(db.String(100))
    tech_e_org_name = db.Column(db.String(100))
    tech_zip = db.Column(db.String(16))
    tech_j_addr1 = db.Column(db.Numeric(2, 0))
    tech_e_addr1 = db.Column(db.String(20))
    tech_j_addr2 = db.Column(db.String(50))
    tech_e_addr2 = db.Column(db.String(50))
    tech_j_addr3 = db.Column(db.String(50))
    tech_e_addr3 = db.Column(db.String(50))
    tech_j_addr4 = db.Column(db.String(50))
    tech_e_addr4 = db.Column(db.String(50))
    tech_telno = db.Column(db.String(20))
    tech_faxno = db.Column(db.String(20))
    tech_email = db.Column(db.String(100))
    acc_j_last_name = db.Column(db.String(50))
    acc_e_last_name = db.Column(db.String(50))
    acc_j_first_name = db.Column(db.String(50))
    acc_e_first_name = db.Column(db.String(50))
    acc_user_type = db.Column(db.String(1))
    acc_j_org_name = db.Column(db.String(100))
    acc_e_org_name = db.Column(db.String(100))
    acc_zip = db.Column(db.String(16))
    acc_j_addr1 = db.Column(db.Numeric(2, 0))
    acc_e_addr1 = db.Column(db.String(20))
    acc_j_addr2 = db.Column(db.String(50))
    acc_e_addr2 = db.Column(db.String(50))
    acc_j_addr3 = db.Column(db.String(50))
    acc_e_addr3 = db.Column(db.String(50))
    acc_j_addr4 = db.Column(db.String(50))
    acc_e_addr4 = db.Column(db.String(50))
    acc_telno = db.Column(db.String(20))
    acc_faxno = db.Column(db.String(20))
    acc_email = db.Column(db.String(100))
    gmo_id = db.Column(db.String(18))
    gmo_pass = db.Column(db.String(18))
    release_apply_date = db.Column(db.DateTime)
    domain_pending_id = db.Column(db.String(18))


class UniversalServiceMst(db.Model):
    __tablename__ = 'universal_service_mst'

    valid_date = db.Column(db.DateTime, primary_key=True)
    cost = db.Column(db.Numeric(2, 0), nullable=False)
    taxfree_kbn = db.Column(db.String(1), nullable=False)
    create_date = db.Column(db.DateTime, nullable=False)
    renew_date = db.Column(db.DateTime, nullable=False)
    operate_cd = db.Column(db.String(128), nullable=False)


class UnlimitedChargeLog(db.Model):
    __tablename__ = 'unlimited_charge_log'

    used_month = db.Column(db.Date, primary_key=True, nullable=False)
    line_no = db.Column(db.Numeric(7, 0), primary_key=True, nullable=False)
    msisdn = db.Column(db.String(16), nullable=False)
    charge_kb = db.Column(db.Numeric(7, 0), nullable=False)
    charge_date = db.Column(db.DateTime, nullable=False)
    quota_code = db.Column(db.String(128))
    bill_month = db.Column(db.Date, nullable=False)
    contract_no = db.Column(db.String(12))
    free_flag = db.Column(db.String(3))
    create_date = db.Column(db.DateTime, nullable=False)
    renew_date = db.Column(db.DateTime, nullable=False)
    operate_cd = db.Column(db.String(128), nullable=False)


t_upd_customer_id_mng_tmp = db.Table(
    'upd_customer_id_mng_tmp',
    db.Column('customer_id', db.String(8), nullable=False),
    db.Column('pay_status', db.String(1)),
    db.Column('create_date', db.DateTime),
    db.Column('renew_date', db.DateTime),
    db.Column('operate_cd', db.String(128))
)


t_used_3g_unlimited = db.Table(
    'used_3g_unlimited',
    db.Column('dmdto_id', db.String(12), nullable=False),
    db.Column('contract_no', db.String(12), nullable=False),
    db.Column('msisdn', db.String(11), nullable=False),
    db.Column('used_kb', db.Numeric(10, 0), nullable=False),
    db.Column('remain_kb', db.Numeric(10, 0), nullable=False),
    db.Column('used', db.Numeric(10, 0), nullable=False),
    db.Column('remain', db.Numeric(10, 0), nullable=False),
    db.Column('used_tax', db.Numeric(10, 0), nullable=False),
    db.Column('remain_tax', db.Numeric(10, 0), nullable=False),
    db.Column('tax_late', db.String(5), nullable=False),
    db.Column('charged', db.Numeric(10, 0), nullable=False),
    db.Column('used_date', db.DateTime, nullable=False),
    db.Column('expire_date', db.DateTime, nullable=False),
    db.Column('plan_cd', db.String(8), nullable=False),
    db.Column('dmd_date', db.DateTime, nullable=False),
    db.Column('create_date', db.DateTime, nullable=False),
    db.Column('free_flag', db.String(1))
)


t_v_acc_trans_err_cvs = db.Table(
    'v_acc_trans_err_cvs',
    db.Column('dmd_month', db.String(6)),
    db.Column('dmdto_id', db.String(12)),
    db.Column('create_date', db.DateTime),
    db.Column('renew_date', db.DateTime),
    db.Column('operate_cd', db.String(128)),
    db.Column('trans_kind', db.String(1)),
    db.Column('result_cd', db.String(1)),
    db.Column('dmd_no', db.String(13)),
    db.Column('demand_kbn', db.String(2)),
    db.Column('dmd_valid_date', db.DateTime),
    db.Column('cvs_next_month_flag', db.String(1)),
    db.Column('dmd_no_next_month', db.String(13)),
    db.Column('chg_dmd_kbn_flag', db.String(1)),
    db.Column('reserved_dmd_kbn_flag', db.String(1))
)


t_v_acca_dat = db.Table(
    'v_acca_dat',
    db.Column('ws_common_id', db.String(20)),
    db.Column('ws_common_renbn', db.String(2)),
    db.Column('contract_no', db.String(12)),
    db.Column('isp_order_no', db.String(20)),
    db.Column('apply_date', db.DateTime),
    db.Column('send_plan_date', db.DateTime),
    db.Column('send_date', db.DateTime),
    db.Column('apply_kind', db.String(4)),
    db.Column('prog_status', db.String(2)),
    db.Column('apply_brand', db.String(2)),
    db.Column('order_cd', db.String(3)),
    db.Column('order_no', db.String(10)),
    db.Column('acca_no', db.String(60)),
    db.Column('service_id', db.String(10)),
    db.Column('gc_name', db.String(200)),
    db.Column('line_name', db.String(60)),
    db.Column('install_cd', db.String(1)),
    db.Column('zip', db.String(8)),
    db.Column('todohuken', db.String(8)),
    db.Column('gun', db.String(30)),
    db.Column('ku', db.String(30)),
    db.Column('area', db.String(30)),
    db.Column('banchi', db.String(50)),
    db.Column('build_name', db.String(120)),
    db.Column('telno', db.String(13)),
    db.Column('toi_telno', db.String(13)),
    db.Column('email', db.String(90)),
    db.Column('service_kind', db.String(1)),
    db.Column('isdn_type', db.String(1)),
    db.Column('user_cd', db.String(1)),
    db.Column('isdn_change', db.String(1)),
    db.Column('cpe_provider', db.String(1)),
    db.Column('cpe_installer', db.String(1)),
    db.Column('cpe_kind', db.String(3)),
    db.Column('nw_kind', db.String(1)),
    db.Column('ntt_result', db.String(1)),
    db.Column('ntt_ng1', db.String(2)),
    db.Column('ntt_ng2', db.String(2)),
    db.Column('ntt_notes', db.String(1800)),
    db.Column('reason_cd', db.String(2)),
    db.Column('result_date', db.DateTime),
    db.Column('change_date', db.DateTime),
    db.Column('ntt_work_date', db.DateTime),
    db.Column('complete_date', db.DateTime),
    db.Column('notes', db.String(600)),
    db.Column('entry_cd', db.String(10)),
    db.Column('campaign_cd', db.String(15)),
    db.Column('agency_cd', db.String(12)),
    db.Column('create_date', db.DateTime),
    db.Column('renew_date', db.DateTime),
    db.Column('operate_cd', db.String(128)),
    db.Column('c_flag', db.String(1)),
    db.Column('remark', db.String(80)),
    db.Column('owner_zip', db.String(8)),
    db.Column('owner_todohuken', db.String(8)),
    db.Column('owner_gun', db.String(30)),
    db.Column('owner_ku', db.String(30)),
    db.Column('owner_area', db.String(30)),
    db.Column('owner_banchi', db.String(50)),
    db.Column('owner_build_name', db.String(120)),
    db.Column('cert_telno', db.String(13))
)


t_v_adjust = db.Table(
    'v_adjust',
    db.Column('bill_month', db.Date),
    db.Column('adjust_renban', db.Numeric(9, 0)),
    db.Column('dmdto_id', db.String(12)),
    db.Column('contbase_no', db.String(10)),
    db.Column('contract_no', db.String(12)),
    db.Column('opt_contract_no', db.Numeric(10, 0)),
    db.Column('customer_id', db.String(8)),
    db.Column('reason', db.String(64)),
    db.Column('cost', db.Numeric(6, 0)),
    db.Column('taxfree_kbn', db.String(1)),
    db.Column('adjust_kind', db.String(1)),
    db.Column('adjust_cd', db.String(9)),
    db.Column('create_date', db.DateTime),
    db.Column('renew_date', db.DateTime),
    db.Column('operate_cd', db.String(128)),
    db.Column('c_flag', db.String(1)),
    db.Column('creditor_cd', db.String(1)),
    db.Column('creditor_subcd', db.String(3)),
    db.Column('sales_dmd_kbn', db.String(1)),
    db.Column('stat_kbn', db.Numeric(1, 0)),
    db.Column('tax_percent', db.Numeric(4, 1))
)


t_v_alipay_dat = db.Table(
    'v_alipay_dat',
    db.Column('contract_no', db.String(12)),
    db.Column('opt_contract_no', db.Numeric(10, 0)),
    db.Column('jpayment_trade_no', db.String(64))
)


t_v_all_telno = db.Table(
    'v_all_telno',
    db.Column('customer_id', db.String(8)),
    db.Column('telno', db.String),
    db.Index('idx_v_all_telno_01', 'telno', 'customer_id')
)


t_v_announce = db.Table(
    'v_announce',
    db.Column('customer_id', db.String(8)),
    db.Column('type', db.String(1)),
    db.Column('create_date', db.DateTime),
    db.Column('renew_date', db.DateTime),
    db.Column('c_flag', db.String(1)),
    db.Column('operate_cd', db.String(128))
)


t_v_appli_res_mst = db.Table(
    'v_appli_res_mst',
    db.Column('res_cd', db.String(4)),
    db.Column('address_kind', db.String(16)),
    db.Column('res_kind', db.String(128)),
    db.Column('append_res1', db.String(4)),
    db.Column('append_res2', db.String(4)),
    db.Column('enc_num', db.Numeric(2, 0))
)


t_v_appli_send_dat = db.Table(
    'v_appli_send_dat',
    db.Column('send_no', db.String(20)),
    db.Column('renew_date', db.DateTime),
    db.Column('create_date', db.DateTime),
    db.Column('operate_cd', db.String(128)),
    db.Column('c_flag', db.String(1)),
    db.Column('remark', db.String(80)),
    db.Column('apply_date', db.DateTime),
    db.Column('customer_id', db.String(8)),
    db.Column('prog_status', db.String(2)),
    db.Column('direct_operate_cd', db.String(128)),
    db.Column('direct_date', db.DateTime),
    db.Column('ship_decision_date', db.DateTime),
    db.Column('slip_number', db.String(20)),
    db.Column('ship_result', db.String(16)),
    db.Column('send_name', db.String(72)),
    db.Column('send_chgdept', db.String(100)),
    db.Column('send_chgpost', db.String(40)),
    db.Column('send_chgname', db.String(40)),
    db.Column('send_zip', db.String(7)),
    db.Column('send_addr1', db.String(8)),
    db.Column('send_addr2', db.String(100)),
    db.Column('send_addr3', db.String(100)),
    db.Column('send_telno', db.String(11)),
    db.Column('memo', db.String(512)),
    db.Column('express_flg', db.String(1)),
    db.Column('sign_kind', db.String(1)),
    db.Column('res_base', db.String(4)),
    db.Column('res_base_num', db.Numeric(2, 0)),
    db.Column('res_add1', db.String(4)),
    db.Column('res_add1_num', db.Numeric(2, 0)),
    db.Column('res_add2', db.String(4)),
    db.Column('res_add2_num', db.Numeric(2, 0)),
    db.Column('res_add3', db.String(4)),
    db.Column('res_add3_num', db.Numeric(2, 0)),
    db.Column('res_add4', db.String(4)),
    db.Column('res_add4_num', db.Numeric(2, 0))
)


t_v_au_set_info = db.Table(
    'v_au_set_info',
    db.Column('contract_no', db.String(12)),
    db.Column('isp_order_no', db.String(20)),
    db.Column('renew_date', db.DateTime),
    db.Column('create_date', db.DateTime),
    db.Column('operate_cd', db.String(128)),
    db.Column('c_flag', db.String(1)),
    db.Column('apply_date', db.DateTime),
    db.Column('auset_camp_status', db.String(2)),
    db.Column('auset_camp_available', db.String(1)),
    db.Column('auset_camp_ng_reason', db.String(1)),
    db.Column('auset_camp_disc', db.String(1)),
    db.Column('au_cont_telno', db.String(11)),
    db.Column('au_firstname_k', db.String(20)),
    db.Column('au_lastname_k', db.String(100)),
    db.Column('au_cont_zip', db.String(7)),
    db.Column('au_cont_todohuken', db.String(8)),
    db.Column('au_cont_shiku', db.String(60)),
    db.Column('au_cont_area_chome_banchi', db.String(60)),
    db.Column('au_cont_build_name', db.String(100)),
    db.Column('auset_appy_available', db.String(1)),
    db.Column('auset_appy_ng_reason', db.String(1)),
    db.Column('auset_appy_disc', db.String(1))
)


t_v_bank_calender_mst = db.Table(
    'v_bank_calender_mst',
    db.Column('year_month', db.String(6)),
    db.Column('disp_mmdd', db.String(4))
)


t_v_bank_mst = db.Table(
    'v_bank_mst',
    db.Column('bnkcd', db.String(4)),
    db.Column('bnkkana', db.String(60)),
    db.Column('bnkname', db.String(46)),
    db.Column('pwd_valid_flag', db.String(1)),
    db.Column('pwd_stro_kbn', db.String(1)),
    db.Column('abolish_flag', db.String(1))
)


t_v_bill_customer = db.Table(
    'v_bill_customer',
    db.Column('customer_id', db.String(8)),
    db.Column('creditor_cd', db.String(1)),
    db.Column('creditor_subcd', db.String(3)),
    db.Column('sales_dmd_kbn', db.String(1)),
    db.Column('tax_percent', db.Numeric(4, 1)),
    db.Column('taxable_total', db.Numeric(10, 0)),
    db.Column('taxfree_total', db.Numeric(10, 0)),
    db.Column('tax_total', db.Numeric(10, 0))
)


t_v_bill_detail = db.Table(
    'v_bill_detail',
    db.Column('create_date', db.DateTime),
    db.Column('renew_date', db.DateTime),
    db.Column('operate_cd', db.String(128)),
    db.Column('c_flag', db.String(1)),
    db.Column('dmdto_id', db.String(12)),
    db.Column('customer_id', db.String(8)),
    db.Column('contract_no', db.String(12)),
    db.Column('bill_detailno', db.Numeric(5, 0)),
    db.Column('opt_contract_no', db.Numeric(10, 0)),
    db.Column('plan_cd', db.String(8)),
    db.Column('disc_type', db.String(2)),
    db.Column('disc_cd', db.String(3)),
    db.Column('bill_kbn_cd', db.String(2)),
    db.Column('bill_start', db.DateTime),
    db.Column('bill_end', db.DateTime),
    db.Column('quantity', db.Numeric(19, 0)),
    db.Column('unit', db.String(10)),
    db.Column('unit_cost', db.Numeric(10, 4)),
    db.Column('tax_cost', db.Numeric(9, 0)),
    db.Column('account_id', db.String(64)),
    db.Column('adjust_renban', db.Numeric(9, 0)),
    db.Column('cost', db.Numeric(9, 0)),
    db.Column('taxfree_kbn', db.String(1)),
    db.Column('kihon_tuika_kbn', db.String(1)),
    db.Column('kddi_plan_cd', db.String(10)),
    db.Column('plan_name', db.String(128)),
    db.Column('creditor_cd', db.String(1)),
    db.Column('ntt_plan_cd', db.String(10)),
    db.Column('creditor_subcd', db.String(3)),
    db.Column('sales_dmd_kbn', db.String(1)),
    db.Column('demand_count', db.Numeric(2, 0)),
    db.Column('jpayment_trade_no', db.String(64)),
    db.Column('tax_percent', db.Numeric(4, 1))
)


t_v_bill_dmd = db.Table(
    'v_bill_dmd',
    db.Column('dmdto_id', db.String(12)),
    db.Column('creditor_cd', db.String(1)),
    db.Column('creditor_subcd', db.String(3)),
    db.Column('sales_dmd_kbn', db.String(1)),
    db.Column('use_aim', db.Numeric(1, 0)),
    db.Column('stat_kbn', db.Numeric(1, 0)),
    db.Column('tax_percent', db.Numeric(4, 1)),
    db.Column('taxable_total', db.Numeric(10, 0)),
    db.Column('taxfree_total', db.Numeric(10, 0)),
    db.Column('tax_total', db.Numeric(10, 0))
)


t_v_bill_history = db.Table(
    'v_bill_history',
    db.Column('bill_month', db.Date),
    db.Column('history', db.Numeric(2, 0)),
    db.Column('create_date', db.DateTime),
    db.Column('operate_cd', db.String(128))
)


t_v_bill_shift_contract = db.Table(
    'v_bill_shift_contract',
    db.Column('create_date', db.DateTime),
    db.Column('renew_date', db.DateTime),
    db.Column('operate_cd', db.String(128)),
    db.Column('c_flag', db.String(1)),
    db.Column('contract_no', db.String(12)),
    db.Column('used_month', db.Date),
    db.Column('org_bill_month', db.Date),
    db.Column('plan_bill_month', db.Date),
    db.Column('dmdto_id', db.String(12)),
    db.Column('kddi_taxable_total', db.Numeric(10, 0)),
    db.Column('kddi_taxfree_total', db.Numeric(10, 0)),
    db.Column('kddi_tax', db.Numeric(10, 0)),
    db.Column('collection_taxable_total', db.Numeric(10, 0)),
    db.Column('collection_taxin_total', db.Numeric(10, 0)),
    db.Column('ntt_e_taxable_total', db.Numeric(10, 0)),
    db.Column('ntt_e_taxfree_total', db.Numeric(10, 0)),
    db.Column('ntt_e_tax_total', db.Numeric(10, 0)),
    db.Column('ntt_w_taxable_total', db.Numeric(10, 0)),
    db.Column('ntt_w_taxfree_total', db.Numeric(10, 0)),
    db.Column('ntt_w_tax_total', db.Numeric(10, 0))
)


t_v_bill_shift_detail = db.Table(
    'v_bill_shift_detail',
    db.Column('create_date', db.DateTime),
    db.Column('renew_date', db.DateTime),
    db.Column('operate_cd', db.String(128)),
    db.Column('c_flag', db.String(1)),
    db.Column('org_bill_month', db.Date),
    db.Column('plan_bill_month', db.Date),
    db.Column('dmdto_id', db.String(12)),
    db.Column('customer_id', db.String(8)),
    db.Column('contract_no', db.String(12)),
    db.Column('bill_detailno', db.Numeric(5, 0)),
    db.Column('opt_contract_no', db.Numeric(10, 0)),
    db.Column('plan_cd', db.String(8)),
    db.Column('disc_type', db.String(2)),
    db.Column('disc_cd', db.String(3)),
    db.Column('bill_kbn_cd', db.String(2)),
    db.Column('bill_start', db.DateTime),
    db.Column('bill_end', db.DateTime),
    db.Column('quantity', db.Numeric(19, 0)),
    db.Column('unit', db.String(10)),
    db.Column('unit_cost', db.Numeric(10, 4)),
    db.Column('tax_cost', db.Numeric(9, 0)),
    db.Column('account_id', db.String(64)),
    db.Column('adjust_renban', db.Numeric(9, 0)),
    db.Column('cost', db.Numeric(9, 0)),
    db.Column('taxfree_kbn', db.String(1)),
    db.Column('kihon_tuika_kbn', db.String(1)),
    db.Column('kddi_plan_cd', db.String(10)),
    db.Column('plan_name', db.String(128)),
    db.Column('creditor_cd', db.String(1)),
    db.Column('ntt_plan_cd', db.String(10)),
    db.Column('creditor_subcd', db.String(3)),
    db.Column('tax_percent', db.Numeric(4, 1))
)


t_v_branch_mst = db.Table(
    'v_branch_mst',
    db.Column('bnkcd', db.String(4)),
    db.Column('brncd', db.String(3)),
    db.Column('brnsidecd', db.String(1)),
    db.Column('brnkana', db.String(40)),
    db.Column('brnname', db.String(30)),
    db.Column('brnzip', db.String(10)),
    db.Column('brnaddress', db.String(110)),
    db.Column('brntelno', db.String(20)),
    db.Column('brninvexgno', db.String(4)),
    db.Column('abolish_flag', db.String(1))
)


t_v_branch_wk = db.Table(
    'v_branch_wk',
    db.Column('bnkcd', db.String(4)),
    db.Column('brncd', db.String(3)),
    db.Column('bnkkana', db.String(60)),
    db.Column('bnkname', db.String(46)),
    db.Column('brnkana', db.String(40)),
    db.Column('brnname', db.String(30)),
    db.Column('brnzip', db.String(10)),
    db.Column('brnaddress', db.String(110)),
    db.Column('brntelno', db.String(20)),
    db.Column('brninvexgno', db.String(4)),
    db.Column('brnsidecd', db.String(1))
)


t_v_bulk_adjust = db.Table(
    'v_bulk_adjust',
    db.Column('bill_month', db.Date),
    db.Column('proc_renban', db.Numeric(3, 0)),
    db.Column('file_nm', db.String(256)),
    db.Column('proc_status', db.String(1)),
    db.Column('proc_date', db.DateTime),
    db.Column('create_date', db.DateTime),
    db.Column('renew_date', db.DateTime),
    db.Column('operate_cd', db.String(128)),
    db.Column('c_flag', db.String(1))
)


t_v_bulk_adjust_wk = db.Table(
    'v_bulk_adjust_wk',
    db.Column('bill_month', db.Date),
    db.Column('proc_renban', db.Numeric(3, 0)),
    db.Column('line_no', db.Numeric(6, 0)),
    db.Column('line_text', db.String(1024)),
    db.Column('create_date', db.DateTime),
    db.Column('renew_date', db.DateTime),
    db.Column('operate_cd', db.String(128)),
    db.Column('c_flag', db.String(1))
)


t_v_card_refile_mst = db.Table(
    'v_card_refile_mst',
    db.Column('system_id', db.Numeric(4, 0)),
    db.Column('sales_valid_kbn', db.Numeric(1, 0)),
    db.Column('card_corpname', db.String(10)),
    db.Column('card_cd', db.String(4)),
    db.Column('cd_start', db.Numeric(8, 0)),
    db.Column('cd_end', db.Numeric(8, 0)),
    db.Column('card_figure', db.Numeric(2, 0)),
    db.Column('cardkind', db.String(2)),
    db.Column('note', db.String(512)),
    db.Column('priority_flag', db.String(1)),
    db.Column('amount', db.Numeric(6, 0))
)


t_v_cashback = db.Table(
    'v_cashback',
    db.Column('cashback_no', db.Numeric(10, 0)),
    db.Column('master_kbn', db.String(1)),
    db.Column('work_kbn', db.String(2)),
    db.Column('customer_id', db.String(8)),
    db.Column('policy_no', db.String(10)),
    db.Column('cashback_cost', db.Numeric(10, 0)),
    db.Column('cashback_status', db.String(3)),
    db.Column('order_date', db.DateTime),
    db.Column('create_date', db.DateTime),
    db.Column('renew_date', db.DateTime),
    db.Column('operate_cd', db.String(128)),
    db.Column('cashback_lastname_k', db.String(200)),
    db.Column('cashback_firstname_k', db.String(200)),
    db.Column('cashback_email', db.String(128)),
    db.Column('order_plan_month', db.Date),
    db.Column('contract_no', db.String(12)),
    db.Column('opt_contract_no', db.Numeric(10, 0)),
    db.Column('cashback_method', db.String(1)),
    db.Column('prog_status', db.String(2)),
    db.Column('send_mail_date', db.DateTime)
)


t_v_cashback_mst = db.Table(
    'v_cashback_mst',
    db.Column('policy_no', db.String(10)),
    db.Column('policy_name', db.String(128)),
    db.Column('policy_start_date', db.DateTime),
    db.Column('policy_end_date', db.DateTime),
    db.Column('cashback_cost', db.Numeric(10, 0)),
    db.Column('create_date', db.DateTime),
    db.Column('renew_date', db.DateTime),
    db.Column('operate_cd', db.String(128)),
    db.Column('cashback_month', db.Numeric(2, 0)),
    db.Column('cashback_method', db.String(1)),
    db.Column('open_term', db.DateTime)
)


t_v_cashpo_dat = db.Table(
    'v_cashpo_dat',
    db.Column('cashpo_no', db.String(10)),
    db.Column('epark_order_id', db.String(22)),
    db.Column('contbase_no', db.String(10)),
    db.Column('policy_no', db.String(10)),
    db.Column('coop_kind', db.String(4)),
    db.Column('coop_status', db.String(1)),
    db.Column('coop_nth_time', db.Numeric(2, 0)),
    db.Column('plan_coop_month', db.String(6)),
    db.Column('coop_date', db.Date),
    db.Column('plan_vest_date', db.Date),
    db.Column('create_date', db.DateTime),
    db.Column('renew_date', db.DateTime),
    db.Column('operate_cd', db.String(128))
)


t_v_cashpo_mst = db.Table(
    'v_cashpo_mst',
    db.Column('policy_no', db.String(10)),
    db.Column('policy_name', db.String(128)),
    db.Column('policy_start_date', db.Date),
    db.Column('policy_end_date', db.Date),
    db.Column('fee_extract_interval_months', db.Numeric(2, 0)),
    db.Column('cashpo_cost', db.Numeric(10, 0)),
    db.Column('vest_count', db.Numeric(2, 0)),
    db.Column('first_extract_elapsed_months', db.Numeric(2, 0)),
    db.Column('extract_interval_months', db.Numeric(2, 0)),
    db.Column('vest_elapsed_months', db.Numeric(2, 0)),
    db.Column('vest_business_day', db.Numeric(2, 0)),
    db.Column('create_date', db.DateTime),
    db.Column('renew_date', db.DateTime),
    db.Column('operate_cd', db.String(128))
)


t_v_condition_mst = db.Table(
    'v_condition_mst',
    db.Column('condition_no', db.Numeric(5, 0)),
    db.Column('create_date', db.DateTime),
    db.Column('renew_date', db.DateTime),
    db.Column('operate_cd', db.String(128)),
    db.Column('policy_no', db.String(10)),
    db.Column('plan_cd', db.String(8)),
    db.Column('campaign_cd', db.String(15)),
    db.Column('agency_cd', db.String(12))
)


t_v_consumption_tax = db.Table(
    'v_consumption_tax',
    db.Column('valid_date', db.DateTime),
    db.Column('tax_percent', db.Numeric(4, 1)),
    db.Column('create_date', db.DateTime),
    db.Column('renew_date', db.DateTime),
    db.Column('operate_cd', db.String(128)),
    db.Column('c_flag', db.String(1))
)


t_v_contents_bill_info = db.Table(
    'v_contents_bill_info',
    db.Column('bill_month', db.Date),
    db.Column('data_renbn', db.Numeric(7, 0)),
    db.Column('buy_date', db.DateTime),
    db.Column('provider_cd', db.String(8)),
    db.Column('service_cd', db.String(16)),
    db.Column('cost', db.Numeric(9, 0)),
    db.Column('tax_cost', db.Numeric(9, 0)),
    db.Column('tax_percent', db.Numeric(4, 1)),
    db.Column('note', db.String(512)),
    db.Column('contbase_no', db.String(10)),
    db.Column('taxfree_kbn', db.String(1)),
    db.Column('plan_cd', db.String(8)),
    db.Column('create_date', db.DateTime),
    db.Column('renew_date', db.DateTime),
    db.Column('operate_cd', db.String(128))
)


t_v_contract = db.Table(
    'v_contract',
    db.Column('contract_no', db.String(12)),
    db.Column('customer_id', db.String(8)),
    db.Column('contbase_no', db.String(10)),
    db.Column('cont_renbn', db.String(2)),
    db.Column('plan_cd', db.String(8)),
    db.Column('vc_no', db.String(10)),
    db.Column('order_status', db.String(2)),
    db.Column('cont_apply_date', db.DateTime),
    db.Column('cont_start_date', db.DateTime),
    db.Column('cont_end_date', db.DateTime),
    db.Column('cont_cancel_date', db.DateTime),
    db.Column('cancel_status', db.String(2)),
    db.Column('cancel_apply_date', db.DateTime),
    db.Column('cancel_date', db.DateTime),
    db.Column('agency_cd', db.String(12)),
    db.Column('campaign_cd', db.String(15)),
    db.Column('flets_apply_id', db.String(14)),
    db.Column('create_date', db.DateTime),
    db.Column('renew_date', db.DateTime),
    db.Column('operate_cd', db.String(128)),
    db.Column('c_flag', db.String(1)),
    db.Column('apply_status', db.String(2)),
    db.Column('unsuited_date', db.DateTime),
    db.Column('bill_start_date', db.DateTime),
    db.Column('apply_no', db.String(10)),
    db.Column('penalty_remission_month', db.Date),
    db.Column('cont_chgname', db.String(20)),
    db.Column('order_no', db.String(26)),
    db.Column('partner_channel', db.String(128)),
    db.Column('partner_info', db.String(1024)),
    db.Column('monthly_end_date', db.Date),
    db.Column('syonin_status', db.String(3)),
    db.Column('syonin_date', db.DateTime)
)


t_v_contract_opt = db.Table(
    'v_contract_opt',
    db.Column('opt_contract_no', db.Numeric(10, 0)),
    db.Column('customer_id', db.String(8)),
    db.Column('contbase_no', db.String(10)),
    db.Column('plan_cd', db.String(8)),
    db.Column('opt_status', db.String(2)),
    db.Column('opt_apply_date', db.DateTime),
    db.Column('opt_start_date', db.DateTime),
    db.Column('opt_end_date', db.DateTime),
    db.Column('opt_cancel_status', db.String(2)),
    db.Column('opt_cancel_apply', db.DateTime),
    db.Column('opt_cancel_date', db.DateTime),
    db.Column('opt_agency_cd', db.String(12)),
    db.Column('opt_campaign_cd', db.String(15)),
    db.Column('opt_kbn_cd', db.String(2)),
    db.Column('create_date', db.DateTime),
    db.Column('renew_date', db.DateTime),
    db.Column('operate_cd', db.String(128)),
    db.Column('c_flag', db.String(1)),
    db.Column('apply_status', db.String(2)),
    db.Column('unsuited_date', db.DateTime),
    db.Column('penalty_end_date', db.DateTime),
    db.Column('partner_channel', db.String(128)),
    db.Column('partner_info', db.String(1024))
)


t_v_cpass_demand_trans = db.Table(
    'v_cpass_demand_trans',
    db.Column('dmdto_id', db.String(12)),
    db.Column('cpass_cst_no', db.String(8)),
    db.Column('create_date', db.DateTime),
    db.Column('renew_date', db.DateTime),
    db.Column('operate_cd', db.String(128))
)


t_v_customer = db.Table(
    'v_customer',
    db.Column('custinfo_id', db.Numeric(10, 0)),
    db.Column('old_custid', db.String(15)),
    db.Column('firstname', db.String(20)),
    db.Column('firstname_k', db.String(20)),
    db.Column('lastname', db.String(50)),
    db.Column('lastname_k', db.String(100)),
    db.Column('cust_zip', db.String(7)),
    db.Column('cust_addr1', db.String(4)),
    db.Column('cust_addr2', db.String(50)),
    db.Column('cust_addr3', db.String(50)),
    db.Column('cust_addr1_k', db.String(6)),
    db.Column('cust_addr2_k', db.String(100)),
    db.Column('cust_addr3_k', db.String(100)),
    db.Column('cust_telno', db.String(11)),
    db.Column('cust_faxno', db.String(11)),
    db.Column('cust_user_type', db.String(1)),
    db.Column('cust_level', db.String(2)),
    db.Column('cust_fukushi', db.String(1)),
    db.Column('cust_chgdept', db.String(50)),
    db.Column('cust_chgpost', db.String(20)),
    db.Column('cust_chgname', db.String(20)),
    db.Column('cust_chgname_k', db.String(40)),
    db.Column('addr_defect_cre_date', db.DateTime),
    db.Column('addr_defect_off_date', db.DateTime),
    db.Column('create_date', db.DateTime),
    db.Column('renew_date', db.DateTime),
    db.Column('operate_cd', db.String(128)),
    db.Column('c_flag', db.String(1)),
    db.Column('stockholder_cd', db.String(10)),
    db.Column('address_code', db.String(11)),
    db.Column('cust_banchi1', db.String(40)),
    db.Column('cust_banchi2', db.String(20)),
    db.Column('cust_banchi3', db.String(20)),
    db.Column('cust_sex', db.String(1)),
    db.Column('cust_birth', db.DateTime)
)


t_v_customer_id_mng = db.Table(
    'v_customer_id_mng',
    db.Column('customer_id', db.String(8)),
    db.Column('custinfo_id', db.Numeric(10, 0)),
    db.Column('cust_password', db.String(32)),
    db.Column('cust_status', db.String(1)),
    db.Column('approval_date', db.DateTime),
    db.Column('pay_status', db.String(1)),
    db.Column('pay_status_renew_date', db.DateTime),
    db.Column('dmdto_id', db.String(12)),
    db.Column('dmd_method', db.String(1)),
    db.Column('apply_type', db.String(1)),
    db.Column('member_kind', db.String(1)),
    db.Column('cust_apply_date', db.DateTime),
    db.Column('cust_start_date', db.DateTime),
    db.Column('cust_end_apply_date', db.DateTime),
    db.Column('cust_cancel_date', db.DateTime),
    db.Column('cust_end_date', db.DateTime),
    db.Column('cust_email', db.String(128)),
    db.Column('create_date', db.DateTime),
    db.Column('renew_date', db.DateTime),
    db.Column('operate_cd', db.String(128)),
    db.Column('c_flag', db.String(1)),
    db.Column('cust_apply_status', db.String(2)),
    db.Column('old_isp', db.String(3)),
    db.Column('non_volume_discount', db.String(1))
)


t_v_customer_reserve = db.Table(
    'v_customer_reserve',
    db.Column('customer_id', db.String(8)),
    db.Column('change_status', db.String(1)),
    db.Column('change_date', db.DateTime),
    db.Column('cust_zip', db.String(7)),
    db.Column('cust_addr1', db.String(4)),
    db.Column('cust_addr2', db.String(50)),
    db.Column('cust_addr3', db.String(50)),
    db.Column('cust_telno', db.String(11)),
    db.Column('create_date', db.DateTime),
    db.Column('renew_date', db.DateTime),
    db.Column('operate_cd', db.String(128))
)


t_v_customer_sup = db.Table(
    'v_customer_sup',
    db.Column('incident_id', db.Numeric(10, 0)),
    db.Column('incident_kind', db.String(1)),
    db.Column('customer_id', db.String(8)),
    db.Column('contract_no', db.String(12)),
    db.Column('receipt_channel', db.String(2)),
    db.Column('base_plan_cd', db.String(8)),
    db.Column('add_plan_cd', db.String(8)),
    db.Column('opt_plan_cd', db.String(8)),
    db.Column('account_kind', db.String(1)),
    db.Column('account_name', db.String(128)),
    db.Column('contact_telno', db.String(16)),
    db.Column('contact_email', db.String(128)),
    db.Column('incident_status', db.String(2)),
    db.Column('lock_status', db.String(1)),
    db.Column('inq_item1', db.Numeric(10, 0)),
    db.Column('inq_item2', db.Numeric(10, 0)),
    db.Column('inq_item3', db.Numeric(10, 0)),
    db.Column('subject', db.String(1)),
    db.Column('area', db.String(8)),
    db.Column('line_traders', db.String(2)),
    db.Column('os', db.String(3)),
    db.Column('line_kind', db.Numeric(10, 0)),
    db.Column('document_kind', db.String(2048)),
    db.Column('inquiry_content', db.Text),
    db.Column('answer', db.Text),
    db.Column('register_cd', db.String(128)),
    db.Column('create_date', db.DateTime),
    db.Column('renew_date', db.DateTime),
    db.Column('operate_cd', db.String(128)),
    db.Column('c_flag', db.String(1)),
    db.Column('firstname', db.String(20)),
    db.Column('lastname', db.String(50)),
    db.Column('cust_zip', db.String(7)),
    db.Column('cust_addr1', db.String(4)),
    db.Column('cust_addr2', db.String(50)),
    db.Column('cust_addr3', db.String(50)),
    db.Column('cust_chgdept', db.String(50)),
    db.Column('cust_chgpost', db.String(20)),
    db.Column('cust_chgname', db.String(20)),
    db.Column('cust_telno', db.String(11)),
    db.Column('req_plan_cd', db.String(128))
)


t_v_demandto = db.Table(
    'v_demandto',
    db.Column('dmdto_id', db.String(12)),
    db.Column('valid_date', db.DateTime),
    db.Column('valid_flag', db.String(1)),
    db.Column('pwd_kbn', db.String(1)),
    db.Column('dmdto_status', db.String(2)),
    db.Column('ng_rsn', db.String(3)),
    db.Column('pay_chg_rsn', db.String(2)),
    db.Column('account_ask_no', db.String(20)),
    db.Column('demand_kbn', db.String(2)),
    db.Column('detail_kbn', db.String(2)),
    db.Column('detail_rsn', db.String(255)),
    db.Column('pwd_demandprint_kbn', db.String(1)),
    db.Column('old_dmdto_cd', db.String(15)),
    db.Column('cust_user_type', db.String(1)),
    db.Column('dmd_firstname', db.String(20)),
    db.Column('dmd_firstname_k', db.String(20)),
    db.Column('dmd_lastname', db.String(50)),
    db.Column('dmd_lastname_k', db.String(100)),
    db.Column('dmd_zip', db.String(7)),
    db.Column('dmd_addr1', db.String(4)),
    db.Column('dmd_addr2', db.String(50)),
    db.Column('dmd_addr3', db.String(50)),
    db.Column('dmd_addr1_k', db.String(6)),
    db.Column('dmd_addr2_k', db.String(100)),
    db.Column('dmd_addr3_k', db.String(100)),
    db.Column('dmd_telno', db.String(11)),
    db.Column('dmd_faxno', db.String(11)),
    db.Column('dmd_email', db.String(128)),
    db.Column('dmd_chgdept', db.String(50)),
    db.Column('dmd_chgtitle', db.String(20)),
    db.Column('dmd_chgname', db.String(20)),
    db.Column('dmd_chgname_k', db.String(40)),
    db.Column('cardkind', db.String(2)),
    db.Column('cardno', db.String(16)),
    db.Column('cardvalid', db.String(6)),
    db.Column('verify_no', db.String(8)),
    db.Column('verify_money', db.Numeric(8, 0)),
    db.Column('verify_date', db.DateTime),
    db.Column('agreement', db.String(1)),
    db.Column('pwd_stro_cd', db.String(1)),
    db.Column('trans_bankcd', db.String(4)),
    db.Column('trans_branchcd', db.String(3)),
    db.Column('trans_linecd', db.String(1)),
    db.Column('trans_acckind', db.String(1)),
    db.Column('trans_accno', db.String(7)),
    db.Column('trans_accname', db.String(60)),
    db.Column('kobetu_bankcd', db.String(4)),
    db.Column('kobetu_branchcd', db.String(3)),
    db.Column('kobetu_linecd', db.String(1)),
    db.Column('kobetu_acckind', db.String(1)),
    db.Column('kobetu_accno', db.String(7)),
    db.Column('kobetu_accname', db.String(60)),
    db.Column('dmdto_memo', db.String(128)),
    db.Column('end_date', db.DateTime),
    db.Column('addr_defect_cre_date', db.DateTime),
    db.Column('addr_defect_off_date', db.DateTime),
    db.Column('demand_renew_date', db.DateTime),
    db.Column('demand_operate_cd', db.String(128)),
    db.Column('payment_renew_date', db.DateTime),
    db.Column('payment_operate_cd', db.String(128)),
    db.Column('ol_new_user_trans_flag', db.String(1)),
    db.Column('create_date', db.DateTime),
    db.Column('renew_date', db.DateTime),
    db.Column('operate_cd', db.String(128)),
    db.Column('c_flag', db.String(1)),
    db.Column('confirm_kbn', db.String(1)),
    db.Column('ntt_assentor_name', db.String(128)),
    db.Column('ntt_kbn', db.String(2)),
    db.Column('ntt_apply_date', db.DateTime),
    db.Column('ntt_user_tel_no', db.String(11)),
    db.Column('entrepreneur_cd', db.String(4)),
    db.Column('address_code', db.String(11)),
    db.Column('dmd_banchi1', db.String(40)),
    db.Column('dmd_banchi2', db.String(20)),
    db.Column('dmd_banchi3', db.String(20)),
    db.Column('yuso_ptn_cd', db.String(2)),
    db.Column('kddi_dmd_kbn', db.String(1)),
    db.Column('kddi_mng_no', db.Numeric(10, 0)),
    db.Column('ntt_id', db.String(12)),
    db.Column('ntt_name', db.String(128)),
    db.Column('ntt_name_k', db.String(256)),
    db.Column('change_possible_date', db.DateTime),
    db.Column('tabal_keep_branch', db.String(4)),
    db.Column('nttf_kind', db.String(1))
)


t_v_device_change_dat = db.Table(
    'v_device_change_dat',
    db.Column('ws_common_id', db.String(20)),
    db.Column('ws_common_renbn', db.String(2)),
    db.Column('contract_no', db.String(12)),
    db.Column('opt_contract_no', db.Numeric(10, 0)),
    db.Column('isp_order_no', db.String(16)),
    db.Column('renew_date', db.DateTime),
    db.Column('create_date', db.DateTime),
    db.Column('operate_cd', db.String(128)),
    db.Column('c_flag', db.String(1)),
    db.Column('send_plan_date', db.DateTime),
    db.Column('send_date', db.DateTime),
    db.Column('apply_date', db.DateTime),
    db.Column('apply_kind', db.String(4)),
    db.Column('prog_status', db.String(2)),
    db.Column('send_service_cd', db.String(8)),
    db.Column('send_name_lastname', db.String(60)),
    db.Column('send_name_firstname', db.String(60)),
    db.Column('send_name_lastname_k', db.String(120)),
    db.Column('send_name_firstname_k', db.String(120)),
    db.Column('send_zip', db.String(7)),
    db.Column('send_todohuken', db.String(8)),
    db.Column('send_addr1', db.String(100)),
    db.Column('send_addr2', db.String(100)),
    db.Column('send_build_name', db.String(80)),
    db.Column('send_telno', db.String(11)),
    db.Column('ship_no', db.String(20)),
    db.Column('ship_decision_date', db.DateTime),
    db.Column('ship_comp_date', db.DateTime),
    db.Column('ship_return_date', db.DateTime),
    db.Column('send_status', db.String(2)),
    db.Column('org_isp_order_no', db.String(20)),
    db.Column('cont_sex', db.String(1)),
    db.Column('cont_birth', db.DateTime),
    db.Column('send_rent_device_cd', db.String(20)),
    db.Column('send_rent_lost_opt_contract_no', db.Numeric(10, 0)),
    db.Column('send_rent_return_limit_date', db.DateTime),
    db.Column('send_rent_return_flg', db.String(1)),
    db.Column('send_rent_return_date', db.DateTime)
)


t_v_device_cont = db.Table(
    'v_device_cont',
    db.Column('imei', db.String(15)),
    db.Column('isp_order_no', db.String(16)),
    db.Column('contbase_no', db.String(10)),
    db.Column('opt_contract_no', db.Numeric(10, 0)),
    db.Column('renew_date', db.DateTime),
    db.Column('create_date', db.DateTime),
    db.Column('operate_cd', db.String(128)),
    db.Column('c_flag', db.String(1)),
    db.Column('work_kind', db.String(2)),
    db.Column('rent_device_cd', db.String(20)),
    db.Column('device_status', db.String(2))
)


t_v_df_headrecord_mst = db.Table(
    'v_df_headrecord_mst',
    db.Column('hdrcmmcd', db.String(10)),
    db.Column('hdrcmmname', db.String(80)),
    db.Column('hdrgetdate', db.String(4)),
    db.Column('hdrbnkcd', db.String(4)),
    db.Column('hdrbnkname', db.String(92)),
    db.Column('hdrbrncd', db.String(3)),
    db.Column('hdrbrnname', db.String(60)),
    db.Column('hdracckind', db.String(1)),
    db.Column('hdraccno', db.String(7))
)


t_v_df_regreference = db.Table(
    'v_df_regreference',
    db.Column('dmdto_id', db.String(12)),
    db.Column('rgraccname', db.String(60)),
    db.Column('rgrbnkname', db.String(4)),
    db.Column('rgrbrncd', db.String(3)),
    db.Column('rgracckind', db.String(1)),
    db.Column('rgraccno', db.String(7)),
    db.Column('create_date', db.DateTime),
    db.Column('renew_date', db.DateTime)
)


t_v_disc_commission_old_isp = db.Table(
    'v_disc_commission_old_isp',
    db.Column('disc_cd', db.String(3)),
    db.Column('customer_id', db.String(8))
)


t_v_disc_mail_point = db.Table(
    'v_disc_mail_point',
    db.Column('customer_id', db.String(8)),
    db.Column('n', db.Numeric(2, 0))
)


t_v_disc_rel_mng = db.Table(
    'v_disc_rel_mng',
    db.Column('customer_id', db.String(8)),
    db.Column('contbase_no', db.String(10)),
    db.Column('cont_renbn', db.String(2)),
    db.Column('rel_contbase_no', db.String(10)),
    db.Column('rel_cont_renbn', db.String(2)),
    db.Column('create_date', db.DateTime),
    db.Column('renew_date', db.DateTime),
    db.Column('operate_cd', db.String(128)),
    db.Column('disc_cd', db.String(3)),
    db.Column('set_kind', db.String(1))
)


t_v_disc_reserve = db.Table(
    'v_disc_reserve',
    db.Column('customer_id', db.String(8)),
    db.Column('disc_type', db.String(2)),
    db.Column('disc_cd', db.String(3))
)


t_v_discount = db.Table(
    'v_discount',
    db.Column('contract_no', db.String(12)),
    db.Column('disc_renbn', db.Numeric(4, 0)),
    db.Column('opt_contract_no', db.Numeric(10, 0)),
    db.Column('disc_type', db.String(2)),
    db.Column('disc_cd', db.String(3)),
    db.Column('disc_start_date', db.DateTime),
    db.Column('disc_end_date', db.DateTime),
    db.Column('create_date', db.DateTime),
    db.Column('renew_date', db.DateTime),
    db.Column('operate_cd', db.String(128)),
    db.Column('c_flag', db.String(1)),
    db.Column('disc_status', db.String(2)),
    db.Column('cancel_date', db.DateTime)
)


t_v_discount_mst = db.Table(
    'v_discount_mst',
    db.Column('disc_type', db.String(2)),
    db.Column('disc_cd', db.String(3)),
    db.Column('disc_name', db.String(256)),
    db.Column('plan_cd', db.String(17)),
    db.Column('aitai_cd', db.String(13)),
    db.Column('disc_mst_init', db.Numeric(10, 0)),
    db.Column('disc_useal', db.Numeric(10, 0)),
    db.Column('disc_work', db.Numeric(10, 0)),
    db.Column('disc_term', db.Numeric(2, 0)),
    db.Column('open_term', db.DateTime),
    db.Column('disc_point', db.Numeric(10, 0)),
    db.Column('disc_memo', db.String(128)),
    db.Column('disc_start_date', db.DateTime),
    db.Column('disc_end_date', db.DateTime),
    db.Column('create_date', db.DateTime),
    db.Column('renew_date', db.DateTime),
    db.Column('operate_cd', db.String(128)),
    db.Column('partner_cd', db.String(10)),
    db.Column('bfcampaign', db.String(64)),
    db.Column('disc_term_round', db.String(1)),
    db.Column('policy_no', db.String(10)),
    db.Column('campaign_cd', db.String(15)),
    db.Column('ntt_service_name', db.String(64)),
    db.Column('ntt_e_agency_cd', db.String(8))
)


t_v_dmd_customer_total = db.Table(
    'v_dmd_customer_total',
    db.Column('dmd_month', db.String(6)),
    db.Column('customer_id', db.String(8)),
    db.Column('creditor_cd', db.String(1)),
    db.Column('creditor_subcd', db.String(3)),
    db.Column('taxable_total', db.Numeric(10, 0)),
    db.Column('taxfree_total', db.Numeric(10, 0)),
    db.Column('tax_total', db.Numeric(10, 0)),
    db.Column('tax_percent', db.Numeric(4, 1))
)


t_v_dmd_dmdto_total = db.Table(
    'v_dmd_dmdto_total',
    db.Column('dmd_no', db.String(13)),
    db.Column('creditor_cd', db.String(1)),
    db.Column('creditor_subcd', db.String(3)),
    db.Column('taxable_total', db.Numeric(10, 0)),
    db.Column('taxfree_total', db.Numeric(10, 0)),
    db.Column('tax_total', db.Numeric(10, 0)),
    db.Column('tax_percent', db.Numeric(4, 1))
)


t_v_dmd_job_mng = db.Table(
    'v_dmd_job_mng',
    db.Column('dmd_job_id', db.String(3)),
    db.Column('dmd_month', db.String(6)),
    db.Column('job_complete_date', db.DateTime)
)


t_v_docomol2_packet = db.Table(
    'v_docomol2_packet',
    db.Column('msisdn', db.String(11)),
    db.Column('packet_date', db.DateTime),
    db.Column('bl_status', db.Numeric(2, 0)),
    db.Column('packet', db.Numeric(16, 0)),
    db.Column('create_date', db.DateTime),
    db.Column('renew_date', db.DateTime),
    db.Column('operate_cd', db.String(128))
)


t_v_domain_lst_mst = db.Table(
    'v_domain_lst_mst',
    db.Column('domain_renbn', db.Numeric(3, 0)),
    db.Column('domain_id', db.String(32)),
    db.Column('domain_start_date', db.DateTime)
)


t_v_dti_sim_sms_log = db.Table(
    'v_dti_sim_sms_log',
    db.Column('used_month', db.Date),
    db.Column('line_no', db.Numeric(7, 0)),
    db.Column('telno', db.String(16)),
    db.Column('call_date', db.String(8)),
    db.Column('call_time', db.String(6)),
    db.Column('telno_dialed', db.String(32)),
    db.Column('dist_type', db.String(6)),
    db.Column('dist_detail', db.String(24)),
    db.Column('call_duration', db.String(7)),
    db.Column('time_period', db.String(24)),
    db.Column('discount', db.String(24)),
    db.Column('call_classification_1', db.String(24)),
    db.Column('call_classification_2', db.String(24)),
    db.Column('call_classification_3', db.String(24)),
    db.Column('separate_cd', db.String(1)),
    db.Column('isp_name', db.String(32)),
    db.Column('trans_type', db.String(100)),
    db.Column('trans_kbn', db.String(32)),
    db.Column('bill_month', db.Date),
    db.Column('contract_no', db.String(12)),
    db.Column('user_charge', db.Numeric(6, 0)),
    db.Column('bill_kbn_cd', db.String(2)),
    db.Column('create_date', db.DateTime),
    db.Column('renew_date', db.DateTime),
    db.Column('operate_cd', db.String(128))
)


t_v_dtisim_mst = db.Table(
    'v_dtisim_mst',
    db.Column('plan_cd', db.String(8)),
    db.Column('pt2_plancd', db.String(32)),
    db.Column('sim_type', db.String(1)),
    db.Column('use_kbn', db.String(1)),
    db.Column('pt2_account_add_kbn', db.String(1)),
    db.Column('plan_change_kbn', db.String(1)),
    db.Column('pt2_plancd_after', db.String(32)),
    db.Column('create_date', db.DateTime),
    db.Column('renew_date', db.DateTime),
    db.Column('operate_cd', db.String(128))
)


t_v_ea_dat = db.Table(
    'v_ea_dat',
    db.Column('ws_common_id', db.String(20)),
    db.Column('ws_common_renbn', db.String(2)),
    db.Column('contract_no', db.String(12)),
    db.Column('isp_order_no', db.String(20)),
    db.Column('apply_date', db.DateTime),
    db.Column('send_plan_date', db.DateTime),
    db.Column('send_date', db.DateTime),
    db.Column('apply_kind', db.String(4)),
    db.Column('prog_status', db.String(2)),
    db.Column('web_no', db.String(10)),
    db.Column('user_cd', db.String(1)),
    db.Column('ea_cust_id', db.String(8)),
    db.Column('ea_contract_id', db.String(8)),
    db.Column('appli_cd', db.String(50)),
    db.Column('pw_cd', db.String(50)),
    db.Column('plan_cd', db.String(10)),
    db.Column('connect_type', db.String(1)),
    db.Column('modem_cd', db.String(1)),
    db.Column('work_cd', db.String(1)),
    db.Column('zip', db.String(8)),
    db.Column('todohuken', db.String(8)),
    db.Column('gun', db.String(40)),
    db.Column('ku', db.String(40)),
    db.Column('area', db.String(40)),
    db.Column('chome', db.String(10)),
    db.Column('banchi', db.String(40)),
    db.Column('build_name', db.String(150)),
    db.Column('contract_telno', db.String(13)),
    db.Column('telno', db.String(13)),
    db.Column('toi_telno', db.String(13)),
    db.Column('email', db.String(120)),
    db.Column('ntt_cd', db.String(50)),
    db.Column('line_kind', db.String(1)),
    db.Column('line_name', db.String(60)),
    db.Column('analog_cd', db.String(1)),
    db.Column('linechg_cd', db.String(1)),
    db.Column('facility_cd', db.String(1)),
    db.Column('linein_cd', db.String(1)),
    db.Column('result_date', db.DateTime),
    db.Column('ntt_result', db.String(1)),
    db.Column('ntt_ng_rsn', db.String(2)),
    db.Column('trans_status', db.String(4)),
    db.Column('bill_date', db.DateTime),
    db.Column('change_date', db.DateTime),
    db.Column('work_date', db.DateTime),
    db.Column('campaign_cd', db.String(15)),
    db.Column('agency_cd', db.String(12)),
    db.Column('create_date', db.DateTime),
    db.Column('renew_date', db.DateTime),
    db.Column('operate_cd', db.String(128)),
    db.Column('c_flag', db.String(1)),
    db.Column('remark', db.String(80)),
    db.Column('acca_isp_order_no', db.String(20))
)


t_v_em_bill_info = db.Table(
    'v_em_bill_info',
    db.Column('em_cont_cd', db.String(10)),
    db.Column('used_month', db.Date),
    db.Column('em_plan_cd', db.String(6)),
    db.Column('create_date', db.DateTime),
    db.Column('renew_date', db.DateTime),
    db.Column('operate_cd', db.String(128)),
    db.Column('msisdn', db.String(11)),
    db.Column('bill_month', db.Date),
    db.Column('bill_kbn_cd', db.String(2)),
    db.Column('em_plan_name', db.String(44)),
    db.Column('cost', db.Numeric(9, 0)),
    db.Column('quantity', db.Numeric(19, 0)),
    db.Column('taxfree_kbn', db.String(1))
)


t_v_em_cont = db.Table(
    'v_em_cont',
    db.Column('contract_no', db.String(12)),
    db.Column('renew_date', db.DateTime),
    db.Column('create_date', db.DateTime),
    db.Column('operate_cd', db.String(128)),
    db.Column('c_flag', db.String(1)),
    db.Column('send_zip', db.String(7)),
    db.Column('send_todohuken', db.String(8)),
    db.Column('send_addr1', db.String(40)),
    db.Column('send_addr2', db.String(50)),
    db.Column('send_addr3', db.String(50)),
    db.Column('send_addr4', db.String(40)),
    db.Column('send_build_name', db.String(80)),
    db.Column('send_name', db.String(60)),
    db.Column('send_telno', db.String(11)),
    db.Column('user_telno', db.String(11)),
    db.Column('imei', db.String(15)),
    db.Column('iccid', db.String(19)),
    db.Column('msisdn', db.String(11)),
    db.Column('em_cont_cd', db.String(10)),
    db.Column('append_cancel_no', db.String(4)),
    db.Column('em_note', db.String(20)),
    db.Column('note1', db.String(100))
)


t_v_em_dat = db.Table(
    'v_em_dat',
    db.Column('ws_common_id', db.String(20)),
    db.Column('ws_common_renbn', db.String(2)),
    db.Column('contract_no', db.String(12)),
    db.Column('renew_date', db.DateTime),
    db.Column('create_date', db.DateTime),
    db.Column('operate_cd', db.String(128)),
    db.Column('c_flag', db.String(1)),
    db.Column('remark', db.String(80)),
    db.Column('apply_date', db.DateTime),
    db.Column('apply_kind', db.String(4)),
    db.Column('prog_status', db.String(2)),
    db.Column('send_plan_date', db.DateTime),
    db.Column('send_date', db.DateTime),
    db.Column('send_flg', db.String(1)),
    db.Column('isp_order_no', db.String(14)),
    db.Column('item_cd', db.String(10)),
    db.Column('item_num', db.Numeric(4, 0)),
    db.Column('item_opt', db.String(2)),
    db.Column('arrival_plan_date', db.DateTime),
    db.Column('arrival_plan_time', db.String(1)),
    db.Column('em_campaign_cd', db.String(6)),
    db.Column('ship_date', db.DateTime),
    db.Column('slip_no', db.String(20)),
    db.Column('ship_decision_date', db.DateTime),
    db.Column('arrival_date', db.DateTime),
    db.Column('ship_comp_date', db.DateTime),
    db.Column('send_status', db.String(2))
)


t_v_enduser = db.Table(
    'v_enduser',
    db.Column('contbase_no', db.String(10)),
    db.Column('enduser_flag', db.String(1)),
    db.Column('enduser_firstname', db.String(20)),
    db.Column('enduser_firstname_k', db.String(20)),
    db.Column('enduser_lastname', db.String(50)),
    db.Column('enduser_lastname_k', db.String(100)),
    db.Column('enduser_sex', db.String(1)),
    db.Column('enduser_birth', db.DateTime),
    db.Column('enduser_addr_flag', db.String(1)),
    db.Column('enduser_zip', db.String(7)),
    db.Column('enduser_addr1', db.String(4)),
    db.Column('enduser_addr2', db.String(50)),
    db.Column('enduser_addr3', db.String(50)),
    db.Column('renew_date', db.DateTime),
    db.Column('create_date', db.DateTime),
    db.Column('operate_cd', db.String(128)),
    db.Column('tid', db.String(16)),
    db.Column('identified_date', db.DateTime)
)


t_v_ex_acc_trans_err_cvs = db.Table(
    'v_ex_acc_trans_err_cvs',
    db.Column('ex_acc_trans_err_cvs_seq', db.Integer),
    db.Column('dmd_month', db.String(6)),
    db.Column('dmdto_id', db.String(12)),
    db.Column('create_date', db.DateTime),
    db.Column('renew_date', db.DateTime),
    db.Column('operate_cd', db.String(128)),
    db.Column('trans_kind', db.String(1)),
    db.Column('result_cd', db.String(1)),
    db.Column('dmd_no', db.String(13)),
    db.Column('demand_kbn', db.String(2)),
    db.Column('dmd_valid_date', db.DateTime),
    db.Column('cvs_next_month_flag', db.String(1)),
    db.Column('dmd_no_next_month', db.String(13)),
    db.Column('chg_dmd_kbn_flag', db.String(1)),
    db.Column('reserved_dmd_kbn_flag', db.String(1))
)


t_v_ex_acca_dat = db.Table(
    'v_ex_acca_dat',
    db.Column('ex_acca_dat_seq', db.Integer),
    db.Column('ws_common_id', db.String(20)),
    db.Column('ws_common_renbn', db.String(2)),
    db.Column('contract_no', db.String(12)),
    db.Column('isp_order_no', db.String(20)),
    db.Column('apply_date', db.DateTime),
    db.Column('send_plan_date', db.DateTime),
    db.Column('send_date', db.DateTime),
    db.Column('apply_kind', db.String(4)),
    db.Column('prog_status', db.String(2)),
    db.Column('apply_brand', db.String(2)),
    db.Column('order_cd', db.String(3)),
    db.Column('order_no', db.String(10)),
    db.Column('acca_no', db.String(60)),
    db.Column('service_id', db.String(10)),
    db.Column('gc_name', db.String(200)),
    db.Column('line_name', db.String(60)),
    db.Column('install_cd', db.String(1)),
    db.Column('zip', db.String(8)),
    db.Column('todohuken', db.String(8)),
    db.Column('gun', db.String(30)),
    db.Column('ku', db.String(30)),
    db.Column('area', db.String(30)),
    db.Column('banchi', db.String(50)),
    db.Column('build_name', db.String(120)),
    db.Column('telno', db.String(13)),
    db.Column('toi_telno', db.String(13)),
    db.Column('email', db.String(90)),
    db.Column('service_kind', db.String(1)),
    db.Column('isdn_type', db.String(1)),
    db.Column('user_cd', db.String(1)),
    db.Column('isdn_change', db.String(1)),
    db.Column('cpe_provider', db.String(1)),
    db.Column('cpe_installer', db.String(1)),
    db.Column('cpe_kind', db.String(3)),
    db.Column('nw_kind', db.String(1)),
    db.Column('ntt_result', db.String(1)),
    db.Column('ntt_ng1', db.String(2)),
    db.Column('ntt_ng2', db.String(2)),
    db.Column('ntt_notes', db.String(1800)),
    db.Column('reason_cd', db.String(2)),
    db.Column('result_date', db.DateTime),
    db.Column('change_date', db.DateTime),
    db.Column('ntt_work_date', db.DateTime),
    db.Column('complete_date', db.DateTime),
    db.Column('notes', db.String(600)),
    db.Column('entry_cd', db.String(10)),
    db.Column('campaign_cd', db.String(15)),
    db.Column('agency_cd', db.String(12)),
    db.Column('create_date', db.DateTime),
    db.Column('renew_date', db.DateTime),
    db.Column('operate_cd', db.String(128)),
    db.Column('c_flag', db.String(1)),
    db.Column('remark', db.String(80)),
    db.Column('owner_zip', db.String(8)),
    db.Column('owner_todohuken', db.String(8)),
    db.Column('owner_gun', db.String(30)),
    db.Column('owner_ku', db.String(30)),
    db.Column('owner_area', db.String(30)),
    db.Column('owner_banchi', db.String(50)),
    db.Column('owner_build_name', db.String(120)),
    db.Column('cert_telno', db.String(13))
)


t_v_ex_appli_send_dat = db.Table(
    'v_ex_appli_send_dat',
    db.Column('ex_appli_send_dat_seq', db.Integer),
    db.Column('send_no', db.String(20)),
    db.Column('renew_date', db.DateTime),
    db.Column('create_date', db.DateTime),
    db.Column('operate_cd', db.String(128)),
    db.Column('c_flag', db.String(1)),
    db.Column('remark', db.String(80)),
    db.Column('apply_date', db.DateTime),
    db.Column('customer_id', db.String(8)),
    db.Column('prog_status', db.String(2)),
    db.Column('direct_operate_cd', db.String(128)),
    db.Column('direct_date', db.DateTime),
    db.Column('ship_decision_date', db.DateTime),
    db.Column('slip_number', db.String(20)),
    db.Column('ship_result', db.String(16)),
    db.Column('send_name', db.String(72)),
    db.Column('send_chgdept', db.String(100)),
    db.Column('send_chgpost', db.String(40)),
    db.Column('send_chgname', db.String(40)),
    db.Column('send_zip', db.String(7)),
    db.Column('send_addr1', db.String(8)),
    db.Column('send_addr2', db.String(100)),
    db.Column('send_addr3', db.String(100)),
    db.Column('send_telno', db.String(11)),
    db.Column('memo', db.String(512)),
    db.Column('express_flg', db.String(1)),
    db.Column('sign_kind', db.String(1)),
    db.Column('res_base', db.String(4)),
    db.Column('res_base_num', db.Numeric(2, 0)),
    db.Column('res_add1', db.String(4)),
    db.Column('res_add1_num', db.Numeric(2, 0)),
    db.Column('res_add2', db.String(4)),
    db.Column('res_add2_num', db.Numeric(2, 0)),
    db.Column('res_add3', db.String(4)),
    db.Column('res_add3_num', db.Numeric(2, 0)),
    db.Column('res_add4', db.String(4)),
    db.Column('res_add4_num', db.Numeric(2, 0))
)


t_v_ex_au_set_info = db.Table(
    'v_ex_au_set_info',
    db.Column('ex_au_set_info_seq', db.Integer),
    db.Column('contract_no', db.String(12)),
    db.Column('isp_order_no', db.String(20)),
    db.Column('renew_date', db.DateTime),
    db.Column('create_date', db.DateTime),
    db.Column('operate_cd', db.String(128)),
    db.Column('c_flag', db.String(1)),
    db.Column('apply_date', db.DateTime),
    db.Column('auset_camp_status', db.String(2)),
    db.Column('auset_camp_available', db.String(1)),
    db.Column('auset_camp_ng_reason', db.String(1)),
    db.Column('auset_camp_disc', db.String(1)),
    db.Column('au_cont_telno', db.String(11)),
    db.Column('au_firstname_k', db.String(20)),
    db.Column('au_lastname_k', db.String(100)),
    db.Column('au_cont_zip', db.String(7)),
    db.Column('au_cont_todohuken', db.String(8)),
    db.Column('au_cont_shiku', db.String(60)),
    db.Column('au_cont_area_chome_banchi', db.String(60)),
    db.Column('au_cont_build_name', db.String(100)),
    db.Column('auset_appy_available', db.String(1)),
    db.Column('auset_appy_ng_reason', db.String(1)),
    db.Column('auset_appy_disc', db.String(1))
)


t_v_ex_bill_customer = db.Table(
    'v_ex_bill_customer',
    db.Column('bill_month', db.DateTime),
    db.Column('history', db.Numeric(22, 0)),
    db.Column('customer_id', db.String(8)),
    db.Column('creditor_cd', db.String(1)),
    db.Column('creditor_subcd', db.String(3)),
    db.Column('sales_dmd_kbn', db.String(1)),
    db.Column('tax_percent', db.Numeric(4, 1)),
    db.Column('taxable_total', db.Numeric(10, 0)),
    db.Column('taxfree_total', db.Numeric(10, 0)),
    db.Column('tax_total', db.Numeric(10, 0))
)


t_v_ex_bill_detail = db.Table(
    'v_ex_bill_detail',
    db.Column('create_date', db.DateTime),
    db.Column('renew_date', db.DateTime),
    db.Column('operate_cd', db.String(128)),
    db.Column('c_flag', db.String(1)),
    db.Column('bill_month', db.DateTime),
    db.Column('history', db.Numeric(22, 0)),
    db.Column('dmdto_id', db.String(12)),
    db.Column('customer_id', db.String(8)),
    db.Column('contract_no', db.String(12)),
    db.Column('bill_detailno', db.Numeric(5, 0)),
    db.Column('opt_contract_no', db.Numeric(10, 0)),
    db.Column('plan_cd', db.String(8)),
    db.Column('disc_type', db.String(2)),
    db.Column('disc_cd', db.String(3)),
    db.Column('bill_kbn_cd', db.String(2)),
    db.Column('bill_start', db.DateTime),
    db.Column('bill_end', db.DateTime),
    db.Column('quantity', db.Numeric(19, 0)),
    db.Column('unit', db.String(10)),
    db.Column('unit_cost', db.Numeric(10, 4)),
    db.Column('tax_cost', db.Numeric(9, 0)),
    db.Column('account_id', db.String(64)),
    db.Column('adjust_renban', db.Numeric(9, 0)),
    db.Column('cost', db.Numeric(9, 0)),
    db.Column('taxfree_kbn', db.String(1)),
    db.Column('kihon_tuika_kbn', db.String(1)),
    db.Column('kddi_plan_cd', db.String(10)),
    db.Column('plan_name', db.String(128)),
    db.Column('creditor_cd', db.String(1)),
    db.Column('ntt_plan_cd', db.String(10)),
    db.Column('creditor_subcd', db.String(3)),
    db.Column('sales_dmd_kbn', db.String(1)),
    db.Column('demand_count', db.Numeric(2, 0)),
    db.Column('jpayment_trade_no', db.String(64)),
    db.Column('tax_percent', db.Numeric(4, 1))
)


t_v_ex_bill_dmd = db.Table(
    'v_ex_bill_dmd',
    db.Column('bill_month', db.DateTime),
    db.Column('history', db.Numeric(22, 0)),
    db.Column('dmdto_id', db.String(12)),
    db.Column('creditor_cd', db.String(1)),
    db.Column('creditor_subcd', db.String(3)),
    db.Column('sales_dmd_kbn', db.String(1)),
    db.Column('use_aim', db.Numeric(1, 0)),
    db.Column('stat_kbn', db.Numeric(1, 0)),
    db.Column('tax_percent', db.Numeric(4, 1)),
    db.Column('taxable_total', db.Numeric(10, 0)),
    db.Column('taxfree_total', db.Numeric(10, 0)),
    db.Column('tax_total', db.Numeric(10, 0))
)


t_v_ex_cashback = db.Table(
    'v_ex_cashback',
    db.Column('ex_cashback_seq', db.Integer),
    db.Column('cashback_no', db.Numeric(10, 0)),
    db.Column('master_kbn', db.String(1)),
    db.Column('work_kbn', db.String(2)),
    db.Column('customer_id', db.String(8)),
    db.Column('policy_no', db.String(10)),
    db.Column('cashback_cost', db.Numeric(10, 0)),
    db.Column('cashback_status', db.String(3)),
    db.Column('order_date', db.DateTime),
    db.Column('create_date', db.DateTime),
    db.Column('renew_date', db.DateTime),
    db.Column('operate_cd', db.String(128)),
    db.Column('cashback_lastname_k', db.String(200)),
    db.Column('cashback_firstname_k', db.String(200)),
    db.Column('cashback_email', db.String(128)),
    db.Column('order_plan_month', db.Date),
    db.Column('contract_no', db.String(12)),
    db.Column('opt_contract_no', db.Numeric(10, 0)),
    db.Column('cashback_method', db.String(1)),
    db.Column('prog_status', db.String(2)),
    db.Column('send_mail_date', db.DateTime)
)


t_v_ex_cashpo_dat = db.Table(
    'v_ex_cashpo_dat',
    db.Column('ex_cashpo_dat_seq', db.Integer),
    db.Column('cashpo_no', db.String(10)),
    db.Column('epark_order_id', db.String(22)),
    db.Column('contbase_no', db.String(10)),
    db.Column('policy_no', db.String(10)),
    db.Column('coop_kind', db.String(4)),
    db.Column('coop_status', db.String(1)),
    db.Column('coop_nth_time', db.Numeric(2, 0)),
    db.Column('plan_coop_month', db.String(6)),
    db.Column('coop_date', db.Date),
    db.Column('plan_vest_date', db.Date),
    db.Column('create_date', db.DateTime),
    db.Column('renew_date', db.DateTime),
    db.Column('operate_cd', db.String(128))
)


t_v_ex_contract = db.Table(
    'v_ex_contract',
    db.Column('ex_contract_seq', db.Integer),
    db.Column('contract_no', db.String(12)),
    db.Column('customer_id', db.String(8)),
    db.Column('contbase_no', db.String(10)),
    db.Column('cont_renbn', db.String(2)),
    db.Column('plan_cd', db.String(8)),
    db.Column('vc_no', db.String(10)),
    db.Column('order_status', db.String(2)),
    db.Column('cont_apply_date', db.DateTime),
    db.Column('cont_start_date', db.DateTime),
    db.Column('cont_end_date', db.DateTime),
    db.Column('cont_cancel_date', db.DateTime),
    db.Column('cancel_status', db.String(2)),
    db.Column('cancel_apply_date', db.DateTime),
    db.Column('cancel_date', db.DateTime),
    db.Column('agency_cd', db.String(12)),
    db.Column('campaign_cd', db.String(15)),
    db.Column('flets_apply_id', db.String(14)),
    db.Column('create_date', db.DateTime),
    db.Column('renew_date', db.DateTime),
    db.Column('operate_cd', db.String(128)),
    db.Column('c_flag', db.String(1)),
    db.Column('apply_status', db.String(2)),
    db.Column('unsuited_date', db.DateTime),
    db.Column('bill_start_date', db.DateTime),
    db.Column('apply_no', db.String(10)),
    db.Column('penalty_remission_month', db.Date),
    db.Column('cont_chgname', db.String(20)),
    db.Column('order_no', db.String(26)),
    db.Column('partner_channel', db.String(128)),
    db.Column('partner_info', db.String(1024)),
    db.Column('monthly_end_date', db.Date),
    db.Column('syonin_status', db.String(3)),
    db.Column('syonin_date', db.DateTime)
)


t_v_ex_contract_opt = db.Table(
    'v_ex_contract_opt',
    db.Column('ex_contract_opt_seq', db.Integer),
    db.Column('opt_contract_no', db.Numeric(10, 0)),
    db.Column('customer_id', db.String(8)),
    db.Column('contbase_no', db.String(10)),
    db.Column('plan_cd', db.String(8)),
    db.Column('opt_status', db.String(2)),
    db.Column('opt_apply_date', db.DateTime),
    db.Column('opt_start_date', db.DateTime),
    db.Column('opt_end_date', db.DateTime),
    db.Column('opt_cancel_status', db.String(2)),
    db.Column('opt_cancel_apply', db.DateTime),
    db.Column('opt_cancel_date', db.DateTime),
    db.Column('opt_agency_cd', db.String(12)),
    db.Column('opt_campaign_cd', db.String(15)),
    db.Column('opt_kbn_cd', db.String(2)),
    db.Column('create_date', db.DateTime),
    db.Column('renew_date', db.DateTime),
    db.Column('operate_cd', db.String(128)),
    db.Column('c_flag', db.String(1)),
    db.Column('apply_status', db.String(2)),
    db.Column('unsuited_date', db.DateTime),
    db.Column('penalty_end_date', db.DateTime),
    db.Column('partner_channel', db.String(128)),
    db.Column('partner_info', db.String(1024))
)


t_v_ex_customer = db.Table(
    'v_ex_customer',
    db.Column('ex_customer_seq', db.Integer),
    db.Column('custinfo_id', db.Numeric(10, 0)),
    db.Column('old_custid', db.String(15)),
    db.Column('firstname', db.String(20)),
    db.Column('firstname_k', db.String(20)),
    db.Column('lastname', db.String(50)),
    db.Column('lastname_k', db.String(100)),
    db.Column('cust_zip', db.String(7)),
    db.Column('cust_addr1', db.String(4)),
    db.Column('cust_addr2', db.String(50)),
    db.Column('cust_addr3', db.String(50)),
    db.Column('cust_addr1_k', db.String(6)),
    db.Column('cust_addr2_k', db.String(100)),
    db.Column('cust_addr3_k', db.String(100)),
    db.Column('cust_telno', db.String(11)),
    db.Column('cust_faxno', db.String(11)),
    db.Column('cust_user_type', db.String(1)),
    db.Column('cust_level', db.String(2)),
    db.Column('cust_fukushi', db.String(1)),
    db.Column('cust_chgdept', db.String(50)),
    db.Column('cust_chgpost', db.String(20)),
    db.Column('cust_chgname', db.String(20)),
    db.Column('cust_chgname_k', db.String(40)),
    db.Column('addr_defect_cre_date', db.DateTime),
    db.Column('addr_defect_off_date', db.DateTime),
    db.Column('create_date', db.DateTime),
    db.Column('renew_date', db.DateTime),
    db.Column('operate_cd', db.String(128)),
    db.Column('c_flag', db.String(1)),
    db.Column('stockholder_cd', db.String(10)),
    db.Column('address_code', db.String(11)),
    db.Column('cust_banchi1', db.String(40)),
    db.Column('cust_banchi2', db.String(20)),
    db.Column('cust_banchi3', db.String(20)),
    db.Column('cust_sex', db.String(1)),
    db.Column('cust_birth', db.DateTime)
)


t_v_ex_customer_id_mng = db.Table(
    'v_ex_customer_id_mng',
    db.Column('ex_customer_id_mng_seq', db.Integer),
    db.Column('customer_id', db.String(8)),
    db.Column('custinfo_id', db.Numeric(10, 0)),
    db.Column('cust_password', db.String(32)),
    db.Column('cust_status', db.String(1)),
    db.Column('approval_date', db.DateTime),
    db.Column('pay_status', db.String(1)),
    db.Column('pay_status_renew_date', db.DateTime),
    db.Column('dmdto_id', db.String(12)),
    db.Column('dmd_method', db.String(1)),
    db.Column('apply_type', db.String(1)),
    db.Column('member_kind', db.String(1)),
    db.Column('cust_apply_date', db.DateTime),
    db.Column('cust_start_date', db.DateTime),
    db.Column('cust_end_apply_date', db.DateTime),
    db.Column('cust_cancel_date', db.DateTime),
    db.Column('cust_end_date', db.DateTime),
    db.Column('cust_email', db.String(128)),
    db.Column('create_date', db.DateTime),
    db.Column('renew_date', db.DateTime),
    db.Column('operate_cd', db.String(128)),
    db.Column('c_flag', db.String(1)),
    db.Column('cust_apply_status', db.String(2)),
    db.Column('old_isp', db.String(3)),
    db.Column('non_volume_discount', db.String(1))
)


t_v_ex_customer_reserve = db.Table(
    'v_ex_customer_reserve',
    db.Column('ex_customer_reserve_seq', db.Integer),
    db.Column('customer_id', db.String(8)),
    db.Column('change_status', db.String(1)),
    db.Column('change_date', db.DateTime),
    db.Column('cust_zip', db.String(7)),
    db.Column('cust_addr1', db.String(4)),
    db.Column('cust_addr2', db.String(50)),
    db.Column('cust_addr3', db.String(50)),
    db.Column('cust_telno', db.String(11)),
    db.Column('create_date', db.DateTime),
    db.Column('renew_date', db.DateTime),
    db.Column('operate_cd', db.String(128))
)


t_v_ex_demandto = db.Table(
    'v_ex_demandto',
    db.Column('ex_demandto_seq', db.Integer),
    db.Column('dmdto_id', db.String(12)),
    db.Column('valid_date', db.DateTime),
    db.Column('valid_flag', db.String(1)),
    db.Column('pwd_kbn', db.String(1)),
    db.Column('dmdto_status', db.String(2)),
    db.Column('ng_rsn', db.String(3)),
    db.Column('pay_chg_rsn', db.String(2)),
    db.Column('account_ask_no', db.String(20)),
    db.Column('demand_kbn', db.String(2)),
    db.Column('detail_kbn', db.String(2)),
    db.Column('detail_rsn', db.String(255)),
    db.Column('pwd_demandprint_kbn', db.String(1)),
    db.Column('old_dmdto_cd', db.String(15)),
    db.Column('cust_user_type', db.String(1)),
    db.Column('dmd_firstname', db.String(20)),
    db.Column('dmd_firstname_k', db.String(20)),
    db.Column('dmd_lastname', db.String(50)),
    db.Column('dmd_lastname_k', db.String(100)),
    db.Column('dmd_zip', db.String(7)),
    db.Column('dmd_addr1', db.String(4)),
    db.Column('dmd_addr2', db.String(50)),
    db.Column('dmd_addr3', db.String(50)),
    db.Column('dmd_addr1_k', db.String(6)),
    db.Column('dmd_addr2_k', db.String(100)),
    db.Column('dmd_addr3_k', db.String(100)),
    db.Column('dmd_telno', db.String(11)),
    db.Column('dmd_faxno', db.String(11)),
    db.Column('dmd_email', db.String(128)),
    db.Column('dmd_chgdept', db.String(50)),
    db.Column('dmd_chgtitle', db.String(20)),
    db.Column('dmd_chgname', db.String(20)),
    db.Column('dmd_chgname_k', db.String(40)),
    db.Column('cardkind', db.String(2)),
    db.Column('cardno', db.String(16)),
    db.Column('cardvalid', db.String(6)),
    db.Column('verify_no', db.String(8)),
    db.Column('verify_money', db.Numeric(8, 0)),
    db.Column('verify_date', db.DateTime),
    db.Column('agreement', db.String(1)),
    db.Column('pwd_stro_cd', db.String(1)),
    db.Column('trans_bankcd', db.String(4)),
    db.Column('trans_branchcd', db.String(3)),
    db.Column('trans_linecd', db.String(1)),
    db.Column('trans_acckind', db.String(1)),
    db.Column('trans_accno', db.String(7)),
    db.Column('trans_accname', db.String(60)),
    db.Column('kobetu_bankcd', db.String(4)),
    db.Column('kobetu_branchcd', db.String(3)),
    db.Column('kobetu_linecd', db.String(1)),
    db.Column('kobetu_acckind', db.String(1)),
    db.Column('kobetu_accno', db.String(7)),
    db.Column('kobetu_accname', db.String(60)),
    db.Column('dmdto_memo', db.String(128)),
    db.Column('end_date', db.DateTime),
    db.Column('addr_defect_cre_date', db.DateTime),
    db.Column('addr_defect_off_date', db.DateTime),
    db.Column('demand_renew_date', db.DateTime),
    db.Column('demand_operate_cd', db.String(128)),
    db.Column('payment_renew_date', db.DateTime),
    db.Column('payment_operate_cd', db.String(128)),
    db.Column('ol_new_user_trans_flag', db.String(1)),
    db.Column('create_date', db.DateTime),
    db.Column('renew_date', db.DateTime),
    db.Column('operate_cd', db.String(128)),
    db.Column('c_flag', db.String(1)),
    db.Column('confirm_kbn', db.String(1)),
    db.Column('ntt_assentor_name', db.String(128)),
    db.Column('ntt_kbn', db.String(2)),
    db.Column('ntt_apply_date', db.DateTime),
    db.Column('ntt_user_tel_no', db.String(11)),
    db.Column('entrepreneur_cd', db.String(4)),
    db.Column('address_code', db.String(11)),
    db.Column('dmd_banchi1', db.String(40)),
    db.Column('dmd_banchi2', db.String(20)),
    db.Column('dmd_banchi3', db.String(20)),
    db.Column('yuso_ptn_cd', db.String(2)),
    db.Column('kddi_dmd_kbn', db.String(1)),
    db.Column('kddi_mng_no', db.Numeric(10, 0)),
    db.Column('ntt_id', db.String(12)),
    db.Column('ntt_name', db.String(128)),
    db.Column('ntt_name_k', db.String(256)),
    db.Column('change_possible_date', db.DateTime),
    db.Column('tabal_keep_branch', db.String(4)),
    db.Column('nttf_kind', db.String(1))
)


t_v_ex_device_change_dat = db.Table(
    'v_ex_device_change_dat',
    db.Column('ex_device_change_dat_seq', db.Integer),
    db.Column('ws_common_id', db.String(20)),
    db.Column('ws_common_renbn', db.String(2)),
    db.Column('contract_no', db.String(12)),
    db.Column('opt_contract_no', db.Numeric(10, 0)),
    db.Column('isp_order_no', db.String(16)),
    db.Column('renew_date', db.DateTime),
    db.Column('create_date', db.DateTime),
    db.Column('operate_cd', db.String(128)),
    db.Column('c_flag', db.String(1)),
    db.Column('send_plan_date', db.DateTime),
    db.Column('send_date', db.DateTime),
    db.Column('apply_date', db.DateTime),
    db.Column('apply_kind', db.String(4)),
    db.Column('prog_status', db.String(2)),
    db.Column('send_service_cd', db.String(8)),
    db.Column('send_name_lastname', db.String(60)),
    db.Column('send_name_firstname', db.String(60)),
    db.Column('send_name_lastname_k', db.String(120)),
    db.Column('send_name_firstname_k', db.String(120)),
    db.Column('send_zip', db.String(7)),
    db.Column('send_todohuken', db.String(8)),
    db.Column('send_addr1', db.String(100)),
    db.Column('send_addr2', db.String(100)),
    db.Column('send_build_name', db.String(80)),
    db.Column('send_telno', db.String(11)),
    db.Column('ship_no', db.String(20)),
    db.Column('ship_decision_date', db.DateTime),
    db.Column('ship_comp_date', db.DateTime),
    db.Column('ship_return_date', db.DateTime),
    db.Column('send_status', db.String(2)),
    db.Column('org_isp_order_no', db.String(20)),
    db.Column('cont_sex', db.String(1)),
    db.Column('cont_birth', db.DateTime),
    db.Column('send_rent_device_cd', db.String(20)),
    db.Column('send_rent_lost_opt_contract_no', db.Numeric(10, 0)),
    db.Column('send_rent_return_limit_date', db.DateTime),
    db.Column('send_rent_return_flg', db.String(1)),
    db.Column('send_rent_return_date', db.DateTime)
)


t_v_ex_device_cont = db.Table(
    'v_ex_device_cont',
    db.Column('ex_device_cont_seq', db.Integer),
    db.Column('imei', db.String(15)),
    db.Column('isp_order_no', db.String(16)),
    db.Column('contbase_no', db.String(10)),
    db.Column('opt_contract_no', db.Numeric(10, 0)),
    db.Column('renew_date', db.DateTime),
    db.Column('create_date', db.DateTime),
    db.Column('operate_cd', db.String(128)),
    db.Column('c_flag', db.String(1)),
    db.Column('work_kind', db.String(2)),
    db.Column('rent_device_cd', db.String(20)),
    db.Column('device_status', db.String(2))
)


t_v_ex_discount = db.Table(
    'v_ex_discount',
    db.Column('ex_discount_seq', db.Integer),
    db.Column('contract_no', db.String(12)),
    db.Column('disc_renbn', db.Numeric(4, 0)),
    db.Column('opt_contract_no', db.Numeric(10, 0)),
    db.Column('disc_type', db.String(2)),
    db.Column('disc_cd', db.String(3)),
    db.Column('disc_start_date', db.DateTime),
    db.Column('disc_end_date', db.DateTime),
    db.Column('create_date', db.DateTime),
    db.Column('renew_date', db.DateTime),
    db.Column('operate_cd', db.String(128)),
    db.Column('c_flag', db.String(1)),
    db.Column('disc_status', db.String(2)),
    db.Column('cancel_date', db.DateTime)
)


t_v_ex_discount_mst = db.Table(
    'v_ex_discount_mst',
    db.Column('ex_discount_mst_seq', db.Integer),
    db.Column('disc_type', db.String(2)),
    db.Column('disc_cd', db.String(3)),
    db.Column('disc_name', db.String(256)),
    db.Column('plan_cd', db.String(17)),
    db.Column('aitai_cd', db.String(13)),
    db.Column('disc_mst_init', db.Numeric(10, 0)),
    db.Column('disc_useal', db.Numeric(10, 0)),
    db.Column('disc_work', db.Numeric(10, 0)),
    db.Column('disc_term', db.Numeric(2, 0)),
    db.Column('open_term', db.DateTime),
    db.Column('disc_point', db.Numeric(10, 0)),
    db.Column('disc_memo', db.String(128)),
    db.Column('disc_start_date', db.DateTime),
    db.Column('disc_end_date', db.DateTime),
    db.Column('create_date', db.DateTime),
    db.Column('renew_date', db.DateTime),
    db.Column('operate_cd', db.String(128)),
    db.Column('partner_cd', db.String(10)),
    db.Column('bfcampaign', db.String(64)),
    db.Column('disc_term_round', db.String(1)),
    db.Column('policy_no', db.String(10)),
    db.Column('campaign_cd', db.String(15)),
    db.Column('ntt_service_name', db.String(64)),
    db.Column('ntt_e_agency_cd', db.String(8))
)


t_v_ex_dtisim_mst = db.Table(
    'v_ex_dtisim_mst',
    db.Column('ex_dtisim_mst_seq', db.Integer),
    db.Column('plan_cd', db.String(8)),
    db.Column('pt2_plancd', db.String(32)),
    db.Column('sim_type', db.String(1)),
    db.Column('use_kbn', db.String(1)),
    db.Column('pt2_account_add_kbn', db.String(1)),
    db.Column('plan_change_kbn', db.String(1)),
    db.Column('pt2_plancd_after', db.String(32)),
    db.Column('create_date', db.DateTime),
    db.Column('renew_date', db.DateTime),
    db.Column('operate_cd', db.String(128))
)


t_v_ex_ea_dat = db.Table(
    'v_ex_ea_dat',
    db.Column('ex_ea_dat_seq', db.Integer),
    db.Column('ws_common_id', db.String(20)),
    db.Column('ws_common_renbn', db.String(2)),
    db.Column('contract_no', db.String(12)),
    db.Column('isp_order_no', db.String(20)),
    db.Column('apply_date', db.DateTime),
    db.Column('send_plan_date', db.DateTime),
    db.Column('send_date', db.DateTime),
    db.Column('apply_kind', db.String(4)),
    db.Column('prog_status', db.String(2)),
    db.Column('web_no', db.String(10)),
    db.Column('user_cd', db.String(1)),
    db.Column('ea_cust_id', db.String(8)),
    db.Column('ea_contract_id', db.String(8)),
    db.Column('appli_cd', db.String(50)),
    db.Column('pw_cd', db.String(50)),
    db.Column('plan_cd', db.String(10)),
    db.Column('connect_type', db.String(1)),
    db.Column('modem_cd', db.String(1)),
    db.Column('work_cd', db.String(1)),
    db.Column('zip', db.String(8)),
    db.Column('todohuken', db.String(8)),
    db.Column('gun', db.String(40)),
    db.Column('ku', db.String(40)),
    db.Column('area', db.String(40)),
    db.Column('chome', db.String(10)),
    db.Column('banchi', db.String(40)),
    db.Column('build_name', db.String(150)),
    db.Column('contract_telno', db.String(13)),
    db.Column('telno', db.String(13)),
    db.Column('toi_telno', db.String(13)),
    db.Column('email', db.String(120)),
    db.Column('ntt_cd', db.String(50)),
    db.Column('line_kind', db.String(1)),
    db.Column('line_name', db.String(60)),
    db.Column('analog_cd', db.String(1)),
    db.Column('linechg_cd', db.String(1)),
    db.Column('facility_cd', db.String(1)),
    db.Column('linein_cd', db.String(1)),
    db.Column('result_date', db.DateTime),
    db.Column('ntt_result', db.String(1)),
    db.Column('ntt_ng_rsn', db.String(2)),
    db.Column('trans_status', db.String(4)),
    db.Column('bill_date', db.DateTime),
    db.Column('change_date', db.DateTime),
    db.Column('work_date', db.DateTime),
    db.Column('campaign_cd', db.String(15)),
    db.Column('agency_cd', db.String(12)),
    db.Column('create_date', db.DateTime),
    db.Column('renew_date', db.DateTime),
    db.Column('operate_cd', db.String(128)),
    db.Column('c_flag', db.String(1)),
    db.Column('remark', db.String(80)),
    db.Column('acca_isp_order_no', db.String(20))
)


t_v_ex_em_cont = db.Table(
    'v_ex_em_cont',
    db.Column('ex_em_cont_seq', db.Integer),
    db.Column('contract_no', db.String(12)),
    db.Column('renew_date', db.DateTime),
    db.Column('create_date', db.DateTime),
    db.Column('operate_cd', db.String(128)),
    db.Column('c_flag', db.String(1)),
    db.Column('send_zip', db.String(7)),
    db.Column('send_todohuken', db.String(8)),
    db.Column('send_addr1', db.String(40)),
    db.Column('send_addr2', db.String(50)),
    db.Column('send_addr3', db.String(50)),
    db.Column('send_addr4', db.String(40)),
    db.Column('send_build_name', db.String(80)),
    db.Column('send_name', db.String(60)),
    db.Column('send_telno', db.String(11)),
    db.Column('user_telno', db.String(11)),
    db.Column('imei', db.String(15)),
    db.Column('iccid', db.String(19)),
    db.Column('msisdn', db.String(11)),
    db.Column('em_cont_cd', db.String(10)),
    db.Column('append_cancel_no', db.String(4)),
    db.Column('em_note', db.String(20)),
    db.Column('note1', db.String(100))
)


t_v_ex_em_dat = db.Table(
    'v_ex_em_dat',
    db.Column('ex_em_dat_seq', db.Integer),
    db.Column('ws_common_id', db.String(20)),
    db.Column('ws_common_renbn', db.String(2)),
    db.Column('contract_no', db.String(12)),
    db.Column('renew_date', db.DateTime),
    db.Column('create_date', db.DateTime),
    db.Column('operate_cd', db.String(128)),
    db.Column('c_flag', db.String(1)),
    db.Column('remark', db.String(80)),
    db.Column('apply_date', db.DateTime),
    db.Column('apply_kind', db.String(4)),
    db.Column('prog_status', db.String(2)),
    db.Column('send_plan_date', db.DateTime),
    db.Column('send_date', db.DateTime),
    db.Column('send_flg', db.String(1)),
    db.Column('isp_order_no', db.String(14)),
    db.Column('item_cd', db.String(10)),
    db.Column('item_num', db.Numeric(4, 0)),
    db.Column('item_opt', db.String(2)),
    db.Column('arrival_plan_date', db.DateTime),
    db.Column('arrival_plan_time', db.String(1)),
    db.Column('em_campaign_cd', db.String(6)),
    db.Column('ship_date', db.DateTime),
    db.Column('slip_no', db.String(20)),
    db.Column('ship_decision_date', db.DateTime),
    db.Column('arrival_date', db.DateTime),
    db.Column('ship_comp_date', db.DateTime),
    db.Column('send_status', db.String(2))
)


t_v_ex_enduser = db.Table(
    'v_ex_enduser',
    db.Column('ex_enduser_seq', db.Integer),
    db.Column('contbase_no', db.String(10)),
    db.Column('enduser_flag', db.String(1)),
    db.Column('enduser_firstname', db.String(20)),
    db.Column('enduser_firstname_k', db.String(20)),
    db.Column('enduser_lastname', db.String(50)),
    db.Column('enduser_lastname_k', db.String(100)),
    db.Column('enduser_sex', db.String(1)),
    db.Column('enduser_birth', db.DateTime),
    db.Column('enduser_addr_flag', db.String(1)),
    db.Column('enduser_zip', db.String(7)),
    db.Column('enduser_addr1', db.String(4)),
    db.Column('enduser_addr2', db.String(50)),
    db.Column('enduser_addr3', db.String(50)),
    db.Column('renew_date', db.DateTime),
    db.Column('create_date', db.DateTime),
    db.Column('operate_cd', db.String(128)),
    db.Column('tid', db.String(16)),
    db.Column('identified_date', db.DateTime)
)


t_v_ex_goods_dat = db.Table(
    'v_ex_goods_dat',
    db.Column('ex_goods_dat_seq', db.Integer),
    db.Column('ws_common_id', db.String(20)),
    db.Column('ws_common_renbn', db.String(2)),
    db.Column('contract_no', db.String(12)),
    db.Column('renew_date', db.DateTime),
    db.Column('create_date', db.DateTime),
    db.Column('operate_cd', db.String(128)),
    db.Column('remark', db.String(80)),
    db.Column('apply_date', db.DateTime),
    db.Column('apply_kind', db.String(4)),
    db.Column('prog_status', db.String(2)),
    db.Column('send_plan_date', db.DateTime),
    db.Column('send_date', db.DateTime),
    db.Column('model_number', db.String(64)),
    db.Column('order_no', db.String(16)),
    db.Column('deliver_date', db.DateTime),
    db.Column('deliver_time', db.String(2)),
    db.Column('deliver_firstname', db.String(20)),
    db.Column('deliver_lastname', db.String(50)),
    db.Column('deliver_chgdept', db.String(50)),
    db.Column('deliver_chgpost', db.String(20)),
    db.Column('deliver_chgname', db.String(20)),
    db.Column('deliver_zip', db.String(8)),
    db.Column('deliver_todohuken', db.String(8)),
    db.Column('deliver_gun', db.String(40)),
    db.Column('deliver_ku', db.String(40)),
    db.Column('deliver_area', db.String(40)),
    db.Column('deliver_chome', db.String(10)),
    db.Column('deliver_banchi', db.String(40)),
    db.Column('deliver_build_name', db.String(150)),
    db.Column('search_id', db.String(14)),
    db.Column('lot_cd', db.String(6)),
    db.Column('deliver_start_date', db.DateTime),
    db.Column('deliver_end_date', db.DateTime),
    db.Column('deliver_status', db.String(2))
)


t_v_ex_goods_remainder = db.Table(
    'v_ex_goods_remainder',
    db.Column('ex_goods_remainder_seq', db.Integer),
    db.Column('contract_no', db.String(12)),
    db.Column('create_date', db.DateTime),
    db.Column('renew_date', db.DateTime),
    db.Column('operate_cd', db.String(128)),
    db.Column('installment_cd', db.String(3)),
    db.Column('order_no', db.String(16)),
    db.Column('start_month', db.Date),
    db.Column('end_plan_month', db.Date),
    db.Column('goods_cost', db.Numeric(8, 0)),
    db.Column('end_month', db.Date),
    db.Column('remaining_month', db.Date),
    db.Column('remaining_cost', db.Numeric(8, 0)),
    db.Column('demand_count', db.Numeric(2, 0)),
    db.Column('demand_cost', db.Numeric(8, 0))
)


t_v_ex_hbm_dat = db.Table(
    'v_ex_hbm_dat',
    db.Column('ex_hbm_dat_seq', db.Integer),
    db.Column('ws_common_id', db.String(20)),
    db.Column('ws_common_renbn', db.String(2)),
    db.Column('contract_no', db.String(12)),
    db.Column('opt_contract_no', db.Numeric(10, 0)),
    db.Column('isp_order_no', db.String(20)),
    db.Column('renew_date', db.DateTime),
    db.Column('create_date', db.DateTime),
    db.Column('operate_cd', db.String(128)),
    db.Column('c_flag', db.String(1)),
    db.Column('remark', db.String(80)),
    db.Column('apply_date', db.DateTime),
    db.Column('apply_kind', db.String(4)),
    db.Column('prog_status', db.String(2)),
    db.Column('send_plan_date', db.DateTime),
    db.Column('send_date', db.DateTime),
    db.Column('hbm_status', db.String(1)),
    db.Column('imei', db.String(15)),
    db.Column('iccid', db.String(19)),
    db.Column('msisdn', db.String(11)),
    db.Column('send_name', db.String(120)),
    db.Column('send_zip', db.String(7)),
    db.Column('send_todohuken', db.String(8)),
    db.Column('send_addr1', db.String(100)),
    db.Column('send_addr2', db.String(100)),
    db.Column('send_build_name', db.String(80)),
    db.Column('send_telno', db.String(11)),
    db.Column('arrival_plan_date', db.DateTime),
    db.Column('arrival_plan_time', db.String(1)),
    db.Column('ship_no', db.String(20)),
    db.Column('direct_date', db.DateTime),
    db.Column('ship_decision_date', db.DateTime),
    db.Column('ship_comp_date', db.DateTime),
    db.Column('send_status', db.String(2)),
    db.Column('item_cd', db.String(10)),
    db.Column('return_limit_date', db.DateTime),
    db.Column('return_flg', db.String(1)),
    db.Column('return_date', db.DateTime),
    db.Column('return_kit_reg_date', db.DateTime),
    db.Column('return_send_date', db.DateTime),
    db.Column('org_ws_common_id', db.String(20)),
    db.Column('sim_acct_stop_date', db.DateTime),
    db.Column('lost_opt_contract_no', db.Numeric(10, 0)),
    db.Column('user_name_k', db.String(100)),
    db.Column('user_sex', db.String(1)),
    db.Column('user_birth', db.DateTime),
    db.Column('device_cd', db.String(2)),
    db.Column('mnp_number', db.String(10)),
    db.Column('mnp_telno', db.String(11)),
    db.Column('mnp_expire_date', db.DateTime),
    db.Column('mnp_line_name', db.String(100)),
    db.Column('mnp_line_name_k', db.String(100)),
    db.Column('pt2_account_status', db.String(1)),
    db.Column('charge_date', db.DateTime),
    db.Column('portable_tel_flg', db.String(1)),
    db.Column('mnp_out_number', db.String(10)),
    db.Column('mnp_out_status', db.String(1)),
    db.Column('mnp_out_apply_date', db.DateTime),
    db.Column('mnp_out_order_date', db.DateTime),
    db.Column('mnp_out_order_comp_date', db.DateTime),
    db.Column('mnp_out_expire_date', db.DateTime),
    db.Column('mnp_out_end_date', db.DateTime),
    db.Column('mnp_out_line_lastname_k', db.String(80)),
    db.Column('mnp_out_line_firstname_k', db.String(40)),
    db.Column('mnp_out_line_lastname', db.String(40)),
    db.Column('mnp_out_line_firstname', db.String(20)),
    db.Column('mnp_out_line_birth', db.DateTime),
    db.Column('semiblack_add_status', db.String(1)),
    db.Column('semiblack_add_reserve_date', db.DateTime),
    db.Column('semiblack_add_apply_date', db.DateTime),
    db.Column('semiblack_add_comp_date', db.DateTime),
    db.Column('semiblack_add_error_msg', db.String(100)),
    db.Column('issue_error_msg', db.String(500)),
    db.Column('issue_touser_error_msg', db.String(500)),
    db.Column('notdelivered_date', db.DateTime),
    db.Column('tcard_issue', db.String(1)),
    db.Column('channel_flg', db.String(1)),
    db.Column('changevoice_flg', db.String(1)),
    db.Column('quota_carryover_date', db.DateTime),
    db.Column('pt2_flg', db.String(1)),
    db.Column('warranty_start_date', db.DateTime)
)


t_v_ex_icracked_cont = db.Table(
    'v_ex_icracked_cont',
    db.Column('ex_icracked_cont_seq', db.Integer),
    db.Column('imei', db.String(15)),
    db.Column('contract_no', db.String(12)),
    db.Column('opt_contract_no', db.Numeric(10, 0)),
    db.Column('imei_create_date', db.Date),
    db.Column('service_start_date', db.Date),
    db.Column('repair_date', db.Date),
    db.Column('repair_content', db.String(2)),
    db.Column('renew_date', db.DateTime),
    db.Column('create_date', db.DateTime),
    db.Column('operate_cd', db.String(128)),
    db.Column('c_flag', db.String(1)),
    db.Column('diff_flag', db.String(1)),
    db.Column('prog_status', db.String(2))
)


t_v_ex_installment_mst = db.Table(
    'v_ex_installment_mst',
    db.Column('ex_installment_mst_seq', db.Integer),
    db.Column('installment_cd', db.String(3)),
    db.Column('create_date', db.DateTime),
    db.Column('renew_date', db.DateTime),
    db.Column('operate_cd', db.String(128)),
    db.Column('plan_cd', db.String(8)),
    db.Column('split_count', db.Numeric(2, 0)),
    db.Column('first_cost', db.Numeric(8, 0)),
    db.Column('regular_cost', db.Numeric(8, 0)),
    db.Column('june_extra_cost', db.Numeric(8, 0)),
    db.Column('december_extra_cost', db.Numeric(8, 0))
)


t_v_ex_kddi_cont = db.Table(
    'v_ex_kddi_cont',
    db.Column('ex_kddi_cont_seq', db.Integer),
    db.Column('contract_no', db.String(12)),
    db.Column('kddi_mng_no', db.Numeric(10, 0)),
    db.Column('renew_date', db.DateTime),
    db.Column('create_date', db.DateTime),
    db.Column('operate_cd', db.String(128)),
    db.Column('c_flag', db.String(1)),
    db.Column('remark', db.String(80)),
    db.Column('kddi_cont_no', db.String(10)),
    db.Column('isp_order_no', db.String(20)),
    db.Column('kddi_create_date', db.DateTime),
    db.Column('line_plan_date', db.DateTime),
    db.Column('line_start_date', db.DateTime),
    db.Column('tel_pre_service_num', db.Numeric(1, 0)),
    db.Column('tel_service_num', db.Numeric(1, 0)),
    db.Column('tv_pre_service_num', db.Numeric(1, 0)),
    db.Column('tv_service_num', db.Numeric(1, 0)),
    db.Column('kddi_use_end_date', db.DateTime),
    db.Column('kddi_cont_end_date', db.DateTime),
    db.Column('service_kind', db.String(1)),
    db.Column('service_state_flg', db.String(1)),
    db.Column('design_comp_date', db.DateTime),
    db.Column('outside_comp_date', db.DateTime),
    db.Column('work_stay_reason', db.String(120)),
    db.Column('provide_date', db.DateTime),
    db.Column('provide_flg', db.String(1)),
    db.Column('provide_ng_reason', db.String(120)),
    db.Column('work_plan_date', db.DateTime),
    db.Column('work_end_date', db.DateTime),
    db.Column('counting_start_month', db.Date)
)


t_v_ex_kddi_cont_opt = db.Table(
    'v_ex_kddi_cont_opt',
    db.Column('ex_kddi_cont_opt_seq', db.Integer),
    db.Column('kddi_cont_no', db.String(10)),
    db.Column('service_cont_no', db.String(8)),
    db.Column('renew_date', db.DateTime),
    db.Column('create_date', db.DateTime),
    db.Column('operate_cd', db.String(128)),
    db.Column('c_flag', db.String(1)),
    db.Column('remark', db.String(80)),
    db.Column('service_kbn', db.String(1)),
    db.Column('telno', db.String(11)),
    db.Column('portable_flg', db.String(1)),
    db.Column('portable_prog_flg', db.String(1)),
    db.Column('kddi_apply_date', db.DateTime),
    db.Column('bill_start_date', db.DateTime),
    db.Column('use_end_date', db.DateTime),
    db.Column('cont_end_date', db.DateTime),
    db.Column('talkie_flg', db.String(1)),
    db.Column('talkie_no', db.String(11))
)


t_v_ex_kddi_dat = db.Table(
    'v_ex_kddi_dat',
    db.Column('ex_kddi_dat_seq', db.Integer),
    db.Column('kddi_mng_no', db.Numeric(10, 0)),
    db.Column('seq_no', db.Numeric(2, 0)),
    db.Column('renew_date', db.DateTime),
    db.Column('create_date', db.DateTime),
    db.Column('operate_cd', db.String(128)),
    db.Column('c_flag', db.String(1)),
    db.Column('remark', db.String(80)),
    db.Column('apply_date', db.DateTime),
    db.Column('service_kbn', db.String(1)),
    db.Column('apply_kind', db.String(4)),
    db.Column('prog_status', db.String(2)),
    db.Column('send_plan_date', db.DateTime),
    db.Column('send_date', db.DateTime),
    db.Column('cancel_plan_date', db.DateTime),
    db.Column('tel_no', db.String(11)),
    db.Column('ntt_return_kbn', db.String(1)),
    db.Column('tel_talkie_flg', db.String(1)),
    db.Column('tel_talkie_no', db.String(11))
)


t_v_ex_kddi_dmd = db.Table(
    'v_ex_kddi_dmd',
    db.Column('ex_kddi_dmd_seq', db.Integer),
    db.Column('kddi_mng_no', db.Numeric(10, 0)),
    db.Column('renew_date', db.DateTime),
    db.Column('create_date', db.DateTime),
    db.Column('operate_cd', db.String(128)),
    db.Column('c_flag', db.String(1)),
    db.Column('remark', db.String(80)),
    db.Column('kddi_dmd_shift_flg', db.String(1)),
    db.Column('kddi_dmd_kind', db.String(1)),
    db.Column('au_cont_telno', db.String(11)),
    db.Column('au_cont_birth', db.DateTime),
    db.Column('au_cont_name', db.String(60)),
    db.Column('au_cont_name_k', db.String(60)),
    db.Column('au_cont_sign_flg', db.String(1)),
    db.Column('auonenet_cont_cd', db.String(10)),
    db.Column('auonenet_cont_name', db.String(60)),
    db.Column('auonenet_cont_name_k', db.String(60)),
    db.Column('auonenet_sign_flg', db.String(1)),
    db.Column('kotei_telno', db.String(10)),
    db.Column('kotei_cont_name', db.String(60)),
    db.Column('kotei_cont_name_k', db.String(60)),
    db.Column('kotei_sign_flg', db.String(1)),
    db.Column('kddi_dmd_name', db.String(60)),
    db.Column('kddi_dmd_name_k', db.String(60)),
    db.Column('kddi_dmd_sign_flg', db.String(1)),
    db.Column('kddi_pay_name', db.String(60)),
    db.Column('kddi_pay_name_k', db.String(60)),
    db.Column('pay_sign_flg', db.String(1)),
    db.Column('pledge_name_flg', db.String(1)),
    db.Column('apply_sign_flg', db.String(1)),
    db.Column('apply_pledge_flg', db.String(1)),
    db.Column('paper_bill_flg', db.String(1)),
    db.Column('kddi_payment_kbn', db.String(1)),
    db.Column('kddi_payment_shift_kbn', db.String(1)),
    db.Column('myline_acount', db.String(10)),
    db.Column('kddi_email_apply_flag', db.String(1)),
    db.Column('auonenet_email', db.String(129)),
    db.Column('kddi_dmd_result_kbn', db.String(1)),
    db.Column('kddi_dmd_method', db.String(1)),
    db.Column('kddi_dmd_first_month', db.String(6)),
    db.Column('kddi_dmd_error_cd', db.String(4)),
    db.Column('kddi_dmd_error_msg', db.String(200)),
    db.Column('kddi_dmd_receipt_date', db.DateTime),
    db.Column('kddi_claim_cont_cd', db.String(1)),
    db.Column('kddi_claim_close_reserve_cd', db.String(1)),
    db.Column('servicestop_file_date', db.DateTime)
)


t_v_ex_kddi_info = db.Table(
    'v_ex_kddi_info',
    db.Column('ex_kddi_info_seq', db.Integer),
    db.Column('kddi_mng_no', db.Numeric(10, 0)),
    db.Column('renew_date', db.DateTime),
    db.Column('create_date', db.DateTime),
    db.Column('operate_cd', db.String(128)),
    db.Column('c_flag', db.String(1)),
    db.Column('remark', db.String(80)),
    db.Column('kddi_order_no', db.String(10)),
    db.Column('kddi_jit_bumon_cd', db.String(4)),
    db.Column('kddi_tyoku_kbn', db.String(1)),
    db.Column('kddi_agency_cd', db.String(10)),
    db.Column('cont_zip', db.String(7)),
    db.Column('cont_todohuken', db.String(8)),
    db.Column('cont_shiku', db.String(60)),
    db.Column('cont_area_chome_banchi', db.String(60)),
    db.Column('cont_build_name', db.String(100)),
    db.Column('cont_telno1', db.String(11)),
    db.Column('cont_telno2', db.String(11)),
    db.Column('email', db.String(129)),
    db.Column('est_place_flg', db.String(1)),
    db.Column('est_zip', db.String(7)),
    db.Column('est_todohuken', db.String(8)),
    db.Column('est_shiku', db.String(60)),
    db.Column('est_area_chome_banchi', db.String(60)),
    db.Column('est_build_name', db.String(100)),
    db.Column('dest_place_flg', db.String(1)),
    db.Column('dest_name', db.String(60)),
    db.Column('dest_name_k', db.String(60)),
    db.Column('dest_zip', db.String(7)),
    db.Column('dest_todohuken', db.String(8)),
    db.Column('dest_shiku', db.String(60)),
    db.Column('dest_area_chome_banchi', db.String(60)),
    db.Column('dest_build_name', db.String(100)),
    db.Column('dest_telno', db.String(11)),
    db.Column('cont_group_no', db.String(10)),
    db.Column('article_no', db.String(8)),
    db.Column('ridge_id', db.String(2)),
    db.Column('room_no', db.String(5)),
    db.Column('modular_board_num', db.String(1)),
    db.Column('line1_no', db.String(11)),
    db.Column('line1_status', db.String(1)),
    db.Column('line2_no', db.String(11)),
    db.Column('line2_status', db.String(1)),
    db.Column('taxfree_user_cd', db.String(1)),
    db.Column('hikari_plus_tel_flg', db.String(1)),
    db.Column('portable_tel_flg', db.String(1)),
    db.Column('telno_050_flg', db.String(1)),
    db.Column('portable_tel', db.String(11)),
    db.Column('ntt_name', db.String(60)),
    db.Column('ntt_name_k', db.String(60)),
    db.Column('interrupt_call_flg', db.String(1)),
    db.Column('caller_id_display_flg', db.String(1)),
    db.Column('notice_telno_flg', db.String(1)),
    db.Column('nuisance_call_repulse_flg', db.String(1)),
    db.Column('caller_id_notice_flg', db.String(1)),
    db.Column('caller_id_notice_cd', db.String(1)),
    db.Column('detail_output_flg', db.String(1)),
    db.Column('number_guidance_flg', db.String(1)),
    db.Column('hellopage_flg', db.String(1)),
    db.Column('hikari_plus_tv_flg', db.String(1)),
    db.Column('stb_cd', db.String(4)),
    db.Column('filter_flg', db.String(1)),
    db.Column('filter_cd', db.String(4)),
    db.Column('kaketuke_support_flg', db.String(1)),
    db.Column('campain_apply_date', db.DateTime),
    db.Column('interrupt_number_flg', db.String(1)),
    db.Column('arrival_plan_date', db.DateTime),
    db.Column('dest_addr_change_flg', db.String(1)),
    db.Column('musen_lan_rental_cd', db.String(4)),
    db.Column('musen_lan_rental_num', db.String(2)),
    db.Column('add_hgw_cd', db.String(4)),
    db.Column('add_hgw_num', db.String(2)),
    db.Column('add_stb_cd', db.String(4)),
    db.Column('add_stb_num', db.String(2)),
    db.Column('entering_plan_date', db.DateTime),
    db.Column('redirect_call_flg', db.String(1)),
    db.Column('house_cd', db.String(1)),
    db.Column('possession_cd', db.String(1)),
    db.Column('isp_cd', db.String(3)),
    db.Column('incoming_notice_flg', db.String(1)),
    db.Column('au_term_telno1', db.String(11)),
    db.Column('au_term_telno2', db.String(11)),
    db.Column('au_term_telno3', db.String(11)),
    db.Column('ntt_line_cd', db.String(2)),
    db.Column('kddi_memo', db.String(16)),
    db.Column('same_0abj_telno', db.String(11)),
    db.Column('exist_line_flg', db.String(1)),
    db.Column('important_notice', db.String(100)),
    db.Column('ntt_zip', db.String(7)),
    db.Column('ntt_todohuken', db.String(8)),
    db.Column('ntt_shiku', db.String(60)),
    db.Column('ntt_area_chome_banchi', db.String(60)),
    db.Column('ntt_build_name', db.String(100)),
    db.Column('speed_kbn', db.String(1)),
    db.Column('musen_lan_rental_cd2', db.String(4)),
    db.Column('musen_lan_rental_num2', db.String(2)),
    db.Column('musen_lan_rental_cd3', db.String(4)),
    db.Column('musen_lan_rental_num3', db.String(2)),
    db.Column('musen_lan_rental_cd4', db.String(4)),
    db.Column('musen_lan_rental_num4', db.String(2)),
    db.Column('musen_lan_rental_cd5', db.String(4)),
    db.Column('musen_lan_rental_num5', db.String(2)),
    db.Column('work_date_id', db.String(10)),
    db.Column('monthly_item01', db.String(4)),
    db.Column('monthly_item02', db.String(4)),
    db.Column('monthly_item03', db.String(4)),
    db.Column('monthly_item04', db.String(4)),
    db.Column('monthly_item05', db.String(4)),
    db.Column('monthly_item06', db.String(4)),
    db.Column('monthly_item07', db.String(4)),
    db.Column('monthly_item08', db.String(4)),
    db.Column('monthly_item09', db.String(4)),
    db.Column('monthly_item10', db.String(4)),
    db.Column('monthly_item11', db.String(4)),
    db.Column('monthly_item12', db.String(4)),
    db.Column('pre_voip_co_cd', db.String(4)),
    db.Column('pre_voip_co_cd2', db.String(4)),
    db.Column('est_floors', db.String(3)),
    db.Column('cont_room_no', db.String(40)),
    db.Column('owner_name', db.String(60)),
    db.Column('owner_address', db.String(100)),
    db.Column('owner_telno', db.String(11)),
    db.Column('owner_kbn', db.String(1)),
    db.Column('est_telno', db.String(11)),
    db.Column('kddi3m_au_smart_val_cd', db.String(15)),
    db.Column('kddi3m_multi_campaign_kbn', db.String(1)),
    db.Column('kddi3m_campaign_flg', db.String(1)),
    db.Column('kddi3m_applyprint_no', db.String(9))
)


t_v_ex_lf_cont = db.Table(
    'v_ex_lf_cont',
    db.Column('ex_lf_cont_seq', db.Integer),
    db.Column('contract_no', db.String(12)),
    db.Column('opt_contract_no', db.Numeric(10, 0)),
    db.Column('isp_user_id', db.String(20)),
    db.Column('renew_date', db.DateTime),
    db.Column('create_date', db.DateTime),
    db.Column('operate_cd', db.String(128)),
    db.Column('remark', db.String(80)),
    db.Column('unext_id', db.String(10)),
    db.Column('license_key1', db.String(50)),
    db.Column('license_key2', db.String(50)),
    db.Column('license_key3', db.String(50)),
    db.Column('license_key4', db.String(50)),
    db.Column('license_key5', db.String(50)),
    db.Column('license_key6', db.String(50)),
    db.Column('license_key7', db.String(50)),
    db.Column('apply_request_date', db.Date),
    db.Column('apply_process_date', db.Date),
    db.Column('end_request_date', db.Date),
    db.Column('end_process_date', db.Date)
)


t_v_ex_lf_dat = db.Table(
    'v_ex_lf_dat',
    db.Column('ex_lf_dat_seq', db.Integer),
    db.Column('ws_common_id', db.String(20)),
    db.Column('ws_common_renbn', db.String(2)),
    db.Column('contract_no', db.String(12)),
    db.Column('create_date', db.DateTime),
    db.Column('renew_date', db.DateTime),
    db.Column('operate_cd', db.String(128)),
    db.Column('remark', db.String(80)),
    db.Column('apply_kind', db.String(4)),
    db.Column('prog_status', db.String(2)),
    db.Column('apply_date', db.DateTime),
    db.Column('send_plan_date', db.DateTime),
    db.Column('send_date', db.DateTime),
    db.Column('opt_contract_no', db.Numeric(10, 0)),
    db.Column('firstname', db.String(20)),
    db.Column('firstname_k', db.String(20)),
    db.Column('lastname', db.String(50)),
    db.Column('lastname_k', db.String(100)),
    db.Column('lf_sex', db.String(1)),
    db.Column('lf_birth', db.DateTime),
    db.Column('lf_telno', db.String(20)),
    db.Column('lf_mobile', db.String(20)),
    db.Column('lf_zip', db.String(7)),
    db.Column('lf_todohuken', db.String(4)),
    db.Column('lf_shiku_area_chome', db.String(50)),
    db.Column('lf_banchi', db.String(50)),
    db.Column('lf_build_name', db.String(40)),
    db.Column('lf_email', db.String(128)),
    db.Column('plan_type', db.String(1))
)


t_v_ex_lte_dat = db.Table(
    'v_ex_lte_dat',
    db.Column('ex_lte_dat_seq', db.Integer),
    db.Column('ws_common_id', db.String(20)),
    db.Column('ws_common_renbn', db.String(2)),
    db.Column('contract_no', db.String(12)),
    db.Column('opt_contract_no', db.Numeric(10, 0)),
    db.Column('renew_date', db.DateTime),
    db.Column('create_date', db.DateTime),
    db.Column('operate_cd', db.String(128)),
    db.Column('c_flag', db.String(1)),
    db.Column('remark', db.String(80)),
    db.Column('apply_date', db.DateTime),
    db.Column('apply_kind', db.String(4)),
    db.Column('prog_status', db.String(2)),
    db.Column('send_plan_date', db.DateTime),
    db.Column('send_date', db.DateTime),
    db.Column('lte_user_id', db.String(10)),
    db.Column('imei', db.String(15)),
    db.Column('iccid', db.String(19)),
    db.Column('msisdn', db.String(11)),
    db.Column('lte_machin_meker', db.String(50)),
    db.Column('lte_machin_model', db.String(50)),
    db.Column('send_name', db.String(100)),
    db.Column('send_name_kana', db.String(100)),
    db.Column('send_zip', db.String(7)),
    db.Column('send_todohuken', db.String(8)),
    db.Column('send_addr1', db.String(40)),
    db.Column('send_addr2', db.String(50)),
    db.Column('send_addr3', db.String(50)),
    db.Column('send_addr4', db.String(40)),
    db.Column('send_build_name', db.String(80)),
    db.Column('send_telno', db.String(13)),
    db.Column('arrival_plan_date', db.DateTime),
    db.Column('arrival_plan_time', db.String(1)),
    db.Column('ship_no', db.String(20)),
    db.Column('direct_date', db.DateTime),
    db.Column('ship_plan_date', db.DateTime),
    db.Column('ship_decision_date', db.DateTime),
    db.Column('ship_comp_date', db.DateTime),
    db.Column('id_renbn', db.Numeric(2, 0))
)


t_v_ex_mopita_info = db.Table(
    'v_ex_mopita_info',
    db.Column('ex_mopita_info_seq', db.Integer),
    db.Column('contbase_no', db.String(10)),
    db.Column('mopita_acct_id', db.String(12)),
    db.Column('mopita_status', db.String(2)),
    db.Column('mopita_pwd', db.String(7)),
    db.Column('mopita_reg_date', db.DateTime),
    db.Column('mopita_user_id', db.String(32)),
    db.Column('mopita_end_date', db.DateTime),
    db.Column('create_date', db.DateTime),
    db.Column('renew_date', db.DateTime),
    db.Column('operate_cd', db.String(128)),
    db.Column('c_flag', db.String(1)),
    db.Column('mti_pin_cd', db.String(12))
)


t_v_ex_necat_dat = db.Table(
    'v_ex_necat_dat',
    db.Column('ex_necat_dat_seq', db.Integer),
    db.Column('ws_common_id', db.String(20)),
    db.Column('ws_common_renbn', db.String(2)),
    db.Column('contract_no', db.String(12)),
    db.Column('opt_contract_no', db.Numeric(10, 0)),
    db.Column('isp_order_no', db.String(14)),
    db.Column('status', db.String(1)),
    db.Column('apply_kind', db.String(4)),
    db.Column('syori_status', db.String(2)),
    db.Column('syohin_cd', db.String(20)),
    db.Column('product_no', db.String(20)),
    db.Column('mac_address', db.String(12)),
    db.Column('invoice_no', db.String(20)),
    db.Column('plan_cd', db.String(10)),
    db.Column('zip', db.String(8)),
    db.Column('addr1', db.String(4)),
    db.Column('addr2', db.String(50)),
    db.Column('addr3', db.String(50)),
    db.Column('apply_date', db.DateTime),
    db.Column('send_plan_date', db.DateTime),
    db.Column('send_date', db.DateTime),
    db.Column('arrival_plan_date', db.DateTime),
    db.Column('arrival_plan_time', db.String(2)),
    db.Column('ship_date', db.DateTime),
    db.Column('arrival_date', db.DateTime),
    db.Column('arv_info_recv_date', db.DateTime),
    db.Column('arv_info_no', db.Numeric(2, 0)),
    db.Column('arv_ng_cd', db.String(2)),
    db.Column('cont_start_date', db.DateTime),
    db.Column('cont_end_date', db.DateTime),
    db.Column('iad_customer_id', db.String(30)),
    db.Column('create_date', db.DateTime),
    db.Column('renew_date', db.DateTime),
    db.Column('operate_cd', db.String(128)),
    db.Column('c_flag', db.String(1)),
    db.Column('remark', db.String(80))
)


t_v_ex_nicos_carddb = db.Table(
    'v_ex_nicos_carddb',
    db.Column('ex_nicos_carddb_seq', db.Integer),
    db.Column('card_mng_no', db.String(12)),
    db.Column('recurring_id', db.String(15)),
    db.Column('card_status', db.String(2)),
    db.Column('cardno', db.String(16)),
    db.Column('cardvalid', db.String(6)),
    db.Column('result_cd', db.String(3)),
    db.Column('create_date', db.DateTime),
    db.Column('renew_date', db.DateTime),
    db.Column('operate_cd', db.String(128))
)


t_v_ex_ntt_cor_add_cont = db.Table(
    'v_ex_ntt_cor_add_cont',
    db.Column('ex_ntt_cor_add_cont_seq', db.Integer),
    db.Column('contract_code', db.String(13)),
    db.Column('add_contract_code', db.String(13)),
    db.Column('opt_contract_no', db.Numeric(10, 0)),
    db.Column('ntt_ew_kind', db.String(1)),
    db.Column('renew_date', db.DateTime),
    db.Column('create_date', db.DateTime),
    db.Column('operate_cd', db.String(128)),
    db.Column('c_flag', db.String(1)),
    db.Column('service_kind', db.String(1)),
    db.Column('service_name', db.String(90)),
    db.Column('order_class', db.String(4)),
    db.Column('order_status', db.String(2)),
    db.Column('application_pername', db.String(90)),
    db.Column('contact_phone', db.String(90)),
    db.Column('applied_date', db.DateTime),
    db.Column('appoint_date', db.DateTime),
    db.Column('change_date', db.DateTime),
    db.Column('serv_start_day', db.DateTime),
    db.Column('serv_end_day', db.DateTime),
    db.Column('plan_name', db.String(128)),
    db.Column('operator_ent_name', db.String(40)),
    db.Column('operator_cor_branch_name', db.String(70)),
    db.Column('operator_cor_section_name', db.String(70)),
    db.Column('operator_cor_charge_name', db.String(128)),
    db.Column('operator_cor_phone', db.String(13)),
    db.Column('operator_cor_fax', db.String(13)),
    db.Column('sales_ent_name', db.String(40)),
    db.Column('sales_cor_branch_name', db.String(70)),
    db.Column('sales_cor_section_name', db.String(70)),
    db.Column('sales_cor_chargen_ame', db.String(128)),
    db.Column('sales_cor_phone', db.String(13)),
    db.Column('sales_cor_fax', db.String(13)),
    db.Column('date_renewed', db.DateTime),
    db.Column('add_phone_no', db.String(13)),
    db.Column('service_code', db.String(8)),
    db.Column('add_phone_kbn', db.String(1))
)


t_v_ex_ntt_cor_add_dat = db.Table(
    'v_ex_ntt_cor_add_dat',
    db.Column('ex_ntt_cor_add_dat_seq', db.Integer),
    db.Column('ws_common_id', db.String(20)),
    db.Column('ws_common_renbn', db.String(2)),
    db.Column('contract_code', db.String(13)),
    db.Column('add_contract_code', db.String(13)),
    db.Column('create_date', db.DateTime),
    db.Column('renew_date', db.DateTime),
    db.Column('operate_cd', db.String(128)),
    db.Column('c_flag', db.String(1)),
    db.Column('remark', db.String(80)),
    db.Column('apply_kind', db.String(4)),
    db.Column('prog_status', db.String(2)),
    db.Column('apply_date', db.DateTime),
    db.Column('send_plan_date', db.DateTime),
    db.Column('send_date', db.DateTime),
    db.Column('service_kbn', db.String(1)),
    db.Column('service_code', db.String(8)),
    db.Column('telno', db.String(13)),
    db.Column('opt_contract_no', db.Numeric(10, 0))
)


t_v_ex_ntt_cor_charge_dat = db.Table(
    'v_ex_ntt_cor_charge_dat',
    db.Column('ex_ntt_cor_charge_dat_seq', db.Integer),
    db.Column('contract_no', db.String(12)),
    db.Column('renbn', db.String(3)),
    db.Column('rating_name', db.String(64)),
    db.Column('price', db.Numeric(14, 4)),
    db.Column('count', db.Numeric(10, 0)),
    db.Column('renew_date', db.DateTime),
    db.Column('create_date', db.DateTime),
    db.Column('operate_cd', db.String(128)),
    db.Column('c_flag', db.String(1))
)


t_v_ex_ntt_cor_cont = db.Table(
    'v_ex_ntt_cor_cont',
    db.Column('ex_ntt_cor_cont_seq', db.Integer),
    db.Column('contract_no', db.String(12)),
    db.Column('isp_order_no', db.String(20)),
    db.Column('renew_date', db.DateTime),
    db.Column('create_date', db.DateTime),
    db.Column('operate_cd', db.String(128)),
    db.Column('c_flag', db.String(1)),
    db.Column('business_name', db.String(3)),
    db.Column('contract_code', db.String(13)),
    db.Column('divert_consent_no', db.String(11)),
    db.Column('partner_code', db.String(18)),
    db.Column('service_name', db.String(50)),
    db.Column('service_item', db.String(256)),
    db.Column('so', db.String(4)),
    db.Column('so_stat', db.String(2)),
    db.Column('contractor_name', db.String(128)),
    db.Column('contractor_kname', db.String(256)),
    db.Column('cur_user_addr_code', db.String(802)),
    db.Column('applicationper_name', db.String(128)),
    db.Column('contact_phone', db.String(13)),
    db.Column('applied_date', db.DateTime),
    db.Column('appoint_date', db.DateTime),
    db.Column('change_date', db.DateTime),
    db.Column('business_contract_start_date', db.DateTime),
    db.Column('contract_end_date', db.DateTime),
    db.Column('flets_contract_start_date', db.DateTime),
    db.Column('ftv_trans_business_name', db.String(3)),
    db.Column('indoor_stem_wiring_div', db.String(64)),
    db.Column('ftv_business_cont_start_date', db.DateTime),
    db.Column('ftv_business_cont_end_date', db.DateTime),
    db.Column('regular_charge_div', db.String(8)),
    db.Column('service_change_code', db.String(13)),
    db.Column('operator_ent_name', db.String(40)),
    db.Column('operator_cor_branch_name', db.String(70)),
    db.Column('operator_cor_section_name', db.String(70)),
    db.Column('operator_cor_charge_name', db.String(128)),
    db.Column('operator_cor_phone', db.String(13)),
    db.Column('operator_cor_fax', db.String(13)),
    db.Column('sales_ent_name', db.String(40)),
    db.Column('sales_cor_branch_name', db.String(70)),
    db.Column('sales_cor_section_name', db.String(70)),
    db.Column('sales_cor_chargen_ame', db.String(80)),
    db.Column('sales_cor_phone', db.String(13)),
    db.Column('sales_cor_fax', db.String(12)),
    db.Column('accident_reason', db.String(256)),
    db.Column('accident_reason_sub', db.String(48)),
    db.Column('date_renewed', db.DateTime),
    db.Column('ritei_status', db.String(50)),
    db.Column('ritei_start_date', db.DateTime),
    db.Column('order_no', db.String(18)),
    db.Column('arena_so_no', db.String(20)),
    db.Column('access_key', db.String(8)),
    db.Column('survery_appoint_date', db.DateTime),
    db.Column('survery_appoint_time', db.String(256)),
    db.Column('appoint_am_pm', db.String(256)),
    db.Column('dispatch_div', db.String(256)),
    db.Column('aldivert_flg', db.String(1)),
    db.Column('vcast_business_name', db.String(30)),
    db.Column('ftvdivertflg', db.String(1)),
    db.Column('repflg', db.String(1)),
    db.Column('repbusinessname', db.String(3)),
    db.Column('repdivertflg', db.String(1)),
    db.Column('repbusinessstartdate', db.DateTime),
    db.Column('repbusinessenddate', db.DateTime),
    db.Column('terminal_item_list', db.Text),
    db.Column('charge_list', db.Text),
    db.Column('contact_hope_time_kbn', db.String(2))
)


t_v_ex_ntt_cor_dat = db.Table(
    'v_ex_ntt_cor_dat',
    db.Column('ex_ntt_cor_dat_seq', db.Integer),
    db.Column('ws_common_id', db.String(20)),
    db.Column('ws_common_renbn', db.String(2)),
    db.Column('contract_no', db.String(12)),
    db.Column('renew_date', db.DateTime),
    db.Column('create_date', db.DateTime),
    db.Column('operate_cd', db.String(128)),
    db.Column('c_flag', db.String(1)),
    db.Column('remark', db.String(80)),
    db.Column('apply_date', db.DateTime),
    db.Column('apply_kind', db.String(4)),
    db.Column('prog_status', db.String(2)),
    db.Column('send_plan_date', db.DateTime),
    db.Column('send_date', db.DateTime),
    db.Column('service_item', db.String(256)),
    db.Column('user_zip', db.String(7)),
    db.Column('user_addr', db.String(802)),
    db.Column('iten_plan_date', db.DateTime)
)


t_v_ex_ntt_cor_tmn_dat = db.Table(
    'v_ex_ntt_cor_tmn_dat',
    db.Column('ex_ntt_cor_tmn_dat_seq', db.Integer),
    db.Column('contract_no', db.String(12)),
    db.Column('renbn', db.String(3)),
    db.Column('terminal_name', db.String(128)),
    db.Column('install_date', db.DateTime),
    db.Column('renew_date', db.DateTime),
    db.Column('create_date', db.DateTime),
    db.Column('operate_cd', db.String(128)),
    db.Column('c_flag', db.String(1))
)


t_v_ex_ntt_dat = db.Table(
    'v_ex_ntt_dat',
    db.Column('ex_ntt_dat_seq', db.Integer),
    db.Column('ws_common_id', db.String(20)),
    db.Column('ws_common_renbn', db.String(2)),
    db.Column('contract_no', db.String(12)),
    db.Column('renew_date', db.DateTime),
    db.Column('create_date', db.DateTime),
    db.Column('operate_cd', db.String(128)),
    db.Column('c_flag', db.String(1)),
    db.Column('remark', db.String(80)),
    db.Column('apply_date', db.DateTime),
    db.Column('apply_kind', db.String(4)),
    db.Column('prog_status', db.String(2)),
    db.Column('send_plan_date', db.DateTime),
    db.Column('send_date', db.DateTime),
    db.Column('request_id', db.String(10)),
    db.Column('est_todohuken', db.String(20)),
    db.Column('apply_name', db.String(128)),
    db.Column('operator_name', db.String(128)),
    db.Column('work_plan_date', db.DateTime),
    db.Column('ntt_plan_date', db.DateTime),
    db.Column('ntt_plan_time', db.String(2)),
    db.Column('user_tel1', db.String(13)),
    db.Column('user_tel2', db.String(13)),
    db.Column('user_name', db.String(128)),
    db.Column('relation', db.String(20)),
    db.Column('origin_cd', db.String(2)),
    db.Column('note', db.String(256)),
    db.Column('cancel_flg', db.String(1)),
    db.Column('osm_end_plan_date', db.DateTime),
    db.Column('note2', db.String(16)),
    db.Column('result_cd', db.String(64)),
    db.Column('note3', db.String(256))
)


t_v_ex_ntt_info = db.Table(
    'v_ex_ntt_info',
    db.Column('ex_ntt_info_seq', db.Integer),
    db.Column('contract_no', db.String(12)),
    db.Column('renew_date', db.DateTime),
    db.Column('create_date', db.DateTime),
    db.Column('operate_cd', db.String(128)),
    db.Column('c_flag', db.String(1)),
    db.Column('remark', db.String(80)),
    db.Column('entry_root_cd', db.String(1)),
    db.Column('method_cd', db.String(3)),
    db.Column('tran_mng_no', db.String(16)),
    db.Column('work_plan_date', db.DateTime),
    db.Column('work_plan_time', db.String(2)),
    db.Column('consal_plan_date', db.DateTime),
    db.Column('work_date_flg', db.String(1)),
    db.Column('telno', db.String(10)),
    db.Column('ntt_e_cont_id', db.String(16)),
    db.Column('cont_lastname', db.String(20)),
    db.Column('cont_firstname', db.String(20)),
    db.Column('cont_lastname_k', db.String(20)),
    db.Column('cont_firstname_k', db.String(20)),
    db.Column('apply_name', db.String(128)),
    db.Column('apply_name_k', db.String(256)),
    db.Column('apply_cd', db.String(1)),
    db.Column('contact_cd', db.String(1)),
    db.Column('telno2', db.String(11)),
    db.Column('email', db.String(50)),
    db.Column('a_cd', db.String(1)),
    db.Column('b_cd', db.String(1)),
    db.Column('c_cd', db.String(1)),
    db.Column('d_cd', db.String(1)),
    db.Column('note2', db.String(400)),
    db.Column('partner_cd', db.String(10)),
    db.Column('corp_name', db.String(60)),
    db.Column('corp_kana', db.String(60)),
    db.Column('corp_post_name', db.String(60)),
    db.Column('user_zip', db.String(7)),
    db.Column('user_todohuken', db.String(256)),
    db.Column('user_ku', db.String(256)),
    db.Column('user_area', db.String(256)),
    db.Column('user_chome', db.String(256)),
    db.Column('user_banchi', db.String(160)),
    db.Column('user_build_name', db.String(80)),
    db.Column('user_addr_note', db.String(200)),
    db.Column('send_zip', db.String(7)),
    db.Column('send_todohuken', db.String(256)),
    db.Column('send_ku', db.String(256)),
    db.Column('send_area', db.String(256)),
    db.Column('send_chome', db.String(256)),
    db.Column('send_banchi', db.String(160)),
    db.Column('send_build_name', db.String(80)),
    db.Column('send_addr_note', db.String(200)),
    db.Column('send_name', db.String(128)),
    db.Column('send_name_k', db.String(256)),
    db.Column('send_person', db.String(128)),
    db.Column('ntt_branch_name', db.String(64)),
    db.Column('ntt_position_name', db.String(128)),
    db.Column('ntt_sales_agency_cd', db.String(8)),
    db.Column('ntt_charge_name', db.String(128)),
    db.Column('ntt_charge_cd', db.String(8)),
    db.Column('ntt_charge_telno', db.String(13)),
    db.Column('ntt_charge_fax', db.String(13)),
    db.Column('ntt_charge_mail', db.String(60)),
    db.Column('ntt_isp_apply_kbn', db.String(20)),
    db.Column('ntt_service_name', db.String(64)),
    db.Column('ntt_bf_exist_type', db.String(4)),
    db.Column('ntt_isp_user_id', db.String(60)),
    db.Column('ntt_isp_mail', db.String(60)),
    db.Column('banpo_flg', db.String(1)),
    db.Column('double_contract_flag', db.String(64)),
    db.Column('name_admin_flag', db.String(64)),
    db.Column('cont_address_code', db.String(15)),
    db.Column('cont_address_revision', db.String(10)),
    db.Column('fax', db.String(13)),
    db.Column('address_code', db.String(11)),
    db.Column('partner_serial_no', db.String(16)),
    db.Column('user_banchi1', db.String(40)),
    db.Column('user_banchi2', db.String(20)),
    db.Column('user_banchi3', db.String(20)),
    db.Column('work_witness_name', db.String(20)),
    db.Column('work_witness_contact_cd', db.String(1)),
    db.Column('work_witness_telno', db.String(11)),
    db.Column('use_access_line', db.String(1)),
    db.Column('use_ntt_flets_service', db.String(3)),
    db.Column('other_companies_contract', db.String(1)),
    db.Column('other_companies_service', db.String(1)),
    db.Column('interior_wiring_cd', db.String(1)),
    db.Column('wiring_work_cd', db.String(1)),
    db.Column('tel_directory_carry_cd', db.String(1)),
    db.Column('vcast_contractor_sex_type', db.String(1)),
    db.Column('vcast_contractor_birth', db.DateTime),
    db.Column('connect_tv_const', db.String(1)),
    db.Column('tv_set_construct_type', db.String(1)),
    db.Column('cs_channel_pack1', db.String(1)),
    db.Column('cs_digital_tuner1', db.String(1)),
    db.Column('cs_channel_pack2', db.String(1)),
    db.Column('cs_digital_tuner2', db.String(1)),
    db.Column('cs_channel_pack3', db.String(1)),
    db.Column('cs_digital_tuner3', db.String(1)),
    db.Column('possession_cd', db.String(1)),
    db.Column('number_of_house', db.String(1)),
    db.Column('house_cd', db.String(1)),
    db.Column('work_witness_cd', db.String(1)),
    db.Column('ipv6connectmethod', db.String(64)),
    db.Column('adapterinfo', db.String(64)),
    db.Column('fm_possession_cd', db.String(1)),
    db.Column('ntt_birth', db.DateTime),
    db.Column('ntt_sex_type', db.String(1))
)


t_v_ex_ntt_item_dat = db.Table(
    'v_ex_ntt_item_dat',
    db.Column('ex_ntt_item_dat_seq', db.Integer),
    db.Column('contract_no', db.String(12)),
    db.Column('item_no', db.String(2)),
    db.Column('renew_date', db.DateTime),
    db.Column('create_date', db.DateTime),
    db.Column('operate_cd', db.String(128)),
    db.Column('c_flag', db.String(1)),
    db.Column('apply_flg', db.String(1))
)


t_v_ex_ntt_osmdb = db.Table(
    'v_ex_ntt_osmdb',
    db.Column('ex_ntt_osmdb_seq', db.Integer),
    db.Column('contract_no', db.String(12)),
    db.Column('isp_order_no', db.String(16)),
    db.Column('renew_date', db.DateTime),
    db.Column('create_date', db.DateTime),
    db.Column('operate_cd', db.String(128)),
    db.Column('c_flag', db.String(1)),
    db.Column('ntt_e_cont_id', db.String(16)),
    db.Column('apply_name', db.String(128)),
    db.Column('telno', db.String(14)),
    db.Column('osm_apply_date', db.DateTime),
    db.Column('item_name', db.String(128)),
    db.Column('item_detail_name', db.String(32)),
    db.Column('item_term_name', db.String(50)),
    db.Column('work_plan_date', db.DateTime),
    db.Column('work_plan_time', db.String(40)),
    db.Column('osm_entry_cd', db.String(10)),
    db.Column('osm_status', db.String(5)),
    db.Column('osm_sub_status', db.String(5)),
    db.Column('osm_start_date', db.DateTime),
    db.Column('osm_end_yyyymm', db.DateTime),
    db.Column('branch_name', db.String(20)),
    db.Column('mainte_plan', db.String(16)),
    db.Column('model_name', db.String(512)),
    db.Column('model_num', db.String(128)),
    db.Column('partner_cd', db.String(10)),
    db.Column('osm_create_date', db.DateTime),
    db.Column('branch_telno', db.String(14)),
    db.Column('consal_plan_date', db.DateTime),
    db.Column('ntt_e_agency_cd', db.String(8)),
    db.Column('sales_store_name', db.String(128)),
    db.Column('section_name', db.String(128)),
    db.Column('charge_cd', db.String(8)),
    db.Column('charge_name', db.String(128)),
    db.Column('osm_renew_date', db.DateTime),
    db.Column('change_item_name', db.String(128)),
    db.Column('application_no', db.String(16)),
    db.Column('ntt_e_cont_start_date', db.DateTime),
    db.Column('outside_bill_start_date', db.DateTime),
    db.Column('inside_bill_start_date', db.DateTime),
    db.Column('outside_work_plan_date', db.DateTime),
    db.Column('inside_work_plan_date', db.DateTime),
    db.Column('accident_reason', db.String(256)),
    db.Column('accident_status', db.String(256)),
    db.Column('cancel_reason', db.String(256)),
    db.Column('mainte_info', db.String(128)),
    db.Column('campaign', db.String(64)),
    db.Column('bill_end_date', db.DateTime),
    db.Column('end_reason', db.String(256)),
    db.Column('osa_set_cd', db.String(2)),
    db.Column('osa_cancel_cd', db.String(256)),
    db.Column('change_item_detail_name', db.String(32)),
    db.Column('change_id_no', db.String(64)),
    db.Column('hgw_mainte_info', db.String(32)),
    db.Column('hgw_model_name', db.String(128)),
    db.Column('item_change_bill_date', db.DateTime),
    db.Column('mng_id', db.String(25)),
    db.Column('cp_start_date', db.DateTime),
    db.Column('cp_end_date', db.DateTime),
    db.Column('bill_start_date', db.DateTime),
    db.Column('consal_status', db.String(50)),
    db.Column('osm_flg', db.String(1)),
    db.Column('osm2_start_date', db.DateTime),
    db.Column('osm2_end_yyyymm', db.DateTime)
)


t_v_ex_nttplayer_cont = db.Table(
    'v_ex_nttplayer_cont',
    db.Column('ex_nttplayer_cont_seq', db.Integer),
    db.Column('contract_no', db.String(12)),
    db.Column('isp_order_no', db.String(20)),
    db.Column('renew_date', db.DateTime),
    db.Column('create_date', db.DateTime),
    db.Column('operate_cd', db.String(128)),
    db.Column('c_flag', db.String(1)),
    db.Column('service_name', db.String(40)),
    db.Column('item_name', db.String(128)),
    db.Column('order_status', db.String(40)),
    db.Column('work_plan_date', db.DateTime),
    db.Column('ntt_e_cont_id_pr', db.String(13)),
    db.Column('item_term_name', db.String(1536)),
    db.Column('apply_kbn', db.String(40)),
    db.Column('ntt_e_cont_id', db.String(13)),
    db.Column('divert_consent_no', db.String(11)),
    db.Column('ntt_ew_kind', db.String(40)),
    db.Column('nttplayer_cont_id', db.String(12)),
    db.Column('user_name', db.String(240)),
    db.Column('user_name_k', db.String(480)),
    db.Column('user_address', db.String(2142)),
    db.Column('isp_name', db.String(60)),
    db.Column('isp_status', db.String(2)),
    db.Column('nttplayer_start_end_date', db.DateTime),
    db.Column('isp_start_end_date', db.DateTime),
    db.Column('nttplayer_cont_name', db.String(60)),
    db.Column('nttplayer_cont_name_k', db.String(100)),
    db.Column('nttplayer_cont_telno', db.String(72)),
    db.Column('nttplayer_cont_telno2', db.String(11)),
    db.Column('nttplayer_cont_zip', db.String(7)),
    db.Column('nttplayer_cont_address', db.String(200)),
    db.Column('nttplayer_cont_birth', db.DateTime),
    db.Column('penalty_cost_flag', db.String(2)),
    db.Column('flets_cont_name', db.String(480)),
    db.Column('flets_cont_telno', db.String(72))
)


t_v_ex_nttplayer_dat = db.Table(
    'v_ex_nttplayer_dat',
    db.Column('ex_nttplayer_dat_seq', db.Integer),
    db.Column('ws_common_id', db.String(20)),
    db.Column('ws_common_renbn', db.String(2)),
    db.Column('contract_no', db.String(12)),
    db.Column('renew_date', db.DateTime),
    db.Column('create_date', db.DateTime),
    db.Column('operate_cd', db.String(128)),
    db.Column('c_flag', db.String(1)),
    db.Column('remark', db.String(80)),
    db.Column('apply_date', db.DateTime),
    db.Column('apply_kind', db.String(4)),
    db.Column('prog_status', db.String(2)),
    db.Column('send_plan_date', db.DateTime),
    db.Column('send_date', db.DateTime),
    db.Column('nttplayer_order_no', db.String(17)),
    db.Column('isp_receipt_result', db.String(2)),
    db.Column('isp_receipt_err_cd', db.String(2)),
    db.Column('isp_receipt_err_reason', db.String(1536)),
    db.Column('isp_service_order_status', db.String(2)),
    db.Column('stop_reason', db.String(1536)),
    db.Column('isp_biko', db.String(2)),
    db.Column('isp_confirm_date', db.DateTime)
)


t_v_ex_plan_mst = db.Table(
    'v_ex_plan_mst',
    db.Column('ex_plan_mst_seq', db.Integer),
    db.Column('plan_cd', db.String(8)),
    db.Column('plan_name', db.String(128)),
    db.Column('plan_short', db.String(128)),
    db.Column('plan_kind', db.String(1)),
    db.Column('plan_status', db.String(1)),
    db.Column('initial_cost', db.Numeric(8, 0)),
    db.Column('first_service_cost', db.Numeric(8, 0)),
    db.Column('service_cost', db.Numeric(8, 0)),
    db.Column('work_cost', db.Numeric(8, 0)),
    db.Column('taxfree_kbn', db.String(1)),
    db.Column('dialup', db.String(4)),
    db.Column('roaming', db.String(4)),
    db.Column('mobilepoint', db.String(4)),
    db.Column('service_dmt_name', db.String(128)),
    db.Column('disc_mail_n', db.Numeric(2, 0)),
    db.Column('disc_cd_mail', db.String(3)),
    db.Column('disc_cd_homepage', db.String(3)),
    db.Column('plan_term', db.Numeric(2, 0)),
    db.Column('create_date', db.DateTime),
    db.Column('renew_date', db.DateTime),
    db.Column('operate_cd', db.String(128)),
    db.Column('c_flag', db.String(1)),
    db.Column('penalty_cost', db.Numeric(8, 0)),
    db.Column('max_penalty_month', db.Numeric(2, 0)),
    db.Column('service_cycle_month', db.Numeric(2, 0)),
    db.Column('creditor_cd', db.String(1)),
    db.Column('creditor_subcd', db.String(3)),
    db.Column('penalty_taxfree_kbn', db.String(1)),
    db.Column('volume_discount_cd', db.String(2)),
    db.Column('append_penalty_cost', db.Numeric(8, 0)),
    db.Column('stat_initial_cost', db.Numeric(8, 0)),
    db.Column('stat_service_cost', db.Numeric(8, 0)),
    db.Column('aplus_initial_cost', db.Numeric(8, 0))
)


t_v_ex_prefix_dat = db.Table(
    'v_ex_prefix_dat',
    db.Column('ex_prefix_dat_seq', db.Integer),
    db.Column('ws_common_id', db.String(20)),
    db.Column('ws_common_renbn', db.String(2)),
    db.Column('opt_contract_no', db.Numeric(10, 0)),
    db.Column('process_kbn', db.String(6)),
    db.Column('msisdn', db.String(11)),
    db.Column('contbase_no', db.String(10)),
    db.Column('exec_plan', db.String(1)),
    db.Column('prefix_cd', db.String(20)),
    db.Column('apply_kind', db.String(4)),
    db.Column('prog_status', db.String(2)),
    db.Column('send_plan_date', db.DateTime),
    db.Column('send_date', db.DateTime),
    db.Column('result_cd', db.String(2)),
    db.Column('result_status', db.String(2)),
    db.Column('create_date', db.DateTime),
    db.Column('renew_date', db.DateTime),
    db.Column('operate_cd', db.String(128)),
    db.Column('c_flag', db.String(1))
)


t_v_ex_privilege = db.Table(
    'v_ex_privilege',
    db.Column('ex_privilege_seq', db.Integer),
    db.Column('customer_id', db.String(8)),
    db.Column('grant_date', db.DateTime),
    db.Column('stage', db.String(1)),
    db.Column('used', db.String(1)),
    db.Column('unchanged', db.String(1)),
    db.Column('create_date', db.DateTime),
    db.Column('renew_date', db.DateTime),
    db.Column('operate_cd', db.String(128))
)


t_v_ex_pt2code_mst = db.Table(
    'v_ex_pt2code_mst',
    db.Column('ex_pt2code_mst_seq', db.Integer),
    db.Column('pt2_plancd', db.String(32)),
    db.Column('quota_size', db.Numeric(10, 0)),
    db.Column('quota_carryforward_kbn', db.String(1)),
    db.Column('apn', db.String(50)),
    db.Column('monthly_charge_kbn', db.String(1)),
    db.Column('create_date', db.DateTime),
    db.Column('renew_date', db.DateTime),
    db.Column('operate_cd', db.String(128))
)


t_v_ex_sales_total = db.Table(
    'v_ex_sales_total',
    db.Column('ex_sales_total_seq', db.Integer),
    db.Column('dmd_no', db.String(13)),
    db.Column('dmd_month', db.String(6)),
    db.Column('dmdto_id', db.String(12)),
    db.Column('taxable_total', db.Numeric(10, 0)),
    db.Column('taxfree_total', db.Numeric(10, 0)),
    db.Column('tax', db.Numeric(10, 0)),
    db.Column('all_total', db.Numeric(10, 0)),
    db.Column('slip_kbn', db.String(1)),
    db.Column('dmd_no2', db.String(13)),
    db.Column('dmd_status', db.String(2)),
    db.Column('demand_kbn', db.String(2)),
    db.Column('payment_kbn', db.String(2)),
    db.Column('payment_date', db.DateTime),
    db.Column('result_cd', db.String(2)),
    db.Column('receipt_sts', db.String(1)),
    db.Column('all_receive_mny', db.Numeric(10, 0)),
    db.Column('receive_mny', db.Numeric(10, 0)),
    db.Column('deficiency', db.Numeric(10, 0)),
    db.Column('detail_kbn', db.String(2)),
    db.Column('detail_rsn', db.String(255)),
    db.Column('pwd_demandprint_kbn', db.String(1)),
    db.Column('cardkind', db.String(2)),
    db.Column('cardno', db.String(16)),
    db.Column('cardvalid', db.String(6)),
    db.Column('verify_no', db.String(8)),
    db.Column('verify_money', db.Numeric(8, 0)),
    db.Column('verify_date', db.DateTime),
    db.Column('agreement', db.String(1)),
    db.Column('pwd_stro_cd', db.String(1)),
    db.Column('trans_bankcd', db.String(4)),
    db.Column('trans_branchcd', db.String(3)),
    db.Column('trans_linecd', db.String(1)),
    db.Column('trans_acckind', db.String(1)),
    db.Column('trans_accno', db.String(7)),
    db.Column('trans_accname', db.String(60)),
    db.Column('kobetu_bankcd', db.String(4)),
    db.Column('kobetu_branchcd', db.String(3)),
    db.Column('kobetu_linecd', db.String(1)),
    db.Column('kobetu_acckind', db.String(1)),
    db.Column('kobetu_accno', db.String(7)),
    db.Column('kobetu_accname', db.String(60)),
    db.Column('dmdto_memo', db.String(128)),
    db.Column('payment_memo', db.String(64)),
    db.Column('slip_reason', db.String(2)),
    db.Column('create_date', db.DateTime),
    db.Column('renew_date', db.DateTime),
    db.Column('operate_cd', db.String(128)),
    db.Column('c_flag', db.String(1)),
    db.Column('kddi_taxable_total', db.Numeric(10, 0)),
    db.Column('kddi_taxfree_total', db.Numeric(10, 0)),
    db.Column('kddi_tax', db.Numeric(10, 0)),
    db.Column('collection_taxable_total', db.Numeric(10, 0)),
    db.Column('collection_taxin_total', db.Numeric(10, 0)),
    db.Column('ntt_e_taxable_total', db.Numeric(10, 0)),
    db.Column('ntt_e_taxfree_total', db.Numeric(10, 0)),
    db.Column('ntt_e_tax_total', db.Numeric(10, 0)),
    db.Column('ntt_limit_date', db.DateTime),
    db.Column('ntt_w_taxable_total', db.Numeric(10, 0)),
    db.Column('ntt_w_taxfree_total', db.Numeric(10, 0)),
    db.Column('ntt_w_tax_total', db.Numeric(10, 0)),
    db.Column('cvs_service_stop_plan', db.DateTime),
    db.Column('cvs_change_date', db.DateTime),
    db.Column('cvs_payment_mny', db.Numeric(10, 0)),
    db.Column('cvs_payment_date', db.DateTime),
    db.Column('cvs_payment_cancel_date', db.DateTime),
    db.Column('other_taxable_total', db.Numeric(10, 0)),
    db.Column('other_taxfree_total', db.Numeric(10, 0)),
    db.Column('other_tax_total', db.Numeric(10, 0)),
    db.Column('use_aim', db.Numeric(1, 0)),
    db.Column('ec_receipt_no', db.String(22)),
    db.Column('stat_kbn', db.Numeric(1, 0))
)


t_v_ex_sales_total_df_ng_wk = db.Table(
    'v_ex_sales_total_df_ng_wk',
    db.Column('ex_sales_total_df_ng_wk_seq', db.Integer),
    db.Column('dmd_no', db.String(13)),
    db.Column('dmd_month', db.String(6)),
    db.Column('dmdto_id', db.String(12)),
    db.Column('cst_no', db.String(20)),
    db.Column('all_total', db.Numeric(10, 0)),
    db.Column('dmd_status', db.String(2)),
    db.Column('send_kbn', db.String(2)),
    db.Column('result_cd', db.String(2)),
    db.Column('payment_date', db.DateTime),
    db.Column('cust_user_type', db.String(1)),
    db.Column('cardno', db.String(16)),
    db.Column('trans_bankcd', db.String(4)),
    db.Column('trans_branchcd', db.String(3)),
    db.Column('trans_linecd', db.String(1)),
    db.Column('trans_acckind', db.String(1)),
    db.Column('trans_accno', db.String(7)),
    db.Column('trans_accname', db.String(60)),
    db.Column('new_cd', db.String(1)),
    db.Column('statuscd', db.String(1)),
    db.Column('description', db.String(100)),
    db.Column('dtrgetamn_before', db.Numeric(10, 0)),
    db.Column('create_date', db.DateTime),
    db.Column('renew_date', db.DateTime),
    db.Column('operate_cd', db.String(128))
)


t_v_ex_sales_total_df_wk = db.Table(
    'v_ex_sales_total_df_wk',
    db.Column('ex_sales_total_df_wk_seq', db.Integer),
    db.Column('dmd_no', db.String(13)),
    db.Column('dmd_month', db.String(6)),
    db.Column('dmdto_id', db.String(12)),
    db.Column('cst_no', db.String(20)),
    db.Column('all_total', db.Numeric(10, 0)),
    db.Column('dmd_status', db.String(2)),
    db.Column('send_kbn', db.String(2)),
    db.Column('result_cd', db.String(2)),
    db.Column('payment_date', db.DateTime),
    db.Column('cust_user_type', db.String(1)),
    db.Column('cardno', db.String(16)),
    db.Column('trans_bankcd', db.String(4)),
    db.Column('trans_branchcd', db.String(3)),
    db.Column('trans_linecd', db.String(1)),
    db.Column('trans_acckind', db.String(1)),
    db.Column('trans_accno', db.String(7)),
    db.Column('trans_accname', db.String(60)),
    db.Column('new_cd', db.String(1)),
    db.Column('statuscd', db.String(1)),
    db.Column('description', db.String(100)),
    db.Column('dtrgetamn_before', db.Numeric(10, 0)),
    db.Column('create_date', db.DateTime),
    db.Column('renew_date', db.DateTime),
    db.Column('operate_cd', db.String(128))
)


t_v_ex_service = db.Table(
    'v_ex_service',
    db.Column('ex_service_seq', db.Integer),
    db.Column('contbase_no', db.String(10)),
    db.Column('idkind_no', db.String(1)),
    db.Column('account_id', db.String(64)),
    db.Column('initial_pass', db.String(16)),
    db.Column('create_date', db.DateTime),
    db.Column('renew_date', db.DateTime),
    db.Column('operate_cd', db.String(128)),
    db.Column('c_flag', db.String(1)),
    db.Column('telno', db.String(11))
)


t_v_ex_sim_dat = db.Table(
    'v_ex_sim_dat',
    db.Column('ex_sim_dat_seq', db.Integer),
    db.Column('ws_common_id', db.String(20)),
    db.Column('ws_common_renbn', db.String(2)),
    db.Column('contract_no', db.String(12)),
    db.Column('opt_contract_no', db.Numeric(10, 0)),
    db.Column('isp_order_no', db.String(20)),
    db.Column('renew_date', db.DateTime),
    db.Column('create_date', db.DateTime),
    db.Column('operate_cd', db.String(128)),
    db.Column('c_flag', db.String(1)),
    db.Column('remark', db.String(80)),
    db.Column('apply_date', db.DateTime),
    db.Column('apply_kind', db.String(4)),
    db.Column('prog_status', db.String(2)),
    db.Column('send_plan_date', db.DateTime),
    db.Column('send_date', db.DateTime),
    db.Column('sim_status', db.String(1)),
    db.Column('imei', db.String(15)),
    db.Column('iccid', db.String(19)),
    db.Column('msisdn', db.String(11)),
    db.Column('send_name', db.String(120)),
    db.Column('send_name_k', db.String(240)),
    db.Column('send_zip', db.String(7)),
    db.Column('send_todohuken', db.String(8)),
    db.Column('send_addr1', db.String(100)),
    db.Column('send_addr2', db.String(100)),
    db.Column('send_build_name', db.String(80)),
    db.Column('send_telno', db.String(11)),
    db.Column('arrival_plan_date', db.DateTime),
    db.Column('arrival_plan_time', db.String(1)),
    db.Column('ship_no', db.String(20)),
    db.Column('direct_date', db.DateTime),
    db.Column('ship_decision_date', db.DateTime),
    db.Column('ship_comp_date', db.DateTime),
    db.Column('send_status', db.String(2)),
    db.Column('item_cd', db.String(10)),
    db.Column('return_limit_date', db.DateTime),
    db.Column('return_flg', db.String(1)),
    db.Column('return_date', db.DateTime),
    db.Column('return_kit_reg_date', db.DateTime),
    db.Column('return_send_date', db.DateTime),
    db.Column('org_ws_common_id', db.String(20)),
    db.Column('sim_acct_stop_date', db.DateTime),
    db.Column('lost_opt_contract_no', db.Numeric(10, 0)),
    db.Column('cont_sex', db.String(1)),
    db.Column('cont_birth', db.DateTime),
    db.Column('mnp_number', db.String(10)),
    db.Column('mnp_telno', db.String(11)),
    db.Column('mnp_reserve_date', db.DateTime),
    db.Column('mnp_line_lastname_k', db.String(80)),
    db.Column('mnp_line_firstname_k', db.String(40)),
    db.Column('mnp_line_lastname', db.String(40)),
    db.Column('mnp_line_firstname', db.String(20)),
    db.Column('mnp_line_birth', db.DateTime),
    db.Column('portable_tel_flg', db.String(1)),
    db.Column('send_name_lastname', db.String(60)),
    db.Column('send_name_firstname', db.String(60)),
    db.Column('send_name_lastname_k', db.String(120)),
    db.Column('send_name_firstname_k', db.String(120)),
    db.Column('mnp_out_number', db.String(10)),
    db.Column('mnp_out_status', db.String(1)),
    db.Column('mnp_out_apply_date', db.DateTime),
    db.Column('mnp_out_order_date', db.DateTime),
    db.Column('mnp_out_order_comp_date', db.DateTime),
    db.Column('mnp_out_expire_date', db.DateTime),
    db.Column('mnp_out_end_date', db.DateTime),
    db.Column('mnp_out_line_lastname_k', db.String(80)),
    db.Column('mnp_out_line_firstname_k', db.String(40)),
    db.Column('mnp_out_line_lastname', db.String(40)),
    db.Column('mnp_out_line_firstname', db.String(20)),
    db.Column('mnp_out_line_birth', db.DateTime),
    db.Column('charge_count', db.Numeric(10, 0)),
    db.Column('charge_mb', db.Numeric(10, 0)),
    db.Column('charge_date', db.DateTime),
    db.Column('quota_code', db.String(128)),
    db.Column('semiblack_add_status', db.String(1)),
    db.Column('semiblack_add_reserve_date', db.DateTime),
    db.Column('semiblack_add_apply_date', db.DateTime),
    db.Column('semiblack_add_comp_date', db.DateTime),
    db.Column('semiblack_add_error_msg', db.String(100)),
    db.Column('quota_carryover_mb', db.Numeric(10, 0)),
    db.Column('quota_carryover_date', db.DateTime),
    db.Column('rent_device_cd', db.String(20)),
    db.Column('rent_lost_opt_contract_no', db.Numeric(10, 0)),
    db.Column('rent_return_limit_date', db.DateTime),
    db.Column('rent_return_flg', db.String(1)),
    db.Column('rent_return_date', db.DateTime)
)


t_v_ex_tepco_dat = db.Table(
    'v_ex_tepco_dat',
    db.Column('ex_tepco_dat_seq', db.Integer),
    db.Column('ws_common_id', db.String(20)),
    db.Column('ws_common_renbn', db.String(2)),
    db.Column('contract_no', db.String(12)),
    db.Column('isp_order_no', db.String(20)),
    db.Column('apply_date', db.DateTime),
    db.Column('send_plan_date', db.DateTime),
    db.Column('send_date', db.DateTime),
    db.Column('apply_kind', db.String(4)),
    db.Column('prog_status', db.String(2)),
    db.Column('syori_kind', db.String(2)),
    db.Column('syori_status', db.String(1)),
    db.Column('username', db.String(32)),
    db.Column('domainname', db.String(32)),
    db.Column('tpc_no', db.String(14)),
    db.Column('user_cd', db.String(1)),
    db.Column('zip', db.String(8)),
    db.Column('todohuken', db.String(8)),
    db.Column('gun', db.String(20)),
    db.Column('ku', db.String(20)),
    db.Column('area', db.String(40)),
    db.Column('chome', db.String(10)),
    db.Column('banchi', db.String(20)),
    db.Column('build_name', db.String(80)),
    db.Column('telno', db.String(13)),
    db.Column('toi_telno', db.String(13)),
    db.Column('email', db.String(80)),
    db.Column('house_cd1', db.String(1)),
    db.Column('house_cd2', db.String(1)),
    db.Column('house_cd22', db.String(1)),
    db.Column('lead_in', db.String(1)),
    db.Column('ftth_cd', db.String(1)),
    db.Column('house_floor', db.String(1)),
    db.Column('tpc_user_cd', db.String(1)),
    db.Column('line_cd', db.String(1)),
    db.Column('work_flag', db.String(2)),
    db.Column('tpc_service_cd', db.String(1)),
    db.Column('tpc_kari_date', db.DateTime),
    db.Column('tpc_date', db.DateTime),
    db.Column('start_date', db.DateTime),
    db.Column('closed_date', db.DateTime),
    db.Column('check_date', db.DateTime),
    db.Column('check_time', db.String(1)),
    db.Column('work_date', db.DateTime),
    db.Column('work_time', db.String(1)),
    db.Column('work_end_date', db.DateTime),
    db.Column('cash_cd', db.String(1)),
    db.Column('lump_sum', db.String(30)),
    db.Column('apart_cd', db.String(13)),
    db.Column('opt_flag', db.String(30)),
    db.Column('vdsl_model', db.String(8)),
    db.Column('voip_model', db.String(8)),
    db.Column('musen_model', db.String(8)),
    db.Column('tpc_result', db.String(3)),
    db.Column('tpc_details', db.String(160)),
    db.Column('isp_notes', db.String(160)),
    db.Column('tpc_notes', db.String(160)),
    db.Column('campaign_cd', db.String(15)),
    db.Column('agency_cd', db.String(12)),
    db.Column('create_date', db.DateTime),
    db.Column('renew_date', db.DateTime),
    db.Column('operate_cd', db.String(128)),
    db.Column('c_flag', db.String(1)),
    db.Column('remark', db.String(80))
)


t_v_ex_tg_set_info = db.Table(
    'v_ex_tg_set_info',
    db.Column('ex_tg_set_info_seq', db.Integer),
    db.Column('contract_no', db.String(12)),
    db.Column('isp_order_no', db.String(20)),
    db.Column('renew_date', db.DateTime),
    db.Column('create_date', db.DateTime),
    db.Column('operate_cd', db.String(128)),
    db.Column('c_flag', db.String(1)),
    db.Column('apply_date', db.DateTime),
    db.Column('tg_set_camp_status', db.String(2)),
    db.Column('tg_set_appy_available', db.String(1)),
    db.Column('tg_set_appy_ng_reason', db.String(1)),
    db.Column('tg_set_appy_result_date', db.DateTime),
    db.Column('tg_cont_no', db.String(13)),
    db.Column('tg_set_cont_no', db.String(13)),
    db.Column('tg_toss_cont_no', db.Numeric(8, 0)),
    db.Column('tg_customer_name', db.String(142)),
    db.Column('tg_customer_kname', db.String(142)),
    db.Column('tg_cont_status_gas', db.String(40)),
    db.Column('tg_start_date_gas', db.DateTime),
    db.Column('tg_cont_status_electric', db.String(40)),
    db.Column('tg_start_date_electric', db.DateTime),
    db.Column('tg_set_camp_available', db.String(1)),
    db.Column('tg_set_camp_ng_reason', db.String(1)),
    db.Column('removal_flag', db.String(1)),
    db.Column('yobi01', db.String(100))
)


t_v_ex_tone_prefix_dat = db.Table(
    'v_ex_tone_prefix_dat',
    db.Column('ex_tone_prefix_dat_seq', db.Integer),
    db.Column('ws_common_id', db.String(20)),
    db.Column('ws_common_renbn', db.String(2)),
    db.Column('opt_contract_no', db.Numeric(10, 0)),
    db.Column('process_kbn', db.String(6)),
    db.Column('msisdn', db.String(11)),
    db.Column('contbase_no', db.String(10)),
    db.Column('exec_plan', db.String(1)),
    db.Column('prefix_cd', db.String(20)),
    db.Column('apply_kind', db.String(4)),
    db.Column('prog_status', db.String(2)),
    db.Column('send_plan_date', db.DateTime),
    db.Column('send_date', db.DateTime),
    db.Column('result_receive_date', db.DateTime),
    db.Column('result_cd', db.String(2)),
    db.Column('result_status', db.String(2)),
    db.Column('create_date', db.DateTime),
    db.Column('renew_date', db.DateTime),
    db.Column('operate_cd', db.String(128)),
    db.Column('c_flag', db.String(1))
)


t_v_ex_uname_dat = db.Table(
    'v_ex_uname_dat',
    db.Column('ex_uname_dat_seq', db.Integer),
    db.Column('ws_common_id', db.String(20)),
    db.Column('ws_common_renbn', db.Numeric(2, 0)),
    db.Column('contract_no', db.String(12)),
    db.Column('create_date', db.DateTime),
    db.Column('renew_date', db.DateTime),
    db.Column('operate_cd', db.String(128)),
    db.Column('c_flag', db.String(1)),
    db.Column('remark', db.String(80)),
    db.Column('second_lv_domain', db.String(64)),
    db.Column('top_lv_domain', db.String(3)),
    db.Column('domain_status', db.Numeric(2, 0)),
    db.Column('domain_start_date', db.DateTime),
    db.Column('domain_end_date', db.DateTime),
    db.Column('domain_exp_date', db.DateTime),
    db.Column('owner_j_last_name', db.String(50)),
    db.Column('owner_e_last_name', db.String(50)),
    db.Column('owner_j_first_name', db.String(50)),
    db.Column('owner_e_first_name', db.String(50)),
    db.Column('owner_user_type', db.String(1)),
    db.Column('owner_j_org_name', db.String(100)),
    db.Column('owner_e_org_name', db.String(100)),
    db.Column('owner_zip', db.String(16)),
    db.Column('owner_j_addr1', db.Numeric(2, 0)),
    db.Column('owner_e_addr1', db.String(20)),
    db.Column('owner_j_addr2', db.String(50)),
    db.Column('owner_e_addr2', db.String(50)),
    db.Column('owner_j_addr3', db.String(50)),
    db.Column('owner_e_addr3', db.String(50)),
    db.Column('owner_j_addr4', db.String(50)),
    db.Column('owner_e_addr4', db.String(50)),
    db.Column('owner_telno', db.String(20)),
    db.Column('owner_faxno', db.String(20)),
    db.Column('owner_email', db.String(100)),
    db.Column('admin_j_last_name', db.String(50)),
    db.Column('admin_e_last_name', db.String(50)),
    db.Column('admin_j_first_name', db.String(50)),
    db.Column('admin_e_first_name', db.String(50)),
    db.Column('admin_user_type', db.String(1)),
    db.Column('admin_j_org_name', db.String(100)),
    db.Column('admin_e_org_name', db.String(100)),
    db.Column('admin_zip', db.String(16)),
    db.Column('admin_j_addr1', db.Numeric(2, 0)),
    db.Column('admin_e_addr1', db.String(20)),
    db.Column('admin_j_addr2', db.String(50)),
    db.Column('admin_e_addr2', db.String(50)),
    db.Column('admin_j_addr3', db.String(50)),
    db.Column('admin_e_addr3', db.String(50)),
    db.Column('admin_j_addr4', db.String(50)),
    db.Column('admin_e_addr4', db.String(50)),
    db.Column('admin_telno', db.String(20)),
    db.Column('admin_faxno', db.String(20)),
    db.Column('admin_email', db.String(100)),
    db.Column('tech_j_last_name', db.String(50)),
    db.Column('tech_e_last_name', db.String(50)),
    db.Column('tech_j_first_name', db.String(50)),
    db.Column('tech_e_first_name', db.String(50)),
    db.Column('tech_user_type', db.String(1)),
    db.Column('tech_j_org_name', db.String(100)),
    db.Column('tech_e_org_name', db.String(100)),
    db.Column('tech_zip', db.String(16)),
    db.Column('tech_j_addr1', db.Numeric(2, 0)),
    db.Column('tech_e_addr1', db.String(20)),
    db.Column('tech_j_addr2', db.String(50)),
    db.Column('tech_e_addr2', db.String(50)),
    db.Column('tech_j_addr3', db.String(50)),
    db.Column('tech_e_addr3', db.String(50)),
    db.Column('tech_j_addr4', db.String(50)),
    db.Column('tech_e_addr4', db.String(50)),
    db.Column('tech_telno', db.String(20)),
    db.Column('tech_faxno', db.String(20)),
    db.Column('tech_email', db.String(100)),
    db.Column('acc_j_last_name', db.String(50)),
    db.Column('acc_e_last_name', db.String(50)),
    db.Column('acc_j_first_name', db.String(50)),
    db.Column('acc_e_first_name', db.String(50)),
    db.Column('acc_user_type', db.String(1)),
    db.Column('acc_j_org_name', db.String(100)),
    db.Column('acc_e_org_name', db.String(100)),
    db.Column('acc_zip', db.String(16)),
    db.Column('acc_j_addr1', db.Numeric(2, 0)),
    db.Column('acc_e_addr1', db.String(20)),
    db.Column('acc_j_addr2', db.String(50)),
    db.Column('acc_e_addr2', db.String(50)),
    db.Column('acc_j_addr3', db.String(50)),
    db.Column('acc_e_addr3', db.String(50)),
    db.Column('acc_j_addr4', db.String(50)),
    db.Column('acc_e_addr4', db.String(50)),
    db.Column('acc_telno', db.String(20)),
    db.Column('acc_faxno', db.String(20)),
    db.Column('acc_email', db.String(100)),
    db.Column('gmo_id', db.String(18)),
    db.Column('gmo_pass', db.String(18)),
    db.Column('release_apply_date', db.DateTime),
    db.Column('domain_pending_id', db.String(18))
)


t_v_ex_voip_c_dat = db.Table(
    'v_ex_voip_c_dat',
    db.Column('ex_voip_c_dat_seq', db.Integer),
    db.Column('ws_common_id', db.String(20)),
    db.Column('ws_common_renbn', db.String(2)),
    db.Column('contract_no', db.String(12)),
    db.Column('opt_contract_no', db.Numeric(10, 0)),
    db.Column('isp_order_no', db.String(20)),
    db.Column('isp_opt_order_no', db.String(20)),
    db.Column('enduser_id', db.String(20)),
    db.Column('apply_date', db.DateTime),
    db.Column('send_plan_date', db.DateTime),
    db.Column('send_date', db.DateTime),
    db.Column('apply_kind', db.String(4)),
    db.Column('prog_status', db.String(2)),
    db.Column('apply_brand', db.String(2)),
    db.Column('order_no', db.String(10)),
    db.Column('acca_no', db.String(60)),
    db.Column('business_cd', db.String(2)),
    db.Column('action', db.String(2)),
    db.Column('option_kind', db.String(2)),
    db.Column('line_name', db.String(60)),
    db.Column('zip', db.String(8)),
    db.Column('todohuken', db.String(8)),
    db.Column('gun', db.String(30)),
    db.Column('ku', db.String(30)),
    db.Column('area', db.String(30)),
    db.Column('banchi', db.String(50)),
    db.Column('build_name', db.String(120)),
    db.Column('telno', db.String(13)),
    db.Column('toi_telno', db.String(13)),
    db.Column('email', db.String(90)),
    db.Column('cpe_provider', db.String(1)),
    db.Column('cpe_installer', db.String(1)),
    db.Column('cpe_kind', db.String(3)),
    db.Column('vo_user_id', db.String(40)),
    db.Column('vo_passwd', db.String(20)),
    db.Column('vo_telno', db.String(15)),
    db.Column('vo_server', db.String(50)),
    db.Column('vo_domain', db.String(50)),
    db.Column('isp_circuit_no', db.String(20)),
    db.Column('ntt_work_date', db.DateTime),
    db.Column('billing_date', db.DateTime),
    db.Column('change_date', db.DateTime),
    db.Column('cancel_date', db.DateTime),
    db.Column('agency_cd', db.String(12)),
    db.Column('create_date', db.DateTime),
    db.Column('renew_date', db.DateTime),
    db.Column('operate_cd', db.String(128)),
    db.Column('c_flag', db.String(1)),
    db.Column('remark', db.String(80))
)


t_v_ex_voip_c_num_mst = db.Table(
    'v_ex_voip_c_num_mst',
    db.Column('ex_voip_c_num_mst_seq', db.Integer),
    db.Column('telno', db.String(13)),
    db.Column('sip_user_id', db.String(40)),
    db.Column('sip_password', db.String(20)),
    db.Column('sip_server', db.String(50)),
    db.Column('status', db.String(1)),
    db.Column('pr_order_line_date', db.DateTime),
    db.Column('start_date', db.DateTime),
    db.Column('end_date', db.DateTime),
    db.Column('create_date', db.DateTime),
    db.Column('renew_date', db.DateTime),
    db.Column('operate_cd', db.String(128))
)


t_v_ex_voip_f_dat = db.Table(
    'v_ex_voip_f_dat',
    db.Column('ex_voip_f_dat_seq', db.Integer),
    db.Column('ws_common_id', db.String(20)),
    db.Column('ws_common_renbn', db.String(2)),
    db.Column('contract_no', db.String(12)),
    db.Column('opt_contract_no', db.Numeric(10, 0)),
    db.Column('isp_portable_userid', db.String(12)),
    db.Column('isp_userid', db.String(15)),
    db.Column('isp_order_no', db.String(12)),
    db.Column('apply_date', db.DateTime),
    db.Column('send_plan_date', db.DateTime),
    db.Column('send_date', db.DateTime),
    db.Column('apply_kind', db.String(4)),
    db.Column('prog_status', db.String(2)),
    db.Column('master_status', db.String(2)),
    db.Column('business_cd', db.String(2)),
    db.Column('telno_050', db.String(32)),
    db.Column('telno_0abj', db.String(32)),
    db.Column('portable_tel', db.String(15)),
    db.Column('portable_cd', db.String(1)),
    db.Column('account_050', db.String(32)),
    db.Column('password_050', db.String(32)),
    db.Column('password_0abj', db.String(32)),
    db.Column('ppp_name', db.String(128)),
    db.Column('rental_cd', db.String(1)),
    db.Column('iad_type', db.String(1)),
    db.Column('plan_cd', db.String(8)),
    db.Column('use_change_date', db.DateTime),
    db.Column('ip_start_date', db.DateTime),
    db.Column('ip_end_date', db.DateTime),
    db.Column('suspend_date', db.DateTime),
    db.Column('re_suspend_date', db.DateTime),
    db.Column('iad_status', db.String(1)),
    db.Column('dl_start_date', db.DateTime),
    db.Column('dl_term_date', db.DateTime),
    db.Column('dl_comp_date', db.DateTime),
    db.Column('dl_remind_no', db.Numeric(1, 0)),
    db.Column('start_0abj', db.DateTime),
    db.Column('end_0abj', db.DateTime),
    db.Column('portable_work_date', db.DateTime),
    db.Column('ftth_start_date', db.DateTime),
    db.Column('portable_date', db.DateTime),
    db.Column('portable_ng_cd', db.String(80)),
    db.Column('portable_ng', db.String(256)),
    db.Column('portable_remind_no', db.Numeric(1, 0)),
    db.Column('portable_ng_date', db.DateTime),
    db.Column('bill_flag', db.String(8)),
    db.Column('unnotify_ref_status', db.String(1)),
    db.Column('refusal_number_status', db.String(1)),
    db.Column('catch_status', db.String(1)),
    db.Column('portable_status', db.String(1)),
    db.Column('status_104', db.String(1)),
    db.Column('user_name', db.String(40)),
    db.Column('user_kana', db.String(72)),
    db.Column('zip', db.String(8)),
    db.Column('todohuken', db.String(8)),
    db.Column('gun', db.String(50)),
    db.Column('ku', db.String(40)),
    db.Column('area', db.String(40)),
    db.Column('chome', db.String(10)),
    db.Column('banchi', db.String(40)),
    db.Column('build_name', db.String(126)),
    db.Column('ntt_name', db.String(90)),
    db.Column('ntt_kana', db.String(180)),
    db.Column('ntt_zip', db.String(8)),
    db.Column('ntt_todohuken', db.String(8)),
    db.Column('ntt_gun', db.String(40)),
    db.Column('ntt_ku', db.String(40)),
    db.Column('ntt_area', db.String(40)),
    db.Column('ntt_chome', db.String(10)),
    db.Column('ntt_banchi', db.String(40)),
    db.Column('ntt_build_name', db.String(80)),
    db.Column('toi_telno', db.String(13)),
    db.Column('direct_name', db.String(128)),
    db.Column('direct_kana', db.String(240)),
    db.Column('direct_zip', db.String(8)),
    db.Column('direct_todohuken', db.String(8)),
    db.Column('direct_gun', db.String(40)),
    db.Column('direct_ku', db.String(40)),
    db.Column('direct_area', db.String(40)),
    db.Column('direct_chome', db.String(10)),
    db.Column('direct_banchi', db.String(40)),
    db.Column('direct_build_name', db.String(80)),
    db.Column('build_kind', db.String(1)),
    db.Column('user_cd', db.String(1)),
    db.Column('note1', db.String(32)),
    db.Column('note2', db.String(256)),
    db.Column('campaign_cd', db.String(15)),
    db.Column('agency_cd', db.String(12)),
    db.Column('mansion_id', db.String(13)),
    db.Column('sip_server_address', db.String(50)),
    db.Column('create_date', db.DateTime),
    db.Column('renew_date', db.DateTime),
    db.Column('operate_cd', db.String(128)),
    db.Column('c_flag', db.String(1)),
    db.Column('no_return_kbn', db.String(1)),
    db.Column('entry_cd', db.String(13)),
    db.Column('remark', db.String(80))
)


t_v_ex_voip_f_ref_telno_info = db.Table(
    'v_ex_voip_f_ref_telno_info',
    db.Column('ex_voip_f_ref_telno_info_seq', db.Integer),
    db.Column('ip_telno', db.String(11)),
    db.Column('ref_telno_01', db.String(11)),
    db.Column('ref_telno_02', db.String(11)),
    db.Column('ref_telno_03', db.String(11)),
    db.Column('ref_telno_04', db.String(11)),
    db.Column('ref_telno_05', db.String(11)),
    db.Column('ref_telno_06', db.String(11)),
    db.Column('ref_telno_07', db.String(11)),
    db.Column('ref_telno_08', db.String(11)),
    db.Column('ref_telno_09', db.String(11)),
    db.Column('ref_telno_10', db.String(11)),
    db.Column('ref_telno_11', db.String(11)),
    db.Column('ref_telno_12', db.String(11)),
    db.Column('ref_telno_13', db.String(11)),
    db.Column('ref_telno_14', db.String(11)),
    db.Column('ref_telno_15', db.String(11)),
    db.Column('ref_telno_16', db.String(11)),
    db.Column('ref_telno_17', db.String(11)),
    db.Column('ref_telno_18', db.String(11)),
    db.Column('ref_telno_19', db.String(11)),
    db.Column('ref_telno_20', db.String(11)),
    db.Column('ref_telno_21', db.String(11)),
    db.Column('ref_telno_22', db.String(11)),
    db.Column('ref_telno_23', db.String(11)),
    db.Column('ref_telno_24', db.String(11)),
    db.Column('ref_telno_25', db.String(11)),
    db.Column('ref_telno_26', db.String(11)),
    db.Column('ref_telno_27', db.String(11)),
    db.Column('ref_telno_28', db.String(11)),
    db.Column('ref_telno_29', db.String(11)),
    db.Column('ref_telno_30', db.String(11)),
    db.Column('create_date', db.DateTime),
    db.Column('renew_date', db.DateTime),
    db.Column('operate_cd', db.String(128)),
    db.Column('c_flag', db.String(1))
)


t_v_ex_voip_p_dat = db.Table(
    'v_ex_voip_p_dat',
    db.Column('ex_voip_p_dat_seq', db.Integer),
    db.Column('ws_common_id', db.String(20)),
    db.Column('ws_common_renbn', db.String(2)),
    db.Column('contract_no', db.String(12)),
    db.Column('opt_contract_no', db.Numeric(10, 0)),
    db.Column('apply_date', db.DateTime),
    db.Column('send_plan_date', db.DateTime),
    db.Column('send_date', db.DateTime),
    db.Column('apply_kind', db.String(4)),
    db.Column('prog_status', db.String(2)),
    db.Column('oem_id', db.String(4)),
    db.Column('oem_key', db.String(32)),
    db.Column('phone_user_id', db.String(128)),
    db.Column('isp_num', db.String(3)),
    db.Column('telno', db.String(13)),
    db.Column('sip_user_id', db.String(40)),
    db.Column('sip_password', db.String(20)),
    db.Column('sip_server', db.String(50)),
    db.Column('remark', db.String(80)),
    db.Column('create_date', db.DateTime),
    db.Column('renew_date', db.DateTime),
    db.Column('operate_cd', db.String(128)),
    db.Column('c_flag', db.String(1))
)


t_v_ex_wimax_dat = db.Table(
    'v_ex_wimax_dat',
    db.Column('ex_wimax_dat_seq', db.Integer),
    db.Column('ws_common_id', db.String(20)),
    db.Column('ws_common_renbn', db.String(2)),
    db.Column('contract_no', db.String(12)),
    db.Column('opt_contract_no', db.Numeric(10, 0)),
    db.Column('renew_date', db.DateTime),
    db.Column('create_date', db.DateTime),
    db.Column('operate_cd', db.String(128)),
    db.Column('c_flag', db.String(1)),
    db.Column('remark', db.String(80)),
    db.Column('apply_date', db.DateTime),
    db.Column('apply_kind', db.String(4)),
    db.Column('prog_status', db.String(2)),
    db.Column('send_plan_date', db.DateTime),
    db.Column('send_date', db.DateTime),
    db.Column('wimax_user_id', db.String(10)),
    db.Column('cui', db.String(20)),
    db.Column('uq_issue_date', db.DateTime),
    db.Column('uq_cont_start_date', db.DateTime),
    db.Column('mac_address', db.String(12)),
    db.Column('serial_no', db.String(25)),
    db.Column('send_name', db.String(100)),
    db.Column('send_name_kana', db.String(100)),
    db.Column('send_zip', db.String(7)),
    db.Column('send_todohuken', db.String(8)),
    db.Column('send_addr1', db.String(50)),
    db.Column('send_addr2', db.String(60)),
    db.Column('send_build_name', db.String(80)),
    db.Column('send_telno', db.String(13)),
    db.Column('arrival_plan_date', db.DateTime),
    db.Column('arrival_plan_time', db.String(1)),
    db.Column('ship_no', db.String(20)),
    db.Column('direct_date', db.DateTime),
    db.Column('ship_plan_date', db.DateTime),
    db.Column('ship_decision_date', db.DateTime),
    db.Column('id_renbn', db.Numeric(2, 0)),
    db.Column('equipment_info', db.String(8)),
    db.Column('send_status', db.String(2)),
    db.Column('ship_comp_date', db.DateTime),
    db.Column('iccid', db.String(19)),
    db.Column('ccode', db.String(11)),
    db.Column('uq_apply_no', db.String(9)),
    db.Column('uq_user_cd', db.String(8)),
    db.Column('user_birth', db.DateTime),
    db.Column('shop_accept_date', db.DateTime),
    db.Column('user_sex', db.String(1)),
    db.Column('policy_cd', db.String(40)),
    db.Column('uq_apply_date', db.DateTime),
    db.Column('mvno_plan_cd', db.String(3))
)


t_v_ex_xtyle_info = db.Table(
    'v_ex_xtyle_info',
    db.Column('ex_xtyle_info_seq', db.Integer),
    db.Column('opt_contract_no', db.Numeric(10, 0)),
    db.Column('prog_status', db.String(2)),
    db.Column('send_date', db.DateTime),
    db.Column('form_no', db.String(20)),
    db.Column('serial_no', db.String(9)),
    db.Column('id', db.String(7)),
    db.Column('create_date', db.DateTime),
    db.Column('renew_date', db.DateTime),
    db.Column('operate_cd', db.String(128)),
    db.Column('c_flag', db.String(1))
)


t_v_fl_tariff_mst = db.Table(
    'v_fl_tariff_mst',
    db.Column('stage', db.Numeric(1, 0)),
    db.Column('lower_limit_traffic', db.Numeric(19, 0)),
    db.Column('unit_cost', db.Numeric(10, 0)),
    db.Column('unit_name', db.String(10)),
    db.Column('create_date', db.DateTime),
    db.Column('renew_date', db.DateTime),
    db.Column('operate_cd', db.String(128))
)


t_v_fl_traffic_info = db.Table(
    'v_fl_traffic_info',
    db.Column('bill_month', db.String(6)),
    db.Column('line_no', db.Numeric(7, 0)),
    db.Column('account_id', db.String(256)),
    db.Column('sum_month', db.String(6)),
    db.Column('total_traffic', db.Numeric(19, 0)),
    db.Column('up_traffic', db.Numeric(19, 0)),
    db.Column('down_traffic', db.Numeric(19, 0)),
    db.Column('create_date', db.DateTime),
    db.Column('renew_date', db.DateTime),
    db.Column('operate_cd', db.String(128))
)


t_v_fusion_opr_mst = db.Table(
    'v_fusion_opr_mst',
    db.Column('apply_kind_cd', db.String(4)),
    db.Column('apply_kind_name', db.String(80)),
    db.Column('opr_apply_kind_cd', db.String(3)),
    db.Column('opr_apply_kind_name', db.String(60)),
    db.Column('data_cd', db.String(5)),
    db.Column('create_date', db.DateTime),
    db.Column('renew_date', db.DateTime),
    db.Column('operate_cd', db.String(128)),
    db.Column('c_flag', db.String(1))
)


t_v_goods_dat = db.Table(
    'v_goods_dat',
    db.Column('ws_common_id', db.String(20)),
    db.Column('ws_common_renbn', db.String(2)),
    db.Column('contract_no', db.String(12)),
    db.Column('renew_date', db.DateTime),
    db.Column('create_date', db.DateTime),
    db.Column('operate_cd', db.String(128)),
    db.Column('remark', db.String(80)),
    db.Column('apply_date', db.DateTime),
    db.Column('apply_kind', db.String(4)),
    db.Column('prog_status', db.String(2)),
    db.Column('send_plan_date', db.DateTime),
    db.Column('send_date', db.DateTime),
    db.Column('model_number', db.String(64)),
    db.Column('order_no', db.String(16)),
    db.Column('deliver_date', db.DateTime),
    db.Column('deliver_time', db.String(2)),
    db.Column('deliver_firstname', db.String(20)),
    db.Column('deliver_lastname', db.String(50)),
    db.Column('deliver_chgdept', db.String(50)),
    db.Column('deliver_chgpost', db.String(20)),
    db.Column('deliver_chgname', db.String(20)),
    db.Column('deliver_zip', db.String(8)),
    db.Column('deliver_todohuken', db.String(8)),
    db.Column('deliver_gun', db.String(40)),
    db.Column('deliver_ku', db.String(40)),
    db.Column('deliver_area', db.String(40)),
    db.Column('deliver_chome', db.String(10)),
    db.Column('deliver_banchi', db.String(40)),
    db.Column('deliver_build_name', db.String(150)),
    db.Column('search_id', db.String(14)),
    db.Column('lot_cd', db.String(6)),
    db.Column('deliver_start_date', db.DateTime),
    db.Column('deliver_end_date', db.DateTime),
    db.Column('deliver_status', db.String(2))
)


t_v_goods_remainder = db.Table(
    'v_goods_remainder',
    db.Column('contract_no', db.String(12)),
    db.Column('create_date', db.DateTime),
    db.Column('renew_date', db.DateTime),
    db.Column('operate_cd', db.String(128)),
    db.Column('installment_cd', db.String(3)),
    db.Column('order_no', db.String(16)),
    db.Column('start_month', db.Date),
    db.Column('end_plan_month', db.Date),
    db.Column('goods_cost', db.Numeric(8, 0)),
    db.Column('end_month', db.Date),
    db.Column('remaining_month', db.Date),
    db.Column('remaining_cost', db.Numeric(8, 0)),
    db.Column('demand_count', db.Numeric(2, 0)),
    db.Column('demand_cost', db.Numeric(8, 0))
)


t_v_hbm_bill_info = db.Table(
    'v_hbm_bill_info',
    db.Column('msisdn', db.String(11)),
    db.Column('used_month', db.Date),
    db.Column('capacity', db.Numeric(9, 0)),
    db.Column('create_date', db.DateTime),
    db.Column('renew_date', db.DateTime),
    db.Column('operate_cd', db.String(128)),
    db.Column('bill_month', db.Date),
    db.Column('unit_cost', db.Numeric(10, 4)),
    db.Column('quantity', db.Numeric(19, 0))
)


t_v_hbm_dat = db.Table(
    'v_hbm_dat',
    db.Column('ws_common_id', db.String(20)),
    db.Column('ws_common_renbn', db.String(2)),
    db.Column('contract_no', db.String(12)),
    db.Column('opt_contract_no', db.Numeric(10, 0)),
    db.Column('isp_order_no', db.String(20)),
    db.Column('renew_date', db.DateTime),
    db.Column('create_date', db.DateTime),
    db.Column('operate_cd', db.String(128)),
    db.Column('c_flag', db.String(1)),
    db.Column('remark', db.String(80)),
    db.Column('apply_date', db.DateTime),
    db.Column('apply_kind', db.String(4)),
    db.Column('prog_status', db.String(2)),
    db.Column('send_plan_date', db.DateTime),
    db.Column('send_date', db.DateTime),
    db.Column('hbm_status', db.String(1)),
    db.Column('imei', db.String(15)),
    db.Column('iccid', db.String(19)),
    db.Column('msisdn', db.String(11)),
    db.Column('send_name', db.String(120)),
    db.Column('send_zip', db.String(7)),
    db.Column('send_todohuken', db.String(8)),
    db.Column('send_addr1', db.String(100)),
    db.Column('send_addr2', db.String(100)),
    db.Column('send_build_name', db.String(80)),
    db.Column('send_telno', db.String(11)),
    db.Column('arrival_plan_date', db.DateTime),
    db.Column('arrival_plan_time', db.String(1)),
    db.Column('ship_no', db.String(20)),
    db.Column('direct_date', db.DateTime),
    db.Column('ship_decision_date', db.DateTime),
    db.Column('ship_comp_date', db.DateTime),
    db.Column('send_status', db.String(2)),
    db.Column('item_cd', db.String(10)),
    db.Column('return_limit_date', db.DateTime),
    db.Column('return_flg', db.String(1)),
    db.Column('return_date', db.DateTime),
    db.Column('return_kit_reg_date', db.DateTime),
    db.Column('return_send_date', db.DateTime),
    db.Column('org_ws_common_id', db.String(20)),
    db.Column('sim_acct_stop_date', db.DateTime),
    db.Column('lost_opt_contract_no', db.Numeric(10, 0)),
    db.Column('user_name_k', db.String(100)),
    db.Column('user_sex', db.String(1)),
    db.Column('user_birth', db.DateTime),
    db.Column('device_cd', db.String(2)),
    db.Column('mnp_number', db.String(10)),
    db.Column('mnp_telno', db.String(11)),
    db.Column('mnp_expire_date', db.DateTime),
    db.Column('mnp_line_name', db.String(100)),
    db.Column('mnp_line_name_k', db.String(100)),
    db.Column('pt2_account_status', db.String(1)),
    db.Column('charge_date', db.DateTime),
    db.Column('portable_tel_flg', db.String(1)),
    db.Column('mnp_out_number', db.String(10)),
    db.Column('mnp_out_status', db.String(1)),
    db.Column('mnp_out_apply_date', db.DateTime),
    db.Column('mnp_out_order_date', db.DateTime),
    db.Column('mnp_out_order_comp_date', db.DateTime),
    db.Column('mnp_out_expire_date', db.DateTime),
    db.Column('mnp_out_end_date', db.DateTime),
    db.Column('mnp_out_line_lastname_k', db.String(80)),
    db.Column('mnp_out_line_firstname_k', db.String(40)),
    db.Column('mnp_out_line_lastname', db.String(40)),
    db.Column('mnp_out_line_firstname', db.String(20)),
    db.Column('mnp_out_line_birth', db.DateTime),
    db.Column('semiblack_add_status', db.String(1)),
    db.Column('semiblack_add_reserve_date', db.DateTime),
    db.Column('semiblack_add_apply_date', db.DateTime),
    db.Column('semiblack_add_comp_date', db.DateTime),
    db.Column('semiblack_add_error_msg', db.String(100)),
    db.Column('issue_error_msg', db.String(500)),
    db.Column('issue_touser_error_msg', db.String(500)),
    db.Column('notdelivered_date', db.DateTime),
    db.Column('tcard_issue', db.String(1)),
    db.Column('channel_flg', db.String(1)),
    db.Column('changevoice_flg', db.String(1)),
    db.Column('quota_carryover_date', db.DateTime),
    db.Column('pt2_flg', db.String(1)),
    db.Column('warranty_start_date', db.DateTime)
)


t_v_hibit_collection_info = db.Table(
    'v_hibit_collection_info',
    db.Column('create_date', db.DateTime),
    db.Column('renew_date', db.DateTime),
    db.Column('operate_cd', db.String(128)),
    db.Column('c_flag', db.String(1)),
    db.Column('unext_id', db.String(10)),
    db.Column('used_month', db.Date),
    db.Column('bill_month', db.Date),
    db.Column('service', db.String(128)),
    db.Column('base_cost', db.Numeric(12, 4)),
    db.Column('jimu_cost', db.Numeric(12, 4)),
    db.Column('ppv_cost', db.Numeric(12, 4)),
    db.Column('iyaku_cost', db.Numeric(12, 4)),
    db.Column('tax_cost', db.Numeric(12, 4)),
    db.Column('total_cost', db.Numeric(12, 4))
)


t_v_icracked_cont = db.Table(
    'v_icracked_cont',
    db.Column('imei', db.String(15)),
    db.Column('contract_no', db.String(12)),
    db.Column('opt_contract_no', db.Numeric(10, 0)),
    db.Column('imei_create_date', db.Date),
    db.Column('service_start_date', db.Date),
    db.Column('repair_date', db.Date),
    db.Column('repair_content', db.String(2)),
    db.Column('renew_date', db.DateTime),
    db.Column('create_date', db.DateTime),
    db.Column('operate_cd', db.String(128)),
    db.Column('c_flag', db.String(1)),
    db.Column('diff_flag', db.String(1)),
    db.Column('prog_status', db.String(2))
)


t_v_installment_mst = db.Table(
    'v_installment_mst',
    db.Column('installment_cd', db.String(3)),
    db.Column('create_date', db.DateTime),
    db.Column('renew_date', db.DateTime),
    db.Column('operate_cd', db.String(128)),
    db.Column('plan_cd', db.String(8)),
    db.Column('split_count', db.Numeric(2, 0)),
    db.Column('first_cost', db.Numeric(8, 0)),
    db.Column('regular_cost', db.Numeric(8, 0)),
    db.Column('june_extra_cost', db.Numeric(8, 0)),
    db.Column('december_extra_cost', db.Numeric(8, 0))
)


t_v_ip_num_mst = db.Table(
    'v_ip_num_mst',
    db.Column('ip_telno', db.String(11)),
    db.Column('use_status', db.String(2)),
    db.Column('start_date', db.DateTime),
    db.Column('end_date', db.DateTime),
    db.Column('entry_cd', db.String(13)),
    db.Column('plan_cd', db.String(8)),
    db.Column('create_date', db.DateTime),
    db.Column('renew_date', db.DateTime),
    db.Column('operate_cd', db.String(128)),
    db.Column('c_flag', db.String(1))
)


t_v_kddi_bill_remainder = db.Table(
    'v_kddi_bill_remainder',
    db.Column('create_date', db.DateTime),
    db.Column('renew_date', db.DateTime),
    db.Column('operate_cd', db.String(128)),
    db.Column('kddi_cont_no', db.String(10)),
    db.Column('used_month', db.Date),
    db.Column('kddi_plan_cd', db.String(10)),
    db.Column('remainder_kind', db.String(1)),
    db.Column('remainder_status', db.String(1)),
    db.Column('bill_month', db.Date),
    db.Column('plan_bill_month', db.Date),
    db.Column('kddi_plan_name', db.String(90)),
    db.Column('cost', db.Numeric(12, 4)),
    db.Column('taxfree_kbn', db.String(1)),
    db.Column('creditor_cd', db.String(1)),
    db.Column('creditor_subcd', db.String(3)),
    db.Column('tax_percent', db.Numeric(4, 1))
)


t_v_kddi_collection_info = db.Table(
    'v_kddi_collection_info',
    db.Column('create_date', db.DateTime),
    db.Column('renew_date', db.DateTime),
    db.Column('operate_cd', db.String(128)),
    db.Column('c_flag', db.String(1)),
    db.Column('kddi_cont_no', db.String(10)),
    db.Column('used_month', db.Date),
    db.Column('kddi_plan_cd', db.String(10)),
    db.Column('bill_month', db.Date),
    db.Column('kddi_plan_name', db.String(90)),
    db.Column('cost', db.Numeric(12, 4)),
    db.Column('taxfree_kbn', db.String(1)),
    db.Column('creditor_cd', db.String(1)),
    db.Column('creditor_subcd', db.String(3)),
    db.Column('tax_percent', db.Numeric(4, 1))
)


t_v_kddi_collection_sum = db.Table(
    'v_kddi_collection_sum',
    db.Column('create_date', db.DateTime),
    db.Column('renew_date', db.DateTime),
    db.Column('operate_cd', db.String(128)),
    db.Column('c_flag', db.String(1)),
    db.Column('kddi_cont_no', db.String(10)),
    db.Column('used_month', db.Date),
    db.Column('bill_month', db.Date),
    db.Column('kddi_taxable_total', db.Numeric(12, 4)),
    db.Column('kddi_taxfree_total', db.Numeric(12, 4)),
    db.Column('collection_taxable_total', db.Numeric(12, 4)),
    db.Column('collection_taxin_total', db.Numeric(12, 4)),
    db.Column('taxable_total', db.Numeric(12, 4)),
    db.Column('taxfree_total', db.Numeric(12, 4)),
    db.Column('tax_total', db.Numeric(12, 4)),
    db.Column('all_total', db.Numeric(12, 4)),
    db.Column('plan_bill_month', db.Date)
)


t_v_kddi_cont = db.Table(
    'v_kddi_cont',
    db.Column('contract_no', db.String(12)),
    db.Column('kddi_mng_no', db.Numeric(10, 0)),
    db.Column('renew_date', db.DateTime),
    db.Column('create_date', db.DateTime),
    db.Column('operate_cd', db.String(128)),
    db.Column('c_flag', db.String(1)),
    db.Column('remark', db.String(80)),
    db.Column('kddi_cont_no', db.String(10)),
    db.Column('isp_order_no', db.String(20)),
    db.Column('kddi_create_date', db.DateTime),
    db.Column('line_plan_date', db.DateTime),
    db.Column('line_start_date', db.DateTime),
    db.Column('tel_pre_service_num', db.Numeric(1, 0)),
    db.Column('tel_service_num', db.Numeric(1, 0)),
    db.Column('tv_pre_service_num', db.Numeric(1, 0)),
    db.Column('tv_service_num', db.Numeric(1, 0)),
    db.Column('kddi_use_end_date', db.DateTime),
    db.Column('kddi_cont_end_date', db.DateTime),
    db.Column('service_kind', db.String(1)),
    db.Column('service_state_flg', db.String(1)),
    db.Column('design_comp_date', db.DateTime),
    db.Column('outside_comp_date', db.DateTime),
    db.Column('work_stay_reason', db.String(120)),
    db.Column('provide_date', db.DateTime),
    db.Column('provide_flg', db.String(1)),
    db.Column('provide_ng_reason', db.String(120)),
    db.Column('work_plan_date', db.DateTime),
    db.Column('work_end_date', db.DateTime),
    db.Column('counting_start_month', db.Date)
)


t_v_kddi_cont_opt = db.Table(
    'v_kddi_cont_opt',
    db.Column('kddi_cont_no', db.String(10)),
    db.Column('service_cont_no', db.String(8)),
    db.Column('renew_date', db.DateTime),
    db.Column('create_date', db.DateTime),
    db.Column('operate_cd', db.String(128)),
    db.Column('c_flag', db.String(1)),
    db.Column('remark', db.String(80)),
    db.Column('service_kbn', db.String(1)),
    db.Column('telno', db.String(11)),
    db.Column('portable_flg', db.String(1)),
    db.Column('portable_prog_flg', db.String(1)),
    db.Column('kddi_apply_date', db.DateTime),
    db.Column('bill_start_date', db.DateTime),
    db.Column('use_end_date', db.DateTime),
    db.Column('cont_end_date', db.DateTime),
    db.Column('talkie_flg', db.String(1)),
    db.Column('talkie_no', db.String(11))
)


t_v_kddi_dat = db.Table(
    'v_kddi_dat',
    db.Column('kddi_mng_no', db.Numeric(10, 0)),
    db.Column('seq_no', db.Numeric(2, 0)),
    db.Column('renew_date', db.DateTime),
    db.Column('create_date', db.DateTime),
    db.Column('operate_cd', db.String(128)),
    db.Column('c_flag', db.String(1)),
    db.Column('remark', db.String(80)),
    db.Column('apply_date', db.DateTime),
    db.Column('service_kbn', db.String(1)),
    db.Column('apply_kind', db.String(4)),
    db.Column('prog_status', db.String(2)),
    db.Column('send_plan_date', db.DateTime),
    db.Column('send_date', db.DateTime),
    db.Column('cancel_plan_date', db.DateTime),
    db.Column('tel_no', db.String(11)),
    db.Column('ntt_return_kbn', db.String(1)),
    db.Column('tel_talkie_flg', db.String(1)),
    db.Column('tel_talkie_no', db.String(11))
)


t_v_kddi_dmd = db.Table(
    'v_kddi_dmd',
    db.Column('kddi_mng_no', db.Numeric(10, 0)),
    db.Column('renew_date', db.DateTime),
    db.Column('create_date', db.DateTime),
    db.Column('operate_cd', db.String(128)),
    db.Column('c_flag', db.String(1)),
    db.Column('remark', db.String(80)),
    db.Column('kddi_dmd_shift_flg', db.String(1)),
    db.Column('kddi_dmd_kind', db.String(1)),
    db.Column('au_cont_telno', db.String(11)),
    db.Column('au_cont_birth', db.DateTime),
    db.Column('au_cont_name', db.String(60)),
    db.Column('au_cont_name_k', db.String(60)),
    db.Column('au_cont_sign_flg', db.String(1)),
    db.Column('auonenet_cont_cd', db.String(10)),
    db.Column('auonenet_cont_name', db.String(60)),
    db.Column('auonenet_cont_name_k', db.String(60)),
    db.Column('auonenet_sign_flg', db.String(1)),
    db.Column('kotei_telno', db.String(10)),
    db.Column('kotei_cont_name', db.String(60)),
    db.Column('kotei_cont_name_k', db.String(60)),
    db.Column('kotei_sign_flg', db.String(1)),
    db.Column('kddi_dmd_name', db.String(60)),
    db.Column('kddi_dmd_name_k', db.String(60)),
    db.Column('kddi_dmd_sign_flg', db.String(1)),
    db.Column('kddi_pay_name', db.String(60)),
    db.Column('kddi_pay_name_k', db.String(60)),
    db.Column('pay_sign_flg', db.String(1)),
    db.Column('pledge_name_flg', db.String(1)),
    db.Column('apply_sign_flg', db.String(1)),
    db.Column('apply_pledge_flg', db.String(1)),
    db.Column('paper_bill_flg', db.String(1)),
    db.Column('kddi_payment_kbn', db.String(1)),
    db.Column('kddi_payment_shift_kbn', db.String(1)),
    db.Column('myline_acount', db.String(10)),
    db.Column('kddi_email_apply_flag', db.String(1)),
    db.Column('auonenet_email', db.String(129)),
    db.Column('kddi_dmd_result_kbn', db.String(1)),
    db.Column('kddi_dmd_method', db.String(1)),
    db.Column('kddi_dmd_first_month', db.String(6)),
    db.Column('kddi_dmd_error_cd', db.String(4)),
    db.Column('kddi_dmd_error_msg', db.String(200)),
    db.Column('kddi_dmd_receipt_date', db.DateTime),
    db.Column('kddi_claim_cont_cd', db.String(1)),
    db.Column('kddi_claim_close_reserve_cd', db.String(1)),
    db.Column('servicestop_file_date', db.DateTime)
)


t_v_kddi_info = db.Table(
    'v_kddi_info',
    db.Column('kddi_mng_no', db.Numeric(10, 0)),
    db.Column('renew_date', db.DateTime),
    db.Column('create_date', db.DateTime),
    db.Column('operate_cd', db.String(128)),
    db.Column('c_flag', db.String(1)),
    db.Column('remark', db.String(80)),
    db.Column('kddi_order_no', db.String(10)),
    db.Column('kddi_jit_bumon_cd', db.String(4)),
    db.Column('kddi_tyoku_kbn', db.String(1)),
    db.Column('kddi_agency_cd', db.String(10)),
    db.Column('cont_zip', db.String(7)),
    db.Column('cont_todohuken', db.String(8)),
    db.Column('cont_shiku', db.String(60)),
    db.Column('cont_area_chome_banchi', db.String(60)),
    db.Column('cont_build_name', db.String(100)),
    db.Column('cont_telno1', db.String(11)),
    db.Column('cont_telno2', db.String(11)),
    db.Column('email', db.String(129)),
    db.Column('est_place_flg', db.String(1)),
    db.Column('est_zip', db.String(7)),
    db.Column('est_todohuken', db.String(8)),
    db.Column('est_shiku', db.String(60)),
    db.Column('est_area_chome_banchi', db.String(60)),
    db.Column('est_build_name', db.String(100)),
    db.Column('dest_place_flg', db.String(1)),
    db.Column('dest_name', db.String(60)),
    db.Column('dest_name_k', db.String(60)),
    db.Column('dest_zip', db.String(7)),
    db.Column('dest_todohuken', db.String(8)),
    db.Column('dest_shiku', db.String(60)),
    db.Column('dest_area_chome_banchi', db.String(60)),
    db.Column('dest_build_name', db.String(100)),
    db.Column('dest_telno', db.String(11)),
    db.Column('cont_group_no', db.String(10)),
    db.Column('article_no', db.String(8)),
    db.Column('ridge_id', db.String(2)),
    db.Column('room_no', db.String(5)),
    db.Column('modular_board_num', db.String(1)),
    db.Column('line1_no', db.String(11)),
    db.Column('line1_status', db.String(1)),
    db.Column('line2_no', db.String(11)),
    db.Column('line2_status', db.String(1)),
    db.Column('taxfree_user_cd', db.String(1)),
    db.Column('hikari_plus_tel_flg', db.String(1)),
    db.Column('portable_tel_flg', db.String(1)),
    db.Column('telno_050_flg', db.String(1)),
    db.Column('portable_tel', db.String(11)),
    db.Column('ntt_name', db.String(60)),
    db.Column('ntt_name_k', db.String(60)),
    db.Column('interrupt_call_flg', db.String(1)),
    db.Column('caller_id_display_flg', db.String(1)),
    db.Column('notice_telno_flg', db.String(1)),
    db.Column('nuisance_call_repulse_flg', db.String(1)),
    db.Column('caller_id_notice_flg', db.String(1)),
    db.Column('caller_id_notice_cd', db.String(1)),
    db.Column('detail_output_flg', db.String(1)),
    db.Column('number_guidance_flg', db.String(1)),
    db.Column('hellopage_flg', db.String(1)),
    db.Column('hikari_plus_tv_flg', db.String(1)),
    db.Column('stb_cd', db.String(4)),
    db.Column('filter_flg', db.String(1)),
    db.Column('filter_cd', db.String(4)),
    db.Column('kaketuke_support_flg', db.String(1)),
    db.Column('campain_apply_date', db.DateTime),
    db.Column('interrupt_number_flg', db.String(1)),
    db.Column('arrival_plan_date', db.DateTime),
    db.Column('dest_addr_change_flg', db.String(1)),
    db.Column('musen_lan_rental_cd', db.String(4)),
    db.Column('musen_lan_rental_num', db.String(2)),
    db.Column('add_hgw_cd', db.String(4)),
    db.Column('add_hgw_num', db.String(2)),
    db.Column('add_stb_cd', db.String(4)),
    db.Column('add_stb_num', db.String(2)),
    db.Column('entering_plan_date', db.DateTime),
    db.Column('redirect_call_flg', db.String(1)),
    db.Column('house_cd', db.String(1)),
    db.Column('possession_cd', db.String(1)),
    db.Column('isp_cd', db.String(3)),
    db.Column('incoming_notice_flg', db.String(1)),
    db.Column('au_term_telno1', db.String(11)),
    db.Column('au_term_telno2', db.String(11)),
    db.Column('au_term_telno3', db.String(11)),
    db.Column('ntt_line_cd', db.String(2)),
    db.Column('kddi_memo', db.String(16)),
    db.Column('same_0abj_telno', db.String(11)),
    db.Column('exist_line_flg', db.String(1)),
    db.Column('important_notice', db.String(100)),
    db.Column('ntt_zip', db.String(7)),
    db.Column('ntt_todohuken', db.String(8)),
    db.Column('ntt_shiku', db.String(60)),
    db.Column('ntt_area_chome_banchi', db.String(60)),
    db.Column('ntt_build_name', db.String(100)),
    db.Column('speed_kbn', db.String(1)),
    db.Column('musen_lan_rental_cd2', db.String(4)),
    db.Column('musen_lan_rental_num2', db.String(2)),
    db.Column('musen_lan_rental_cd3', db.String(4)),
    db.Column('musen_lan_rental_num3', db.String(2)),
    db.Column('musen_lan_rental_cd4', db.String(4)),
    db.Column('musen_lan_rental_num4', db.String(2)),
    db.Column('musen_lan_rental_cd5', db.String(4)),
    db.Column('musen_lan_rental_num5', db.String(2)),
    db.Column('work_date_id', db.String(10)),
    db.Column('monthly_item01', db.String(4)),
    db.Column('monthly_item02', db.String(4)),
    db.Column('monthly_item03', db.String(4)),
    db.Column('monthly_item04', db.String(4)),
    db.Column('monthly_item05', db.String(4)),
    db.Column('monthly_item06', db.String(4)),
    db.Column('monthly_item07', db.String(4)),
    db.Column('monthly_item08', db.String(4)),
    db.Column('monthly_item09', db.String(4)),
    db.Column('monthly_item10', db.String(4)),
    db.Column('monthly_item11', db.String(4)),
    db.Column('monthly_item12', db.String(4)),
    db.Column('pre_voip_co_cd', db.String(4)),
    db.Column('pre_voip_co_cd2', db.String(4)),
    db.Column('est_floors', db.String(3)),
    db.Column('cont_room_no', db.String(40)),
    db.Column('owner_name', db.String(60)),
    db.Column('owner_address', db.String(100)),
    db.Column('owner_telno', db.String(11)),
    db.Column('owner_kbn', db.String(1)),
    db.Column('est_telno', db.String(11)),
    db.Column('kddi3m_au_smart_val_cd', db.String(15)),
    db.Column('kddi3m_multi_campaign_kbn', db.String(1)),
    db.Column('kddi3m_campaign_flg', db.String(1)),
    db.Column('kddi3m_applyprint_no', db.String(9))
)


t_v_kddi_liquidation_info = db.Table(
    'v_kddi_liquidation_info',
    db.Column('create_date', db.DateTime),
    db.Column('renew_date', db.DateTime),
    db.Column('operate_cd', db.String(128)),
    db.Column('c_flag', db.String(1)),
    db.Column('kddi_cont_no', db.String(10)),
    db.Column('used_month', db.Date),
    db.Column('kddi_plan_cd', db.String(10)),
    db.Column('bill_month', db.Date),
    db.Column('kddi_plan_name', db.String(90)),
    db.Column('cost', db.Numeric(12, 4)),
    db.Column('taxfree_kbn', db.String(1)),
    db.Column('creditor_cd', db.String(1)),
    db.Column('creditor_subcd', db.String(3)),
    db.Column('tax_percent', db.Numeric(4, 1))
)


t_v_l2_call_log = db.Table(
    'v_l2_call_log',
    db.Column('used_month', db.Date),
    db.Column('line_no', db.Numeric(7, 0)),
    db.Column('telno', db.String(16)),
    db.Column('record_no', db.String(6)),
    db.Column('call_date', db.String(8)),
    db.Column('call_time', db.String(6)),
    db.Column('telno_dialed', db.String(32)),
    db.Column('dist_type', db.String(11)),
    db.Column('dist_detail', db.String(44)),
    db.Column('call_duration', db.String(7)),
    db.Column('call_charge', db.Numeric(8, 2)),
    db.Column('time_period', db.String(24)),
    db.Column('discount', db.String(24)),
    db.Column('call_classification_1', db.String(24)),
    db.Column('call_classification_2', db.String(24)),
    db.Column('call_classification_3', db.String(24)),
    db.Column('bill_month', db.Date),
    db.Column('contract_no', db.String(12)),
    db.Column('user_charge', db.Numeric(6, 0)),
    db.Column('bill_kbn_cd', db.String(2)),
    db.Column('create_date', db.DateTime),
    db.Column('renew_date', db.DateTime),
    db.Column('operate_cd', db.String(128)),
    db.Column('user_duration', db.String(7))
)


t_v_lf_cont = db.Table(
    'v_lf_cont',
    db.Column('contract_no', db.String(12)),
    db.Column('opt_contract_no', db.Numeric(10, 0)),
    db.Column('isp_user_id', db.String(20)),
    db.Column('renew_date', db.DateTime),
    db.Column('create_date', db.DateTime),
    db.Column('operate_cd', db.String(128)),
    db.Column('remark', db.String(80)),
    db.Column('unext_id', db.String(10)),
    db.Column('license_key1', db.String(50)),
    db.Column('license_key2', db.String(50)),
    db.Column('license_key3', db.String(50)),
    db.Column('license_key4', db.String(50)),
    db.Column('license_key5', db.String(50)),
    db.Column('license_key6', db.String(50)),
    db.Column('license_key7', db.String(50)),
    db.Column('apply_request_date', db.Date),
    db.Column('apply_process_date', db.Date),
    db.Column('end_request_date', db.Date),
    db.Column('end_process_date', db.Date)
)


t_v_lf_dat = db.Table(
    'v_lf_dat',
    db.Column('ws_common_id', db.String(20)),
    db.Column('ws_common_renbn', db.String(2)),
    db.Column('contract_no', db.String(12)),
    db.Column('create_date', db.DateTime),
    db.Column('renew_date', db.DateTime),
    db.Column('operate_cd', db.String(128)),
    db.Column('remark', db.String(80)),
    db.Column('apply_kind', db.String(4)),
    db.Column('prog_status', db.String(2)),
    db.Column('apply_date', db.DateTime),
    db.Column('send_plan_date', db.DateTime),
    db.Column('send_date', db.DateTime),
    db.Column('opt_contract_no', db.Numeric(10, 0)),
    db.Column('firstname', db.String(20)),
    db.Column('firstname_k', db.String(20)),
    db.Column('lastname', db.String(50)),
    db.Column('lastname_k', db.String(100)),
    db.Column('lf_sex', db.String(1)),
    db.Column('lf_birth', db.DateTime),
    db.Column('lf_telno', db.String(20)),
    db.Column('lf_mobile', db.String(20)),
    db.Column('lf_zip', db.String(7)),
    db.Column('lf_todohuken', db.String(4)),
    db.Column('lf_shiku_area_chome', db.String(50)),
    db.Column('lf_banchi', db.String(50)),
    db.Column('lf_build_name', db.String(40)),
    db.Column('lf_email', db.String(128)),
    db.Column('plan_type', db.String(1))
)


t_v_lte_dat = db.Table(
    'v_lte_dat',
    db.Column('ws_common_id', db.String(20)),
    db.Column('ws_common_renbn', db.String(2)),
    db.Column('contract_no', db.String(12)),
    db.Column('opt_contract_no', db.Numeric(10, 0)),
    db.Column('renew_date', db.DateTime),
    db.Column('create_date', db.DateTime),
    db.Column('operate_cd', db.String(128)),
    db.Column('c_flag', db.String(1)),
    db.Column('remark', db.String(80)),
    db.Column('apply_date', db.DateTime),
    db.Column('apply_kind', db.String(4)),
    db.Column('prog_status', db.String(2)),
    db.Column('send_plan_date', db.DateTime),
    db.Column('send_date', db.DateTime),
    db.Column('lte_user_id', db.String(10)),
    db.Column('imei', db.String(15)),
    db.Column('iccid', db.String(19)),
    db.Column('msisdn', db.String(11)),
    db.Column('lte_machin_meker', db.String(50)),
    db.Column('lte_machin_model', db.String(50)),
    db.Column('send_name', db.String(100)),
    db.Column('send_name_kana', db.String(100)),
    db.Column('send_zip', db.String(7)),
    db.Column('send_todohuken', db.String(8)),
    db.Column('send_addr1', db.String(40)),
    db.Column('send_addr2', db.String(50)),
    db.Column('send_addr3', db.String(50)),
    db.Column('send_addr4', db.String(40)),
    db.Column('send_build_name', db.String(80)),
    db.Column('send_telno', db.String(13)),
    db.Column('arrival_plan_date', db.DateTime),
    db.Column('arrival_plan_time', db.String(1)),
    db.Column('ship_no', db.String(20)),
    db.Column('direct_date', db.DateTime),
    db.Column('ship_plan_date', db.DateTime),
    db.Column('ship_decision_date', db.DateTime),
    db.Column('ship_comp_date', db.DateTime),
    db.Column('id_renbn', db.Numeric(2, 0))
)


t_v_measured_mst = db.Table(
    'v_measured_mst',
    db.Column('measured_cd', db.String(4)),
    db.Column('measured_name', db.String(32)),
    db.Column('rate', db.Numeric(10, 4)),
    db.Column('measured_unit', db.Numeric(3, 0)),
    db.Column('measured_start', db.Numeric(3, 0)),
    db.Column('measured_limit', db.Numeric(8, 0)),
    db.Column('taxfree_kbn', db.String(1)),
    db.Column('unit_name', db.String(10)),
    db.Column('create_date', db.DateTime),
    db.Column('renew_date', db.DateTime),
    db.Column('operate_cd', db.String(128)),
    db.Column('c_flag', db.String(1))
)


t_v_monitor = db.Table(
    'v_monitor',
    db.Column('monitor_type', db.String(2)),
    db.Column('contract_no', db.String(12)),
    db.Column('cont_cancel_date', db.DateTime)
)


t_v_mopita_info = db.Table(
    'v_mopita_info',
    db.Column('contbase_no', db.String(10)),
    db.Column('mopita_acct_id', db.String(12)),
    db.Column('mopita_status', db.String(2)),
    db.Column('mopita_pwd', db.String(7)),
    db.Column('mopita_reg_date', db.DateTime),
    db.Column('mopita_user_id', db.String(32)),
    db.Column('mopita_end_date', db.DateTime),
    db.Column('create_date', db.DateTime),
    db.Column('renew_date', db.DateTime),
    db.Column('operate_cd', db.String(128)),
    db.Column('c_flag', db.String(1)),
    db.Column('mti_pin_cd', db.String(12))
)


t_v_mti_pin_mst = db.Table(
    'v_mti_pin_mst',
    db.Column('pin_cd', db.String(12)),
    db.Column('expire_date', db.DateTime),
    db.Column('use_status', db.String(1)),
    db.Column('renew_date', db.DateTime),
    db.Column('create_date', db.DateTime),
    db.Column('operate_cd', db.String(128)),
    db.Column('c_flag', db.String(1))
)


t_v_necat_dat = db.Table(
    'v_necat_dat',
    db.Column('ws_common_id', db.String(20)),
    db.Column('ws_common_renbn', db.String(2)),
    db.Column('contract_no', db.String(12)),
    db.Column('opt_contract_no', db.Numeric(10, 0)),
    db.Column('isp_order_no', db.String(14)),
    db.Column('status', db.String(1)),
    db.Column('apply_kind', db.String(4)),
    db.Column('syori_status', db.String(2)),
    db.Column('syohin_cd', db.String(20)),
    db.Column('product_no', db.String(20)),
    db.Column('mac_address', db.String(12)),
    db.Column('invoice_no', db.String(20)),
    db.Column('plan_cd', db.String(10)),
    db.Column('zip', db.String(8)),
    db.Column('addr1', db.String(4)),
    db.Column('addr2', db.String(50)),
    db.Column('addr3', db.String(50)),
    db.Column('apply_date', db.DateTime),
    db.Column('send_plan_date', db.DateTime),
    db.Column('send_date', db.DateTime),
    db.Column('arrival_plan_date', db.DateTime),
    db.Column('arrival_plan_time', db.String(2)),
    db.Column('ship_date', db.DateTime),
    db.Column('arrival_date', db.DateTime),
    db.Column('arv_info_recv_date', db.DateTime),
    db.Column('arv_info_no', db.Numeric(2, 0)),
    db.Column('arv_ng_cd', db.String(2)),
    db.Column('cont_start_date', db.DateTime),
    db.Column('cont_end_date', db.DateTime),
    db.Column('iad_customer_id', db.String(30)),
    db.Column('create_date', db.DateTime),
    db.Column('renew_date', db.DateTime),
    db.Column('operate_cd', db.String(128)),
    db.Column('c_flag', db.String(1)),
    db.Column('remark', db.String(80))
)


t_v_nicos_carddb = db.Table(
    'v_nicos_carddb',
    db.Column('card_mng_no', db.String(12)),
    db.Column('recurring_id', db.String(15)),
    db.Column('card_status', db.String(2)),
    db.Column('cardno', db.String(16)),
    db.Column('cardvalid', db.String(6)),
    db.Column('result_cd', db.String(3)),
    db.Column('create_date', db.DateTime),
    db.Column('renew_date', db.DateTime),
    db.Column('operate_cd', db.String(128))
)


t_v_nicos_demand_trans = db.Table(
    'v_nicos_demand_trans',
    db.Column('dmdto_id', db.String(12)),
    db.Column('nicos_trans_cd', db.String(9)),
    db.Column('create_date', db.DateTime),
    db.Column('renew_date', db.DateTime),
    db.Column('operate_cd', db.String(128))
)


t_v_ntt_collection_info = db.Table(
    'v_ntt_collection_info',
    db.Column('create_date', db.DateTime),
    db.Column('renew_date', db.DateTime),
    db.Column('operate_cd', db.String(128)),
    db.Column('ntt_e_cont_id', db.String(16)),
    db.Column('used_month', db.Date),
    db.Column('ntt_plan_cd', db.String(10)),
    db.Column('isp_order_no', db.String(16)),
    db.Column('bill_month', db.Date),
    db.Column('plan_bill_month', db.Date),
    db.Column('ntt_plan_name', db.String(160)),
    db.Column('cost', db.Numeric(12, 4)),
    db.Column('taxfree_kbn', db.String(1)),
    db.Column('creditor_cd', db.String(1)),
    db.Column('used_start_date', db.DateTime),
    db.Column('used_end_date', db.DateTime),
    db.Column('ntt_branch_name', db.String(20)),
    db.Column('old_ntt_dmd_no', db.String(10)),
    db.Column('charge_back', db.String(1)),
    db.Column('ntt_adjust_id', db.String(12)),
    db.Column('creditor_subcd', db.String(3))
)


t_v_ntt_cor_add_cont = db.Table(
    'v_ntt_cor_add_cont',
    db.Column('contract_code', db.String(13)),
    db.Column('add_contract_code', db.String(13)),
    db.Column('opt_contract_no', db.Numeric(10, 0)),
    db.Column('ntt_ew_kind', db.String(1)),
    db.Column('renew_date', db.DateTime),
    db.Column('create_date', db.DateTime),
    db.Column('operate_cd', db.String(128)),
    db.Column('c_flag', db.String(1)),
    db.Column('service_kind', db.String(1)),
    db.Column('service_name', db.String(90)),
    db.Column('order_class', db.String(4)),
    db.Column('order_status', db.String(2)),
    db.Column('application_pername', db.String(90)),
    db.Column('contact_phone', db.String(90)),
    db.Column('applied_date', db.DateTime),
    db.Column('appoint_date', db.DateTime),
    db.Column('change_date', db.DateTime),
    db.Column('serv_start_day', db.DateTime),
    db.Column('serv_end_day', db.DateTime),
    db.Column('plan_name', db.String(128)),
    db.Column('operator_ent_name', db.String(40)),
    db.Column('operator_cor_branch_name', db.String(70)),
    db.Column('operator_cor_section_name', db.String(70)),
    db.Column('operator_cor_charge_name', db.String(128)),
    db.Column('operator_cor_phone', db.String(13)),
    db.Column('operator_cor_fax', db.String(13)),
    db.Column('sales_ent_name', db.String(40)),
    db.Column('sales_cor_branch_name', db.String(70)),
    db.Column('sales_cor_section_name', db.String(70)),
    db.Column('sales_cor_chargen_ame', db.String(128)),
    db.Column('sales_cor_phone', db.String(13)),
    db.Column('sales_cor_fax', db.String(13)),
    db.Column('date_renewed', db.DateTime),
    db.Column('add_phone_no', db.String(13)),
    db.Column('service_code', db.String(8)),
    db.Column('add_phone_kbn', db.String(1))
)


t_v_ntt_cor_add_dat = db.Table(
    'v_ntt_cor_add_dat',
    db.Column('ws_common_id', db.String(20)),
    db.Column('ws_common_renbn', db.String(2)),
    db.Column('contract_code', db.String(13)),
    db.Column('add_contract_code', db.String(13)),
    db.Column('create_date', db.DateTime),
    db.Column('renew_date', db.DateTime),
    db.Column('operate_cd', db.String(128)),
    db.Column('c_flag', db.String(1)),
    db.Column('remark', db.String(80)),
    db.Column('apply_kind', db.String(4)),
    db.Column('prog_status', db.String(2)),
    db.Column('apply_date', db.DateTime),
    db.Column('send_plan_date', db.DateTime),
    db.Column('send_date', db.DateTime),
    db.Column('service_kbn', db.String(1)),
    db.Column('service_code', db.String(8)),
    db.Column('telno', db.String(13)),
    db.Column('opt_contract_no', db.Numeric(10, 0))
)


t_v_ntt_cor_bill_dtl = db.Table(
    'v_ntt_cor_bill_dtl',
    db.Column('bill_month', db.Date),
    db.Column('ws_kbn', db.String(2)),
    db.Column('data_renbn', db.Numeric(7, 0)),
    db.Column('contract_code', db.String(13)),
    db.Column('giji_dmd_dtlcd', db.String(4)),
    db.Column('dtl_name', db.String(320)),
    db.Column('ws_price', db.Numeric(7, 1)),
    db.Column('tax_kbn', db.String(2)),
    db.Column('dmd_month', db.String(6)),
    db.Column('use_start_date', db.DateTime),
    db.Column('use_end_date', db.DateTime),
    db.Column('used_month', db.Date),
    db.Column('contract_no', db.String(12)),
    db.Column('user_charge', db.Numeric(7, 1)),
    db.Column('taxfree_kbn', db.String(1)),
    db.Column('bill_kbn_cd', db.String(2)),
    db.Column('opt_plan_cd', db.String(8)),
    db.Column('create_date', db.DateTime),
    db.Column('renew_date', db.DateTime),
    db.Column('operate_cd', db.String(128))
)


t_v_ntt_cor_bill_mst = db.Table(
    'v_ntt_cor_bill_mst',
    db.Column('giji_dmd_dtlcd', db.String(4)),
    db.Column('bill_flag', db.String(1)),
    db.Column('selling_rate', db.Numeric(4, 2)),
    db.Column('bill_kbn_cd', db.String(2)),
    db.Column('dtl_context', db.String(128)),
    db.Column('create_date', db.DateTime),
    db.Column('renew_date', db.DateTime),
    db.Column('operate_cd', db.String(128))
)


t_v_ntt_cor_charge_dat = db.Table(
    'v_ntt_cor_charge_dat',
    db.Column('contract_no', db.String(12)),
    db.Column('renbn', db.String(3)),
    db.Column('rating_name', db.String(64)),
    db.Column('price', db.Numeric(14, 4)),
    db.Column('count', db.Numeric(10, 0)),
    db.Column('renew_date', db.DateTime),
    db.Column('create_date', db.DateTime),
    db.Column('operate_cd', db.String(128)),
    db.Column('c_flag', db.String(1))
)


t_v_ntt_cor_cont = db.Table(
    'v_ntt_cor_cont',
    db.Column('contract_no', db.String(12)),
    db.Column('isp_order_no', db.String(20)),
    db.Column('renew_date', db.DateTime),
    db.Column('create_date', db.DateTime),
    db.Column('operate_cd', db.String(128)),
    db.Column('c_flag', db.String(1)),
    db.Column('business_name', db.String(3)),
    db.Column('contract_code', db.String(13)),
    db.Column('divert_consent_no', db.String(11)),
    db.Column('partner_code', db.String(18)),
    db.Column('service_name', db.String(50)),
    db.Column('service_item', db.String(256)),
    db.Column('so', db.String(4)),
    db.Column('so_stat', db.String(2)),
    db.Column('contractor_name', db.String(128)),
    db.Column('contractor_kname', db.String(256)),
    db.Column('cur_user_addr_code', db.String(802)),
    db.Column('applicationper_name', db.String(128)),
    db.Column('contact_phone', db.String(13)),
    db.Column('applied_date', db.DateTime),
    db.Column('appoint_date', db.DateTime),
    db.Column('change_date', db.DateTime),
    db.Column('business_contract_start_date', db.DateTime),
    db.Column('contract_end_date', db.DateTime),
    db.Column('flets_contract_start_date', db.DateTime),
    db.Column('ftv_trans_business_name', db.String(3)),
    db.Column('indoor_stem_wiring_div', db.String(64)),
    db.Column('ftv_business_cont_start_date', db.DateTime),
    db.Column('ftv_business_cont_end_date', db.DateTime),
    db.Column('regular_charge_div', db.String(8)),
    db.Column('service_change_code', db.String(13)),
    db.Column('operator_ent_name', db.String(40)),
    db.Column('operator_cor_branch_name', db.String(70)),
    db.Column('operator_cor_section_name', db.String(70)),
    db.Column('operator_cor_charge_name', db.String(128)),
    db.Column('operator_cor_phone', db.String(13)),
    db.Column('operator_cor_fax', db.String(13)),
    db.Column('sales_ent_name', db.String(40)),
    db.Column('sales_cor_branch_name', db.String(70)),
    db.Column('sales_cor_section_name', db.String(70)),
    db.Column('sales_cor_chargen_ame', db.String(80)),
    db.Column('sales_cor_phone', db.String(13)),
    db.Column('sales_cor_fax', db.String(12)),
    db.Column('accident_reason', db.String(256)),
    db.Column('accident_reason_sub', db.String(48)),
    db.Column('date_renewed', db.DateTime),
    db.Column('ritei_status', db.String(50)),
    db.Column('ritei_start_date', db.DateTime),
    db.Column('order_no', db.String(18)),
    db.Column('arena_so_no', db.String(20)),
    db.Column('access_key', db.String(8)),
    db.Column('survery_appoint_date', db.DateTime),
    db.Column('survery_appoint_time', db.String(256)),
    db.Column('appoint_am_pm', db.String(256)),
    db.Column('dispatch_div', db.String(256)),
    db.Column('aldivert_flg', db.String(1)),
    db.Column('vcast_business_name', db.String(30)),
    db.Column('ftvdivertflg', db.String(1)),
    db.Column('repflg', db.String(1)),
    db.Column('repbusinessname', db.String(3)),
    db.Column('repdivertflg', db.String(1)),
    db.Column('repbusinessstartdate', db.DateTime),
    db.Column('repbusinessenddate', db.DateTime),
    db.Column('terminal_item_list', db.Text),
    db.Column('charge_list', db.Text),
    db.Column('contact_hope_time_kbn', db.String(2))
)


t_v_ntt_cor_dat = db.Table(
    'v_ntt_cor_dat',
    db.Column('ws_common_id', db.String(20)),
    db.Column('ws_common_renbn', db.String(2)),
    db.Column('contract_no', db.String(12)),
    db.Column('renew_date', db.DateTime),
    db.Column('create_date', db.DateTime),
    db.Column('operate_cd', db.String(128)),
    db.Column('c_flag', db.String(1)),
    db.Column('remark', db.String(80)),
    db.Column('apply_date', db.DateTime),
    db.Column('apply_kind', db.String(4)),
    db.Column('prog_status', db.String(2)),
    db.Column('send_plan_date', db.DateTime),
    db.Column('send_date', db.DateTime),
    db.Column('service_item', db.String(256)),
    db.Column('user_zip', db.String(7)),
    db.Column('user_addr', db.String(802)),
    db.Column('iten_plan_date', db.DateTime)
)


t_v_ntt_cor_phone_dtl_mst = db.Table(
    'v_ntt_cor_phone_dtl_mst',
    db.Column('ntt_plan_cd', db.String(5)),
    db.Column('ntt_call_type', db.String(4)),
    db.Column('bill_flag', db.String(1)),
    db.Column('selling_rate', db.Numeric(4, 2)),
    db.Column('bill_kbn_cd', db.String(2)),
    db.Column('create_date', db.DateTime),
    db.Column('renew_date', db.DateTime),
    db.Column('operate_cd', db.String(128))
)


t_v_ntt_cor_tmn_dat = db.Table(
    'v_ntt_cor_tmn_dat',
    db.Column('contract_no', db.String(12)),
    db.Column('renbn', db.String(3)),
    db.Column('terminal_name', db.String(128)),
    db.Column('install_date', db.DateTime),
    db.Column('renew_date', db.DateTime),
    db.Column('create_date', db.DateTime),
    db.Column('operate_cd', db.String(128)),
    db.Column('c_flag', db.String(1))
)


t_v_ntt_dat = db.Table(
    'v_ntt_dat',
    db.Column('ws_common_id', db.String(20)),
    db.Column('ws_common_renbn', db.String(2)),
    db.Column('contract_no', db.String(12)),
    db.Column('renew_date', db.DateTime),
    db.Column('create_date', db.DateTime),
    db.Column('operate_cd', db.String(128)),
    db.Column('c_flag', db.String(1)),
    db.Column('remark', db.String(80)),
    db.Column('apply_date', db.DateTime),
    db.Column('apply_kind', db.String(4)),
    db.Column('prog_status', db.String(2)),
    db.Column('send_plan_date', db.DateTime),
    db.Column('send_date', db.DateTime),
    db.Column('request_id', db.String(10)),
    db.Column('est_todohuken', db.String(20)),
    db.Column('apply_name', db.String(128)),
    db.Column('operator_name', db.String(128)),
    db.Column('work_plan_date', db.DateTime),
    db.Column('ntt_plan_date', db.DateTime),
    db.Column('ntt_plan_time', db.String(2)),
    db.Column('user_tel1', db.String(13)),
    db.Column('user_tel2', db.String(13)),
    db.Column('user_name', db.String(128)),
    db.Column('relation', db.String(20)),
    db.Column('origin_cd', db.String(2)),
    db.Column('note', db.String(256)),
    db.Column('cancel_flg', db.String(1)),
    db.Column('osm_end_plan_date', db.DateTime),
    db.Column('note2', db.String(16)),
    db.Column('result_cd', db.String(64)),
    db.Column('note3', db.String(256))
)


t_v_ntt_ew_mst = db.Table(
    'v_ntt_ew_mst',
    db.Column('telno_area', db.String(6)),
    db.Column('telno_pref', db.String(4)),
    db.Column('telno_suff', db.String(4)),
    db.Column('todofuken', db.String(8)),
    db.Column('ntt_ew_cd', db.String(1))
)


t_v_ntt_info = db.Table(
    'v_ntt_info',
    db.Column('contract_no', db.String(12)),
    db.Column('renew_date', db.DateTime),
    db.Column('create_date', db.DateTime),
    db.Column('operate_cd', db.String(128)),
    db.Column('c_flag', db.String(1)),
    db.Column('remark', db.String(80)),
    db.Column('entry_root_cd', db.String(1)),
    db.Column('method_cd', db.String(3)),
    db.Column('tran_mng_no', db.String(16)),
    db.Column('work_plan_date', db.DateTime),
    db.Column('work_plan_time', db.String(2)),
    db.Column('consal_plan_date', db.DateTime),
    db.Column('work_date_flg', db.String(1)),
    db.Column('telno', db.String(10)),
    db.Column('ntt_e_cont_id', db.String(16)),
    db.Column('cont_lastname', db.String(20)),
    db.Column('cont_firstname', db.String(20)),
    db.Column('cont_lastname_k', db.String(20)),
    db.Column('cont_firstname_k', db.String(20)),
    db.Column('apply_name', db.String(128)),
    db.Column('apply_name_k', db.String(256)),
    db.Column('apply_cd', db.String(1)),
    db.Column('contact_cd', db.String(1)),
    db.Column('telno2', db.String(11)),
    db.Column('email', db.String(50)),
    db.Column('a_cd', db.String(1)),
    db.Column('b_cd', db.String(1)),
    db.Column('c_cd', db.String(1)),
    db.Column('d_cd', db.String(1)),
    db.Column('note2', db.String(400)),
    db.Column('partner_cd', db.String(10)),
    db.Column('corp_name', db.String(60)),
    db.Column('corp_kana', db.String(60)),
    db.Column('corp_post_name', db.String(60)),
    db.Column('user_zip', db.String(7)),
    db.Column('user_todohuken', db.String(256)),
    db.Column('user_ku', db.String(256)),
    db.Column('user_area', db.String(256)),
    db.Column('user_chome', db.String(256)),
    db.Column('user_banchi', db.String(160)),
    db.Column('user_build_name', db.String(80)),
    db.Column('user_addr_note', db.String(200)),
    db.Column('send_zip', db.String(7)),
    db.Column('send_todohuken', db.String(256)),
    db.Column('send_ku', db.String(256)),
    db.Column('send_area', db.String(256)),
    db.Column('send_chome', db.String(256)),
    db.Column('send_banchi', db.String(160)),
    db.Column('send_build_name', db.String(80)),
    db.Column('send_addr_note', db.String(200)),
    db.Column('send_name', db.String(128)),
    db.Column('send_name_k', db.String(256)),
    db.Column('send_person', db.String(128)),
    db.Column('ntt_branch_name', db.String(64)),
    db.Column('ntt_position_name', db.String(128)),
    db.Column('ntt_sales_agency_cd', db.String(8)),
    db.Column('ntt_charge_name', db.String(128)),
    db.Column('ntt_charge_cd', db.String(8)),
    db.Column('ntt_charge_telno', db.String(13)),
    db.Column('ntt_charge_fax', db.String(13)),
    db.Column('ntt_charge_mail', db.String(60)),
    db.Column('ntt_isp_apply_kbn', db.String(20)),
    db.Column('ntt_service_name', db.String(64)),
    db.Column('ntt_bf_exist_type', db.String(4)),
    db.Column('ntt_isp_user_id', db.String(60)),
    db.Column('ntt_isp_mail', db.String(60)),
    db.Column('banpo_flg', db.String(1)),
    db.Column('double_contract_flag', db.String(64)),
    db.Column('name_admin_flag', db.String(64)),
    db.Column('cont_address_code', db.String(15)),
    db.Column('cont_address_revision', db.String(10)),
    db.Column('fax', db.String(13)),
    db.Column('address_code', db.String(11)),
    db.Column('partner_serial_no', db.String(16)),
    db.Column('user_banchi1', db.String(40)),
    db.Column('user_banchi2', db.String(20)),
    db.Column('user_banchi3', db.String(20)),
    db.Column('work_witness_name', db.String(20)),
    db.Column('work_witness_contact_cd', db.String(1)),
    db.Column('work_witness_telno', db.String(11)),
    db.Column('use_access_line', db.String(1)),
    db.Column('use_ntt_flets_service', db.String(3)),
    db.Column('other_companies_contract', db.String(1)),
    db.Column('other_companies_service', db.String(1)),
    db.Column('interior_wiring_cd', db.String(1)),
    db.Column('wiring_work_cd', db.String(1)),
    db.Column('tel_directory_carry_cd', db.String(1)),
    db.Column('vcast_contractor_sex_type', db.String(1)),
    db.Column('vcast_contractor_birth', db.DateTime),
    db.Column('connect_tv_const', db.String(1)),
    db.Column('tv_set_construct_type', db.String(1)),
    db.Column('cs_channel_pack1', db.String(1)),
    db.Column('cs_digital_tuner1', db.String(1)),
    db.Column('cs_channel_pack2', db.String(1)),
    db.Column('cs_digital_tuner2', db.String(1)),
    db.Column('cs_channel_pack3', db.String(1)),
    db.Column('cs_digital_tuner3', db.String(1)),
    db.Column('possession_cd', db.String(1)),
    db.Column('number_of_house', db.String(1)),
    db.Column('house_cd', db.String(1)),
    db.Column('work_witness_cd', db.String(1)),
    db.Column('ipv6connectmethod', db.String(64)),
    db.Column('adapterinfo', db.String(64)),
    db.Column('fm_possession_cd', db.String(1)),
    db.Column('ntt_birth', db.DateTime),
    db.Column('ntt_sex_type', db.String(1))
)


t_v_ntt_item_dat = db.Table(
    'v_ntt_item_dat',
    db.Column('contract_no', db.String(12)),
    db.Column('item_no', db.String(2)),
    db.Column('renew_date', db.DateTime),
    db.Column('create_date', db.DateTime),
    db.Column('operate_cd', db.String(128)),
    db.Column('c_flag', db.String(1)),
    db.Column('apply_flg', db.String(1))
)


t_v_ntt_item_mst = db.Table(
    'v_ntt_item_mst',
    db.Column('item_no', db.String(2)),
    db.Column('item_name', db.String(256)),
    db.Column('use_status', db.String(1)),
    db.Column('renew_date', db.DateTime),
    db.Column('create_date', db.DateTime),
    db.Column('operate_cd', db.String(128)),
    db.Column('c_flag', db.String(1))
)


t_v_ntt_osmdb = db.Table(
    'v_ntt_osmdb',
    db.Column('contract_no', db.String(12)),
    db.Column('isp_order_no', db.String(16)),
    db.Column('renew_date', db.DateTime),
    db.Column('create_date', db.DateTime),
    db.Column('operate_cd', db.String(128)),
    db.Column('c_flag', db.String(1)),
    db.Column('ntt_e_cont_id', db.String(16)),
    db.Column('apply_name', db.String(128)),
    db.Column('telno', db.String(14)),
    db.Column('osm_apply_date', db.DateTime),
    db.Column('item_name', db.String(128)),
    db.Column('item_detail_name', db.String(32)),
    db.Column('item_term_name', db.String(50)),
    db.Column('work_plan_date', db.DateTime),
    db.Column('work_plan_time', db.String(40)),
    db.Column('osm_entry_cd', db.String(10)),
    db.Column('osm_status', db.String(5)),
    db.Column('osm_sub_status', db.String(5)),
    db.Column('osm_start_date', db.DateTime),
    db.Column('osm_end_yyyymm', db.DateTime),
    db.Column('branch_name', db.String(20)),
    db.Column('mainte_plan', db.String(16)),
    db.Column('model_name', db.String(512)),
    db.Column('model_num', db.String(128)),
    db.Column('partner_cd', db.String(10)),
    db.Column('osm_create_date', db.DateTime),
    db.Column('branch_telno', db.String(14)),
    db.Column('consal_plan_date', db.DateTime),
    db.Column('ntt_e_agency_cd', db.String(8)),
    db.Column('sales_store_name', db.String(128)),
    db.Column('section_name', db.String(128)),
    db.Column('charge_cd', db.String(8)),
    db.Column('charge_name', db.String(128)),
    db.Column('osm_renew_date', db.DateTime),
    db.Column('change_item_name', db.String(128)),
    db.Column('application_no', db.String(16)),
    db.Column('ntt_e_cont_start_date', db.DateTime),
    db.Column('outside_bill_start_date', db.DateTime),
    db.Column('inside_bill_start_date', db.DateTime),
    db.Column('outside_work_plan_date', db.DateTime),
    db.Column('inside_work_plan_date', db.DateTime),
    db.Column('accident_reason', db.String(256)),
    db.Column('accident_status', db.String(256)),
    db.Column('cancel_reason', db.String(256)),
    db.Column('mainte_info', db.String(128)),
    db.Column('campaign', db.String(64)),
    db.Column('bill_end_date', db.DateTime),
    db.Column('end_reason', db.String(256)),
    db.Column('osa_set_cd', db.String(2)),
    db.Column('osa_cancel_cd', db.String(256)),
    db.Column('change_item_detail_name', db.String(32)),
    db.Column('change_id_no', db.String(64)),
    db.Column('hgw_mainte_info', db.String(32)),
    db.Column('hgw_model_name', db.String(128)),
    db.Column('item_change_bill_date', db.DateTime),
    db.Column('mng_id', db.String(25)),
    db.Column('cp_start_date', db.DateTime),
    db.Column('cp_end_date', db.DateTime),
    db.Column('bill_start_date', db.DateTime),
    db.Column('consal_status', db.String(50)),
    db.Column('osm_flg', db.String(1)),
    db.Column('osm2_start_date', db.DateTime),
    db.Column('osm2_end_yyyymm', db.DateTime)
)


t_v_ntt_partner_mst = db.Table(
    'v_ntt_partner_mst',
    db.Column('plan_cd', db.String(8)),
    db.Column('partner_cd', db.String(10)),
    db.Column('status', db.String(1))
)


t_v_ntt_result = db.Table(
    'v_ntt_result',
    db.Column('dmdto_id', db.String(12)),
    db.Column('ntt_result_cre_date', db.DateTime),
    db.Column('create_date', db.DateTime),
    db.Column('renew_date', db.DateTime),
    db.Column('operate_cd', db.String(128)),
    db.Column('dmd_no', db.String(13)),
    db.Column('result_kind', db.String(1)),
    db.Column('result_cd', db.String(11)),
    db.Column('ntt_apply_date', db.DateTime)
)


t_v_nttf_result_mng = db.Table(
    'v_nttf_result_mng',
    db.Column('import_date', db.String(14)),
    db.Column('line_no', db.Numeric(6, 0)),
    db.Column('create_date', db.DateTime),
    db.Column('renew_date', db.DateTime),
    db.Column('operate_cd', db.String(128)),
    db.Column('collection_kbn', db.String(1)),
    db.Column('result_reflect_kbn', db.String(1)),
    db.Column('dmd_no', db.String(13)),
    db.Column('dmdto_id', db.String(12)),
    db.Column('result_flag', db.String(2)),
    db.Column('cvs_flag', db.String(1)),
    db.Column('payment_date', db.DateTime),
    db.Column('member_id', db.String(12)),
    db.Column('chg_dmdto_valid_date', db.DateTime),
    db.Column('chg_dmd_kbn_flag', db.String(1)),
    db.Column('ng_rsn', db.String(3)),
    db.Column('dmd_status', db.String(2)),
    db.Column('pay_chg_rsn', db.String(2)),
    db.Column('incident_conf_key', db.String(15)),
    db.Column('mail_send_key', db.String(32)),
    db.Column('document_id', db.String(32)),
    db.Column('use_month', db.String(30)),
    db.Column('err_proc_status', db.String(1)),
    db.Column('demand_mny', db.Numeric(10, 0))
)


t_v_nttplayer_cont = db.Table(
    'v_nttplayer_cont',
    db.Column('contract_no', db.String(12)),
    db.Column('isp_order_no', db.String(20)),
    db.Column('renew_date', db.DateTime),
    db.Column('create_date', db.DateTime),
    db.Column('operate_cd', db.String(128)),
    db.Column('c_flag', db.String(1)),
    db.Column('service_name', db.String(40)),
    db.Column('item_name', db.String(128)),
    db.Column('order_status', db.String(40)),
    db.Column('work_plan_date', db.DateTime),
    db.Column('ntt_e_cont_id_pr', db.String(13)),
    db.Column('item_term_name', db.String(1536)),
    db.Column('apply_kbn', db.String(40)),
    db.Column('ntt_e_cont_id', db.String(13)),
    db.Column('divert_consent_no', db.String(11)),
    db.Column('ntt_ew_kind', db.String(40)),
    db.Column('nttplayer_cont_id', db.String(12)),
    db.Column('user_name', db.String(240)),
    db.Column('user_name_k', db.String(480)),
    db.Column('user_address', db.String(2142)),
    db.Column('isp_name', db.String(60)),
    db.Column('isp_status', db.String(2)),
    db.Column('nttplayer_start_end_date', db.DateTime),
    db.Column('isp_start_end_date', db.DateTime),
    db.Column('nttplayer_cont_name', db.String(60)),
    db.Column('nttplayer_cont_name_k', db.String(100)),
    db.Column('nttplayer_cont_telno', db.String(72)),
    db.Column('nttplayer_cont_telno2', db.String(11)),
    db.Column('nttplayer_cont_zip', db.String(7)),
    db.Column('nttplayer_cont_address', db.String(200)),
    db.Column('nttplayer_cont_birth', db.DateTime),
    db.Column('penalty_cost_flag', db.String(2)),
    db.Column('flets_cont_name', db.String(480)),
    db.Column('flets_cont_telno', db.String(72))
)


t_v_nttplayer_dat = db.Table(
    'v_nttplayer_dat',
    db.Column('ws_common_id', db.String(20)),
    db.Column('ws_common_renbn', db.String(2)),
    db.Column('contract_no', db.String(12)),
    db.Column('renew_date', db.DateTime),
    db.Column('create_date', db.DateTime),
    db.Column('operate_cd', db.String(128)),
    db.Column('c_flag', db.String(1)),
    db.Column('remark', db.String(80)),
    db.Column('apply_date', db.DateTime),
    db.Column('apply_kind', db.String(4)),
    db.Column('prog_status', db.String(2)),
    db.Column('send_plan_date', db.DateTime),
    db.Column('send_date', db.DateTime),
    db.Column('nttplayer_order_no', db.String(17)),
    db.Column('isp_receipt_result', db.String(2)),
    db.Column('isp_receipt_err_cd', db.String(2)),
    db.Column('isp_receipt_err_reason', db.String(1536)),
    db.Column('isp_service_order_status', db.String(2)),
    db.Column('stop_reason', db.String(1536)),
    db.Column('isp_biko', db.String(2)),
    db.Column('isp_confirm_date', db.DateTime)
)


t_v_old_isp_mst = db.Table(
    'v_old_isp_mst',
    db.Column('old_isp', db.String(3)),
    db.Column('renew_date', db.DateTime),
    db.Column('create_date', db.DateTime),
    db.Column('operate_cd', db.String(128)),
    db.Column('old_isp_name', db.String(80)),
    db.Column('old_isp_name_fe', db.String(40))
)


t_v_operator_auth_mst = db.Table(
    'v_operator_auth_mst',
    db.Column('task', db.String(128)),
    db.Column('auth', db.String(128))
)


t_v_operator_mst = db.Table(
    'v_operator_mst',
    db.Column('operator_cd', db.String(128)),
    db.Column('operator_pass', db.String(16)),
    db.Column('auth_time', db.Numeric(3, 0)),
    db.Column('pass_enddate', db.DateTime),
    db.Column('ope_status', db.String(1)),
    db.Column('create_date', db.DateTime),
    db.Column('renew_date', db.DateTime),
    db.Column('operate_cd', db.String(128))
)


t_v_operator_task_mst = db.Table(
    'v_operator_task_mst',
    db.Column('operator_cd', db.String(128)),
    db.Column('task', db.String(128))
)


t_v_opt_plan_rel_mst = db.Table(
    'v_opt_plan_rel_mst',
    db.Column('opt_plan_cd', db.String(8)),
    db.Column('rel_opt_plan_cd', db.String(8)),
    db.Column('rel_opt_flag', db.String(1)),
    db.Column('create_date', db.DateTime),
    db.Column('renew_date', db.DateTime),
    db.Column('operate_cd', db.String(128)),
    db.Column('c_flag', db.String(1))
)


t_v_plan_chg_mst = db.Table(
    'v_plan_chg_mst',
    db.Column('src_plan_cd', db.String(8)),
    db.Column('dst_plan_cd', db.String(8)),
    db.Column('rel_flag', db.String(1)),
    db.Column('disc_cd1', db.String(1)),
    db.Column('disc_cd2', db.String(3)),
    db.Column('disc_cd3', db.String(3)),
    db.Column('disc_cd4', db.String(3)),
    db.Column('disc_cd5', db.String(3)),
    db.Column('disc_cd6', db.String(3)),
    db.Column('disc_cd7', db.String(3)),
    db.Column('disc_cd8', db.String(3)),
    db.Column('create_date', db.DateTime),
    db.Column('renew_date', db.DateTime),
    db.Column('operate_cd', db.String(128)),
    db.Column('c_flag', db.String(1))
)


t_v_plan_mst = db.Table(
    'v_plan_mst',
    db.Column('plan_cd', db.String(8)),
    db.Column('plan_name', db.String(128)),
    db.Column('plan_short', db.String(128)),
    db.Column('plan_kind', db.String(1)),
    db.Column('plan_status', db.String(1)),
    db.Column('initial_cost', db.Numeric(8, 0)),
    db.Column('first_service_cost', db.Numeric(8, 0)),
    db.Column('service_cost', db.Numeric(8, 0)),
    db.Column('work_cost', db.Numeric(8, 0)),
    db.Column('taxfree_kbn', db.String(1)),
    db.Column('dialup', db.String(4)),
    db.Column('roaming', db.String(4)),
    db.Column('mobilepoint', db.String(4)),
    db.Column('service_dmt_name', db.String(128)),
    db.Column('disc_mail_n', db.Numeric(2, 0)),
    db.Column('disc_cd_mail', db.String(3)),
    db.Column('disc_cd_homepage', db.String(3)),
    db.Column('plan_term', db.Numeric(2, 0)),
    db.Column('create_date', db.DateTime),
    db.Column('renew_date', db.DateTime),
    db.Column('operate_cd', db.String(128)),
    db.Column('c_flag', db.String(1)),
    db.Column('penalty_cost', db.Numeric(8, 0)),
    db.Column('max_penalty_month', db.Numeric(2, 0)),
    db.Column('service_cycle_month', db.Numeric(2, 0)),
    db.Column('creditor_cd', db.String(1)),
    db.Column('creditor_subcd', db.String(3)),
    db.Column('penalty_taxfree_kbn', db.String(1)),
    db.Column('volume_discount_cd', db.String(2)),
    db.Column('append_penalty_cost', db.Numeric(8, 0)),
    db.Column('stat_initial_cost', db.Numeric(8, 0)),
    db.Column('stat_service_cost', db.Numeric(8, 0)),
    db.Column('aplus_initial_cost', db.Numeric(8, 0))
)


t_v_plan_rel_mst = db.Table(
    'v_plan_rel_mst',
    db.Column('plan_cd', db.String(8)),
    db.Column('rel_plan_cd', db.String(8)),
    db.Column('rel_flag', db.String(1)),
    db.Column('create_date', db.DateTime),
    db.Column('renew_date', db.DateTime),
    db.Column('operate_cd', db.String(128)),
    db.Column('c_flag', db.String(1))
)


t_v_ppp_info = db.Table(
    'v_ppp_info',
    db.Column('account_id', db.String(64)),
    db.Column('bill_kbn_cd', db.String(2)),
    db.Column('used_month', db.Date),
    db.Column('bill_month', db.Date),
    db.Column('use_minute', db.Numeric(7, 0)),
    db.Column('use_day', db.Numeric(2, 0)),
    db.Column('create_date', db.DateTime),
    db.Column('renew_date', db.DateTime),
    db.Column('operate_cd', db.String(128)),
    db.Column('c_flag', db.String(1))
)


t_v_prefix_dat = db.Table(
    'v_prefix_dat',
    db.Column('ws_common_id', db.String(20)),
    db.Column('ws_common_renbn', db.String(2)),
    db.Column('opt_contract_no', db.Numeric(10, 0)),
    db.Column('process_kbn', db.String(6)),
    db.Column('msisdn', db.String(11)),
    db.Column('contbase_no', db.String(10)),
    db.Column('exec_plan', db.String(1)),
    db.Column('prefix_cd', db.String(20)),
    db.Column('apply_kind', db.String(4)),
    db.Column('prog_status', db.String(2)),
    db.Column('send_plan_date', db.DateTime),
    db.Column('send_date', db.DateTime),
    db.Column('result_cd', db.String(2)),
    db.Column('result_status', db.String(2)),
    db.Column('create_date', db.DateTime),
    db.Column('renew_date', db.DateTime),
    db.Column('operate_cd', db.String(128)),
    db.Column('c_flag', db.String(1))
)


t_v_privilege = db.Table(
    'v_privilege',
    db.Column('customer_id', db.String(8)),
    db.Column('grant_date', db.DateTime),
    db.Column('stage', db.String(1)),
    db.Column('used', db.String(1)),
    db.Column('unchanged', db.String(1)),
    db.Column('create_date', db.DateTime),
    db.Column('renew_date', db.DateTime),
    db.Column('operate_cd', db.String(128))
)


t_v_pt2code_mst = db.Table(
    'v_pt2code_mst',
    db.Column('pt2_plancd', db.String(32)),
    db.Column('quota_size', db.Numeric(10, 0)),
    db.Column('quota_carryforward_kbn', db.String(1)),
    db.Column('apn', db.String(50)),
    db.Column('monthly_charge_kbn', db.String(1)),
    db.Column('create_date', db.DateTime),
    db.Column('renew_date', db.DateTime),
    db.Column('operate_cd', db.String(128))
)


t_v_sales_customer_total = db.Table(
    'v_sales_customer_total',
    db.Column('sales_month', db.String(6)),
    db.Column('customer_id', db.String(8)),
    db.Column('creditor_cd', db.String(1)),
    db.Column('creditor_subcd', db.String(3)),
    db.Column('taxable_total', db.Numeric(10, 0)),
    db.Column('taxfree_total', db.Numeric(10, 0)),
    db.Column('tax_total', db.Numeric(10, 0)),
    db.Column('tax_percent', db.Numeric(4, 1))
)


t_v_sales_detail = db.Table(
    'v_sales_detail',
    db.Column('dmd_no', db.String(13)),
    db.Column('dmd_detailno', db.Numeric(5, 0)),
    db.Column('customer_id', db.String(8)),
    db.Column('contract_no', db.String(12)),
    db.Column('opt_contract_no', db.Numeric(10, 0)),
    db.Column('plan_cd', db.String(8)),
    db.Column('disc_type', db.String(2)),
    db.Column('disc_cd', db.String(3)),
    db.Column('bill_kbn_cd', db.String(2)),
    db.Column('plan_content', db.String(160)),
    db.Column('quantity', db.Numeric(19, 0)),
    db.Column('unit', db.String(10)),
    db.Column('unit_cost', db.Numeric(10, 4)),
    db.Column('tax_cost', db.Numeric(9, 0)),
    db.Column('account_id', db.String(64)),
    db.Column('detail_kbn', db.String(1)),
    db.Column('adjust_renban', db.Numeric(9, 0)),
    db.Column('cost', db.Numeric(9, 0)),
    db.Column('taxfree_kbn', db.String(1)),
    db.Column('kihon_tuika_kbn', db.String(1)),
    db.Column('create_date', db.DateTime),
    db.Column('renew_date', db.DateTime),
    db.Column('operate_cd', db.String(128)),
    db.Column('c_flag', db.String(1)),
    db.Column('creditor_cd', db.String(1)),
    db.Column('kddi_plan_cd', db.String(10)),
    db.Column('ntt_plan_cd', db.String(10)),
    db.Column('creditor_subcd', db.String(3)),
    db.Column('sales_dmd_kbn', db.String(1)),
    db.Column('demand_count', db.Numeric(2, 0)),
    db.Column('jpayment_trade_no', db.String(64)),
    db.Column('bill_start', db.DateTime),
    db.Column('bill_end', db.DateTime),
    db.Column('tax_percent', db.Numeric(4, 1))
)


t_v_sales_dmdto_total = db.Table(
    'v_sales_dmdto_total',
    db.Column('dmd_no', db.String(13)),
    db.Column('creditor_cd', db.String(1)),
    db.Column('creditor_subcd', db.String(3)),
    db.Column('taxable_total', db.Numeric(10, 0)),
    db.Column('taxfree_total', db.Numeric(10, 0)),
    db.Column('tax_total', db.Numeric(10, 0)),
    db.Column('tax_percent', db.Numeric(4, 1))
)


t_v_sales_header = db.Table(
    'v_sales_header',
    db.Column('dmd_no', db.String(13)),
    db.Column('sales_month', db.String(6)),
    db.Column('dmdto_id', db.String(12)),
    db.Column('slip_kbn', db.String(1)),
    db.Column('dmd_no2', db.String(13)),
    db.Column('slip_reason', db.String(2))
)


t_v_sales_shift_detail = db.Table(
    'v_sales_shift_detail',
    db.Column('create_date', db.DateTime),
    db.Column('renew_date', db.DateTime),
    db.Column('operate_cd', db.String(128)),
    db.Column('c_flag', db.String(1)),
    db.Column('org_dmd_month', db.Date),
    db.Column('plan_dmd_month', db.Date),
    db.Column('dmdto_id', db.String(12)),
    db.Column('customer_id', db.String(8)),
    db.Column('contract_no', db.String(12)),
    db.Column('bill_detailno', db.Numeric(5, 0)),
    db.Column('opt_contract_no', db.Numeric(10, 0)),
    db.Column('plan_cd', db.String(8)),
    db.Column('disc_type', db.String(2)),
    db.Column('disc_cd', db.String(3)),
    db.Column('bill_kbn_cd', db.String(2)),
    db.Column('bill_start', db.DateTime),
    db.Column('bill_end', db.DateTime),
    db.Column('quantity', db.Numeric(19, 0)),
    db.Column('unit', db.String(10)),
    db.Column('unit_cost', db.Numeric(10, 4)),
    db.Column('tax_cost', db.Numeric(9, 0)),
    db.Column('account_id', db.String(64)),
    db.Column('adjust_renban', db.Numeric(9, 0)),
    db.Column('cost', db.Numeric(9, 0)),
    db.Column('taxfree_kbn', db.String(1)),
    db.Column('kihon_tuika_kbn', db.String(1)),
    db.Column('kddi_plan_cd', db.String(10)),
    db.Column('plan_name', db.String(128)),
    db.Column('creditor_cd', db.String(1)),
    db.Column('ntt_plan_cd', db.String(10)),
    db.Column('creditor_subcd', db.String(3)),
    db.Column('tax_percent', db.Numeric(4, 1))
)


t_v_sales_shift_total = db.Table(
    'v_sales_shift_total',
    db.Column('create_date', db.DateTime),
    db.Column('renew_date', db.DateTime),
    db.Column('operate_cd', db.String(128)),
    db.Column('c_flag', db.String(1)),
    db.Column('contract_no', db.String(12)),
    db.Column('used_month', db.Date),
    db.Column('org_dmd_month', db.Date),
    db.Column('plan_dmd_month', db.Date),
    db.Column('dmdto_id', db.String(12)),
    db.Column('kddi_taxable_total', db.Numeric(10, 0)),
    db.Column('kddi_taxfree_total', db.Numeric(10, 0)),
    db.Column('kddi_tax', db.Numeric(10, 0)),
    db.Column('collection_taxable_total', db.Numeric(10, 0)),
    db.Column('collection_taxin_total', db.Numeric(10, 0)),
    db.Column('ntt_e_taxable_total', db.Numeric(10, 0)),
    db.Column('ntt_e_taxfree_total', db.Numeric(10, 0)),
    db.Column('ntt_e_tax_total', db.Numeric(10, 0)),
    db.Column('ntt_w_taxable_total', db.Numeric(10, 0)),
    db.Column('ntt_w_taxfree_total', db.Numeric(10, 0)),
    db.Column('ntt_w_tax_total', db.Numeric(10, 0))
)


t_v_sales_total = db.Table(
    'v_sales_total',
    db.Column('dmd_no', db.String(13)),
    db.Column('dmd_month', db.String(6)),
    db.Column('dmdto_id', db.String(12)),
    db.Column('taxable_total', db.Numeric(10, 0)),
    db.Column('taxfree_total', db.Numeric(10, 0)),
    db.Column('tax', db.Numeric(10, 0)),
    db.Column('all_total', db.Numeric(10, 0)),
    db.Column('slip_kbn', db.String(1)),
    db.Column('dmd_no2', db.String(13)),
    db.Column('dmd_status', db.String(2)),
    db.Column('demand_kbn', db.String(2)),
    db.Column('payment_kbn', db.String(2)),
    db.Column('payment_date', db.DateTime),
    db.Column('result_cd', db.String(2)),
    db.Column('receipt_sts', db.String(1)),
    db.Column('all_receive_mny', db.Numeric(10, 0)),
    db.Column('receive_mny', db.Numeric(10, 0)),
    db.Column('deficiency', db.Numeric(10, 0)),
    db.Column('detail_kbn', db.String(2)),
    db.Column('detail_rsn', db.String(255)),
    db.Column('pwd_demandprint_kbn', db.String(1)),
    db.Column('cardkind', db.String(2)),
    db.Column('cardno', db.String(16)),
    db.Column('cardvalid', db.String(6)),
    db.Column('verify_no', db.String(8)),
    db.Column('verify_money', db.Numeric(8, 0)),
    db.Column('verify_date', db.DateTime),
    db.Column('agreement', db.String(1)),
    db.Column('pwd_stro_cd', db.String(1)),
    db.Column('trans_bankcd', db.String(4)),
    db.Column('trans_branchcd', db.String(3)),
    db.Column('trans_linecd', db.String(1)),
    db.Column('trans_acckind', db.String(1)),
    db.Column('trans_accno', db.String(7)),
    db.Column('trans_accname', db.String(60)),
    db.Column('kobetu_bankcd', db.String(4)),
    db.Column('kobetu_branchcd', db.String(3)),
    db.Column('kobetu_linecd', db.String(1)),
    db.Column('kobetu_acckind', db.String(1)),
    db.Column('kobetu_accno', db.String(7)),
    db.Column('kobetu_accname', db.String(60)),
    db.Column('dmdto_memo', db.String(128)),
    db.Column('payment_memo', db.String(64)),
    db.Column('slip_reason', db.String(2)),
    db.Column('create_date', db.DateTime),
    db.Column('renew_date', db.DateTime),
    db.Column('operate_cd', db.String(128)),
    db.Column('c_flag', db.String(1)),
    db.Column('kddi_taxable_total', db.Numeric(10, 0)),
    db.Column('kddi_taxfree_total', db.Numeric(10, 0)),
    db.Column('kddi_tax', db.Numeric(10, 0)),
    db.Column('collection_taxable_total', db.Numeric(10, 0)),
    db.Column('collection_taxin_total', db.Numeric(10, 0)),
    db.Column('ntt_e_taxable_total', db.Numeric(10, 0)),
    db.Column('ntt_e_taxfree_total', db.Numeric(10, 0)),
    db.Column('ntt_e_tax_total', db.Numeric(10, 0)),
    db.Column('ntt_limit_date', db.DateTime),
    db.Column('ntt_w_taxable_total', db.Numeric(10, 0)),
    db.Column('ntt_w_taxfree_total', db.Numeric(10, 0)),
    db.Column('ntt_w_tax_total', db.Numeric(10, 0)),
    db.Column('cvs_service_stop_plan', db.DateTime),
    db.Column('cvs_change_date', db.DateTime),
    db.Column('cvs_payment_mny', db.Numeric(10, 0)),
    db.Column('cvs_payment_date', db.DateTime),
    db.Column('cvs_payment_cancel_date', db.DateTime),
    db.Column('other_taxable_total', db.Numeric(10, 0)),
    db.Column('other_taxfree_total', db.Numeric(10, 0)),
    db.Column('other_tax_total', db.Numeric(10, 0)),
    db.Column('use_aim', db.Numeric(1, 0)),
    db.Column('ec_receipt_no', db.String(22)),
    db.Column('stat_kbn', db.Numeric(1, 0))
)


t_v_sales_total_df_cooperation = db.Table(
    'v_sales_total_df_cooperation',
    db.Column('dmd_no', db.String(13)),
    db.Column('dmd_month', db.String(6)),
    db.Column('dmdto_id', db.String(12)),
    db.Column('cst_no', db.String(20)),
    db.Column('all_total', db.Numeric(10, 0)),
    db.Column('dmd_status', db.String(2)),
    db.Column('result_cd', db.String(2)),
    db.Column('payment_date', db.DateTime),
    db.Column('receive_mny', db.Numeric(10, 0)),
    db.Column('cust_user_type', db.String(1)),
    db.Column('cardno', db.String(16)),
    db.Column('trans_bankcd', db.String(4)),
    db.Column('trans_branchcd', db.String(3)),
    db.Column('trans_linecd', db.String(1)),
    db.Column('trans_acckind', db.String(1)),
    db.Column('trans_accno', db.String(7)),
    db.Column('trans_accname', db.String(60)),
    db.Column('dfsend_amount', db.Numeric(10, 0)),
    db.Column('dtrgetamn_before', db.Numeric(10, 0)),
    db.Column('create_date', db.DateTime),
    db.Column('renew_date', db.DateTime),
    db.Column('operate_cd', db.String(128))
)


t_v_sales_total_df_ng_wk = db.Table(
    'v_sales_total_df_ng_wk',
    db.Column('dmd_no', db.String(13)),
    db.Column('dmd_month', db.String(6)),
    db.Column('dmdto_id', db.String(12)),
    db.Column('cst_no', db.String(20)),
    db.Column('all_total', db.Numeric(10, 0)),
    db.Column('dmd_status', db.String(2)),
    db.Column('send_kbn', db.String(2)),
    db.Column('result_cd', db.String(2)),
    db.Column('payment_date', db.DateTime),
    db.Column('cust_user_type', db.String(1)),
    db.Column('cardno', db.String(16)),
    db.Column('trans_bankcd', db.String(4)),
    db.Column('trans_branchcd', db.String(3)),
    db.Column('trans_linecd', db.String(1)),
    db.Column('trans_acckind', db.String(1)),
    db.Column('trans_accno', db.String(7)),
    db.Column('trans_accname', db.String(60)),
    db.Column('new_cd', db.String(1)),
    db.Column('statuscd', db.String(1)),
    db.Column('description', db.String(100)),
    db.Column('dtrgetamn_before', db.Numeric(10, 0)),
    db.Column('create_date', db.DateTime),
    db.Column('renew_date', db.DateTime),
    db.Column('operate_cd', db.String(128))
)


t_v_sales_total_df_wk = db.Table(
    'v_sales_total_df_wk',
    db.Column('dmd_no', db.String(13)),
    db.Column('dmd_month', db.String(6)),
    db.Column('dmdto_id', db.String(12)),
    db.Column('cst_no', db.String(20)),
    db.Column('all_total', db.Numeric(10, 0)),
    db.Column('dmd_status', db.String(2)),
    db.Column('send_kbn', db.String(2)),
    db.Column('result_cd', db.String(2)),
    db.Column('payment_date', db.DateTime),
    db.Column('cust_user_type', db.String(1)),
    db.Column('cardno', db.String(16)),
    db.Column('trans_bankcd', db.String(4)),
    db.Column('trans_branchcd', db.String(3)),
    db.Column('trans_linecd', db.String(1)),
    db.Column('trans_acckind', db.String(1)),
    db.Column('trans_accno', db.String(7)),
    db.Column('trans_accname', db.String(60)),
    db.Column('new_cd', db.String(1)),
    db.Column('statuscd', db.String(1)),
    db.Column('description', db.String(100)),
    db.Column('dtrgetamn_before', db.Numeric(10, 0)),
    db.Column('create_date', db.DateTime),
    db.Column('renew_date', db.DateTime),
    db.Column('operate_cd', db.String(128))
)


t_v_service = db.Table(
    'v_service',
    db.Column('contbase_no', db.String(10)),
    db.Column('idkind_no', db.String(1)),
    db.Column('account_id', db.String(64)),
    db.Column('initial_pass', db.String(16)),
    db.Column('create_date', db.DateTime),
    db.Column('renew_date', db.DateTime),
    db.Column('operate_cd', db.String(128)),
    db.Column('c_flag', db.String(1)),
    db.Column('telno', db.String(11))
)


t_v_sim_dat = db.Table(
    'v_sim_dat',
    db.Column('ws_common_id', db.String(20)),
    db.Column('ws_common_renbn', db.String(2)),
    db.Column('contract_no', db.String(12)),
    db.Column('opt_contract_no', db.Numeric(10, 0)),
    db.Column('isp_order_no', db.String(20)),
    db.Column('renew_date', db.DateTime),
    db.Column('create_date', db.DateTime),
    db.Column('operate_cd', db.String(128)),
    db.Column('c_flag', db.String(1)),
    db.Column('remark', db.String(80)),
    db.Column('apply_date', db.DateTime),
    db.Column('apply_kind', db.String(4)),
    db.Column('prog_status', db.String(2)),
    db.Column('send_plan_date', db.DateTime),
    db.Column('send_date', db.DateTime),
    db.Column('sim_status', db.String(1)),
    db.Column('imei', db.String(15)),
    db.Column('iccid', db.String(19)),
    db.Column('msisdn', db.String(11)),
    db.Column('send_name', db.String(120)),
    db.Column('send_name_k', db.String(240)),
    db.Column('send_zip', db.String(7)),
    db.Column('send_todohuken', db.String(8)),
    db.Column('send_addr1', db.String(100)),
    db.Column('send_addr2', db.String(100)),
    db.Column('send_build_name', db.String(80)),
    db.Column('send_telno', db.String(11)),
    db.Column('arrival_plan_date', db.DateTime),
    db.Column('arrival_plan_time', db.String(1)),
    db.Column('ship_no', db.String(20)),
    db.Column('direct_date', db.DateTime),
    db.Column('ship_decision_date', db.DateTime),
    db.Column('ship_comp_date', db.DateTime),
    db.Column('send_status', db.String(2)),
    db.Column('item_cd', db.String(10)),
    db.Column('return_limit_date', db.DateTime),
    db.Column('return_flg', db.String(1)),
    db.Column('return_date', db.DateTime),
    db.Column('return_kit_reg_date', db.DateTime),
    db.Column('return_send_date', db.DateTime),
    db.Column('org_ws_common_id', db.String(20)),
    db.Column('sim_acct_stop_date', db.DateTime),
    db.Column('lost_opt_contract_no', db.Numeric(10, 0)),
    db.Column('cont_sex', db.String(1)),
    db.Column('cont_birth', db.DateTime),
    db.Column('mnp_number', db.String(10)),
    db.Column('mnp_telno', db.String(11)),
    db.Column('mnp_reserve_date', db.DateTime),
    db.Column('mnp_line_lastname_k', db.String(80)),
    db.Column('mnp_line_firstname_k', db.String(40)),
    db.Column('mnp_line_lastname', db.String(40)),
    db.Column('mnp_line_firstname', db.String(20)),
    db.Column('mnp_line_birth', db.DateTime),
    db.Column('portable_tel_flg', db.String(1)),
    db.Column('send_name_lastname', db.String(60)),
    db.Column('send_name_firstname', db.String(60)),
    db.Column('send_name_lastname_k', db.String(120)),
    db.Column('send_name_firstname_k', db.String(120)),
    db.Column('mnp_out_number', db.String(10)),
    db.Column('mnp_out_status', db.String(1)),
    db.Column('mnp_out_apply_date', db.DateTime),
    db.Column('mnp_out_order_date', db.DateTime),
    db.Column('mnp_out_order_comp_date', db.DateTime),
    db.Column('mnp_out_expire_date', db.DateTime),
    db.Column('mnp_out_end_date', db.DateTime),
    db.Column('mnp_out_line_lastname_k', db.String(80)),
    db.Column('mnp_out_line_firstname_k', db.String(40)),
    db.Column('mnp_out_line_lastname', db.String(40)),
    db.Column('mnp_out_line_firstname', db.String(20)),
    db.Column('mnp_out_line_birth', db.DateTime),
    db.Column('charge_count', db.Numeric(10, 0)),
    db.Column('charge_mb', db.Numeric(10, 0)),
    db.Column('charge_date', db.DateTime),
    db.Column('quota_code', db.String(128)),
    db.Column('semiblack_add_status', db.String(1)),
    db.Column('semiblack_add_reserve_date', db.DateTime),
    db.Column('semiblack_add_apply_date', db.DateTime),
    db.Column('semiblack_add_comp_date', db.DateTime),
    db.Column('semiblack_add_error_msg', db.String(100)),
    db.Column('quota_carryover_mb', db.Numeric(10, 0)),
    db.Column('quota_carryover_date', db.DateTime),
    db.Column('rent_device_cd', db.String(20)),
    db.Column('rent_lost_opt_contract_no', db.Numeric(10, 0)),
    db.Column('rent_return_limit_date', db.DateTime),
    db.Column('rent_return_flg', db.String(1)),
    db.Column('rent_return_date', db.DateTime)
)


t_v_sp_call_log = db.Table(
    'v_sp_call_log',
    db.Column('log_date', db.String(8)),
    db.Column('line_no', db.Numeric(7, 0)),
    db.Column('cc_account_id', db.Numeric(19, 0)),
    db.Column('contbase_no', db.String(10)),
    db.Column('call_start_time', db.DateTime),
    db.Column('call_second', db.Numeric(19, 0)),
    db.Column('telno', db.String(16)),
    db.Column('partner_telno', db.String(16)),
    db.Column('call_type', db.String(16)),
    db.Column('oem_charge', db.Numeric(6, 0)),
    db.Column('user_charge', db.Numeric(6, 0)),
    db.Column('tarrif_code', db.String(128)),
    db.Column('tarrif_type', db.String(2)),
    db.Column('create_date', db.DateTime),
    db.Column('renew_date', db.DateTime),
    db.Column('operate_cd', db.String(128)),
    db.Column('discount_charge', db.Numeric(6, 0)),
    db.Column('org_call_second', db.Numeric(19, 0)),
    db.Column('org_user_charge', db.Numeric(6, 0))
)


t_v_sp_call_log_mng = db.Table(
    'v_sp_call_log_mng',
    db.Column('error_log_date', db.String(8)),
    db.Column('create_date', db.DateTime),
    db.Column('renew_date', db.DateTime),
    db.Column('operate_cd', db.String(128))
)


t_v_stockholder_cd_mst = db.Table(
    'v_stockholder_cd_mst',
    db.Column('stockholder_cd', db.String(10)),
    db.Column('start_date', db.DateTime),
    db.Column('end_date', db.DateTime)
)


t_v_string = db.Table(
    'v_string',
    db.Column('nvl', db.Text)
)


t_v_tepco_dat = db.Table(
    'v_tepco_dat',
    db.Column('ws_common_id', db.String(20)),
    db.Column('ws_common_renbn', db.String(2)),
    db.Column('contract_no', db.String(12)),
    db.Column('isp_order_no', db.String(20)),
    db.Column('apply_date', db.DateTime),
    db.Column('send_plan_date', db.DateTime),
    db.Column('send_date', db.DateTime),
    db.Column('apply_kind', db.String(4)),
    db.Column('prog_status', db.String(2)),
    db.Column('syori_kind', db.String(2)),
    db.Column('syori_status', db.String(1)),
    db.Column('username', db.String(32)),
    db.Column('domainname', db.String(32)),
    db.Column('tpc_no', db.String(14)),
    db.Column('user_cd', db.String(1)),
    db.Column('zip', db.String(8)),
    db.Column('todohuken', db.String(8)),
    db.Column('gun', db.String(20)),
    db.Column('ku', db.String(20)),
    db.Column('area', db.String(40)),
    db.Column('chome', db.String(10)),
    db.Column('banchi', db.String(20)),
    db.Column('build_name', db.String(80)),
    db.Column('telno', db.String(13)),
    db.Column('toi_telno', db.String(13)),
    db.Column('email', db.String(80)),
    db.Column('house_cd1', db.String(1)),
    db.Column('house_cd2', db.String(1)),
    db.Column('house_cd22', db.String(1)),
    db.Column('lead_in', db.String(1)),
    db.Column('ftth_cd', db.String(1)),
    db.Column('house_floor', db.String(1)),
    db.Column('tpc_user_cd', db.String(1)),
    db.Column('line_cd', db.String(1)),
    db.Column('work_flag', db.String(2)),
    db.Column('tpc_service_cd', db.String(1)),
    db.Column('tpc_kari_date', db.DateTime),
    db.Column('tpc_date', db.DateTime),
    db.Column('start_date', db.DateTime),
    db.Column('closed_date', db.DateTime),
    db.Column('check_date', db.DateTime),
    db.Column('check_time', db.String(1)),
    db.Column('work_date', db.DateTime),
    db.Column('work_time', db.String(1)),
    db.Column('work_end_date', db.DateTime),
    db.Column('cash_cd', db.String(1)),
    db.Column('lump_sum', db.String(30)),
    db.Column('apart_cd', db.String(13)),
    db.Column('opt_flag', db.String(30)),
    db.Column('vdsl_model', db.String(8)),
    db.Column('voip_model', db.String(8)),
    db.Column('musen_model', db.String(8)),
    db.Column('tpc_result', db.String(3)),
    db.Column('tpc_details', db.String(160)),
    db.Column('isp_notes', db.String(160)),
    db.Column('tpc_notes', db.String(160)),
    db.Column('campaign_cd', db.String(15)),
    db.Column('agency_cd', db.String(12)),
    db.Column('create_date', db.DateTime),
    db.Column('renew_date', db.DateTime),
    db.Column('operate_cd', db.String(128)),
    db.Column('c_flag', db.String(1)),
    db.Column('remark', db.String(80))
)


t_v_tepco_opr_mst = db.Table(
    'v_tepco_opr_mst',
    db.Column('apply_kind_cd', db.String(4)),
    db.Column('apply_kind_name', db.String(80)),
    db.Column('opr_apply_kind_cd', db.String(3)),
    db.Column('opr_apply_kind_name', db.String(60)),
    db.Column('data_cd', db.String(2)),
    db.Column('create_date', db.DateTime),
    db.Column('renew_date', db.DateTime),
    db.Column('operate_cd', db.String(128)),
    db.Column('c_flag', db.String(1))
)


t_v_tg_set_info = db.Table(
    'v_tg_set_info',
    db.Column('contract_no', db.String(12)),
    db.Column('isp_order_no', db.String(20)),
    db.Column('renew_date', db.DateTime),
    db.Column('create_date', db.DateTime),
    db.Column('operate_cd', db.String(128)),
    db.Column('c_flag', db.String(1)),
    db.Column('apply_date', db.DateTime),
    db.Column('tg_set_camp_status', db.String(2)),
    db.Column('tg_set_appy_available', db.String(1)),
    db.Column('tg_set_appy_ng_reason', db.String(1)),
    db.Column('tg_set_appy_result_date', db.DateTime),
    db.Column('tg_cont_no', db.String(13)),
    db.Column('tg_set_cont_no', db.String(13)),
    db.Column('tg_toss_cont_no', db.Numeric(8, 0)),
    db.Column('tg_customer_name', db.String(142)),
    db.Column('tg_customer_kname', db.String(142)),
    db.Column('tg_cont_status_gas', db.String(40)),
    db.Column('tg_start_date_gas', db.DateTime),
    db.Column('tg_cont_status_electric', db.String(40)),
    db.Column('tg_start_date_electric', db.DateTime),
    db.Column('tg_set_camp_available', db.String(1)),
    db.Column('tg_set_camp_ng_reason', db.String(1)),
    db.Column('removal_flag', db.String(1)),
    db.Column('yobi01', db.String(100))
)


t_v_tone_prefix_dat = db.Table(
    'v_tone_prefix_dat',
    db.Column('ws_common_id', db.String(20)),
    db.Column('ws_common_renbn', db.String(2)),
    db.Column('opt_contract_no', db.Numeric(10, 0)),
    db.Column('process_kbn', db.String(6)),
    db.Column('msisdn', db.String(11)),
    db.Column('contbase_no', db.String(10)),
    db.Column('exec_plan', db.String(1)),
    db.Column('prefix_cd', db.String(20)),
    db.Column('apply_kind', db.String(4)),
    db.Column('prog_status', db.String(2)),
    db.Column('send_plan_date', db.DateTime),
    db.Column('send_date', db.DateTime),
    db.Column('result_receive_date', db.DateTime),
    db.Column('result_cd', db.String(2)),
    db.Column('result_status', db.String(2)),
    db.Column('create_date', db.DateTime),
    db.Column('renew_date', db.DateTime),
    db.Column('operate_cd', db.String(128)),
    db.Column('c_flag', db.String(1))
)


t_v_tone_session = db.Table(
    'v_tone_session',
    db.Column('sid', db.String(40)),
    db.Column('data', db.Text),
    db.Column('expires', db.Numeric(10, 0))
)


t_v_trans_mst = db.Table(
    'v_trans_mst',
    db.Column('type', db.String(3)),
    db.Column('code1', db.String(100)),
    db.Column('code2', db.String(500))
)


t_v_trans_result_error_tmp = db.Table(
    'v_trans_result_error_tmp',
    db.Column('dmdto_id', db.String(12)),
    db.Column('dmd_no', db.String(13)),
    db.Column('result_cd', db.String(2)),
    db.Column('dmd_month', db.String(6)),
    db.Column('all_total', db.Numeric(10, 0)),
    db.Column('demand_kbn', db.String(2)),
    db.Column('valid_date', db.DateTime),
    db.Column('customer_id', db.String(8)),
    db.Column('cust_email', db.String(128)),
    db.Column('lastname', db.String(50)),
    db.Column('firstname', db.String(20)),
    db.Column('trans_result', db.String(2)),
    db.Column('year_month', db.String(6)),
    db.Column('disp_mmdd', db.String(4)),
    db.Column('trans_kind', db.String(1)),
    db.Column('create_date', db.DateTime),
    db.Column('current_demand_kbn', db.String(2)),
    db.Column('current_valid_date', db.DateTime)
)


t_v_trans_result_tmp = db.Table(
    'v_trans_result_tmp',
    db.Column('data_cd', db.String(1)),
    db.Column('trans_bankcd', db.String(4)),
    db.Column('trans_bankkana', db.String(30)),
    db.Column('trans_branchcd', db.String(3)),
    db.Column('trans_branchkana', db.String(30)),
    db.Column('blank', db.String(4)),
    db.Column('trans_acckind', db.String(1)),
    db.Column('trans_accno', db.String(7)),
    db.Column('trans_accname', db.String(60)),
    db.Column('trans_money', db.String(10)),
    db.Column('new_cd', db.String(1)),
    db.Column('fixed_item', db.String(6)),
    db.Column('zengin_cst_no', db.String(14)),
    db.Column('trans_result_cd', db.String(1)),
    db.Column('trans_kind', db.String(1)),
    db.Column('create_date', db.DateTime),
    db.Column('dmdto_id', db.String(12)),
    db.Column('dmd_no', db.String(13))
)


t_v_transfer_serversman_sim = db.Table(
    'v_transfer_serversman_sim',
    db.Column('dti_customer_id', db.String(8)),
    db.Column('tone_customer_id', db.String(8))
)


t_v_uname_dat = db.Table(
    'v_uname_dat',
    db.Column('ws_common_id', db.String(20)),
    db.Column('ws_common_renbn', db.Numeric(2, 0)),
    db.Column('contract_no', db.String(12)),
    db.Column('create_date', db.DateTime),
    db.Column('renew_date', db.DateTime),
    db.Column('operate_cd', db.String(128)),
    db.Column('c_flag', db.String(1)),
    db.Column('remark', db.String(80)),
    db.Column('second_lv_domain', db.String(64)),
    db.Column('top_lv_domain', db.String(3)),
    db.Column('domain_status', db.Numeric(2, 0)),
    db.Column('domain_start_date', db.DateTime),
    db.Column('domain_end_date', db.DateTime),
    db.Column('domain_exp_date', db.DateTime),
    db.Column('owner_j_last_name', db.String(50)),
    db.Column('owner_e_last_name', db.String(50)),
    db.Column('owner_j_first_name', db.String(50)),
    db.Column('owner_e_first_name', db.String(50)),
    db.Column('owner_user_type', db.String(1)),
    db.Column('owner_j_org_name', db.String(100)),
    db.Column('owner_e_org_name', db.String(100)),
    db.Column('owner_zip', db.String(16)),
    db.Column('owner_j_addr1', db.Numeric(2, 0)),
    db.Column('owner_e_addr1', db.String(20)),
    db.Column('owner_j_addr2', db.String(50)),
    db.Column('owner_e_addr2', db.String(50)),
    db.Column('owner_j_addr3', db.String(50)),
    db.Column('owner_e_addr3', db.String(50)),
    db.Column('owner_j_addr4', db.String(50)),
    db.Column('owner_e_addr4', db.String(50)),
    db.Column('owner_telno', db.String(20)),
    db.Column('owner_faxno', db.String(20)),
    db.Column('owner_email', db.String(100)),
    db.Column('admin_j_last_name', db.String(50)),
    db.Column('admin_e_last_name', db.String(50)),
    db.Column('admin_j_first_name', db.String(50)),
    db.Column('admin_e_first_name', db.String(50)),
    db.Column('admin_user_type', db.String(1)),
    db.Column('admin_j_org_name', db.String(100)),
    db.Column('admin_e_org_name', db.String(100)),
    db.Column('admin_zip', db.String(16)),
    db.Column('admin_j_addr1', db.Numeric(2, 0)),
    db.Column('admin_e_addr1', db.String(20)),
    db.Column('admin_j_addr2', db.String(50)),
    db.Column('admin_e_addr2', db.String(50)),
    db.Column('admin_j_addr3', db.String(50)),
    db.Column('admin_e_addr3', db.String(50)),
    db.Column('admin_j_addr4', db.String(50)),
    db.Column('admin_e_addr4', db.String(50)),
    db.Column('admin_telno', db.String(20)),
    db.Column('admin_faxno', db.String(20)),
    db.Column('admin_email', db.String(100)),
    db.Column('tech_j_last_name', db.String(50)),
    db.Column('tech_e_last_name', db.String(50)),
    db.Column('tech_j_first_name', db.String(50)),
    db.Column('tech_e_first_name', db.String(50)),
    db.Column('tech_user_type', db.String(1)),
    db.Column('tech_j_org_name', db.String(100)),
    db.Column('tech_e_org_name', db.String(100)),
    db.Column('tech_zip', db.String(16)),
    db.Column('tech_j_addr1', db.Numeric(2, 0)),
    db.Column('tech_e_addr1', db.String(20)),
    db.Column('tech_j_addr2', db.String(50)),
    db.Column('tech_e_addr2', db.String(50)),
    db.Column('tech_j_addr3', db.String(50)),
    db.Column('tech_e_addr3', db.String(50)),
    db.Column('tech_j_addr4', db.String(50)),
    db.Column('tech_e_addr4', db.String(50)),
    db.Column('tech_telno', db.String(20)),
    db.Column('tech_faxno', db.String(20)),
    db.Column('tech_email', db.String(100)),
    db.Column('acc_j_last_name', db.String(50)),
    db.Column('acc_e_last_name', db.String(50)),
    db.Column('acc_j_first_name', db.String(50)),
    db.Column('acc_e_first_name', db.String(50)),
    db.Column('acc_user_type', db.String(1)),
    db.Column('acc_j_org_name', db.String(100)),
    db.Column('acc_e_org_name', db.String(100)),
    db.Column('acc_zip', db.String(16)),
    db.Column('acc_j_addr1', db.Numeric(2, 0)),
    db.Column('acc_e_addr1', db.String(20)),
    db.Column('acc_j_addr2', db.String(50)),
    db.Column('acc_e_addr2', db.String(50)),
    db.Column('acc_j_addr3', db.String(50)),
    db.Column('acc_e_addr3', db.String(50)),
    db.Column('acc_j_addr4', db.String(50)),
    db.Column('acc_e_addr4', db.String(50)),
    db.Column('acc_telno', db.String(20)),
    db.Column('acc_faxno', db.String(20)),
    db.Column('acc_email', db.String(100)),
    db.Column('gmo_id', db.String(18)),
    db.Column('gmo_pass', db.String(18)),
    db.Column('release_apply_date', db.DateTime),
    db.Column('domain_pending_id', db.String(18))
)


t_v_universal_service_mst = db.Table(
    'v_universal_service_mst',
    db.Column('valid_date', db.DateTime),
    db.Column('cost', db.Numeric(2, 0)),
    db.Column('taxfree_kbn', db.String(1)),
    db.Column('create_date', db.DateTime),
    db.Column('renew_date', db.DateTime),
    db.Column('operate_cd', db.String(128))
)


t_v_unlimited_charge_log = db.Table(
    'v_unlimited_charge_log',
    db.Column('used_month', db.Date),
    db.Column('line_no', db.Numeric(7, 0)),
    db.Column('msisdn', db.String(16)),
    db.Column('charge_kb', db.Numeric(7, 0)),
    db.Column('charge_date', db.DateTime),
    db.Column('quota_code', db.String(128)),
    db.Column('bill_month', db.Date),
    db.Column('contract_no', db.String(12)),
    db.Column('free_flag', db.String(3)),
    db.Column('create_date', db.DateTime),
    db.Column('renew_date', db.DateTime),
    db.Column('operate_cd', db.String(128))
)


t_v_upd_customer_id_mng_tmp = db.Table(
    'v_upd_customer_id_mng_tmp',
    db.Column('customer_id', db.String(8)),
    db.Column('pay_status', db.String(1)),
    db.Column('create_date', db.DateTime),
    db.Column('renew_date', db.DateTime),
    db.Column('operate_cd', db.String(128))
)


t_v_used_3g_unlimited = db.Table(
    'v_used_3g_unlimited',
    db.Column('dmdto_id', db.String(12)),
    db.Column('contract_no', db.String(12)),
    db.Column('msisdn', db.String(11)),
    db.Column('used_kb', db.Numeric(10, 0)),
    db.Column('remain_kb', db.Numeric(10, 0)),
    db.Column('used', db.Numeric(10, 0)),
    db.Column('remain', db.Numeric(10, 0)),
    db.Column('used_tax', db.Numeric(10, 0)),
    db.Column('remain_tax', db.Numeric(10, 0)),
    db.Column('tax_late', db.String(5)),
    db.Column('charged', db.Numeric(10, 0)),
    db.Column('used_date', db.DateTime),
    db.Column('expire_date', db.DateTime),
    db.Column('plan_cd', db.String(8)),
    db.Column('dmd_date', db.DateTime),
    db.Column('create_date', db.DateTime),
    db.Column('free_flag', db.String(1))
)


t_v_voip_c_dat = db.Table(
    'v_voip_c_dat',
    db.Column('ws_common_id', db.String(20)),
    db.Column('ws_common_renbn', db.String(2)),
    db.Column('contract_no', db.String(12)),
    db.Column('opt_contract_no', db.Numeric(10, 0)),
    db.Column('isp_order_no', db.String(20)),
    db.Column('isp_opt_order_no', db.String(20)),
    db.Column('enduser_id', db.String(20)),
    db.Column('apply_date', db.DateTime),
    db.Column('send_plan_date', db.DateTime),
    db.Column('send_date', db.DateTime),
    db.Column('apply_kind', db.String(4)),
    db.Column('prog_status', db.String(2)),
    db.Column('apply_brand', db.String(2)),
    db.Column('order_no', db.String(10)),
    db.Column('acca_no', db.String(60)),
    db.Column('business_cd', db.String(2)),
    db.Column('action', db.String(2)),
    db.Column('option_kind', db.String(2)),
    db.Column('line_name', db.String(60)),
    db.Column('zip', db.String(8)),
    db.Column('todohuken', db.String(8)),
    db.Column('gun', db.String(30)),
    db.Column('ku', db.String(30)),
    db.Column('area', db.String(30)),
    db.Column('banchi', db.String(50)),
    db.Column('build_name', db.String(120)),
    db.Column('telno', db.String(13)),
    db.Column('toi_telno', db.String(13)),
    db.Column('email', db.String(90)),
    db.Column('cpe_provider', db.String(1)),
    db.Column('cpe_installer', db.String(1)),
    db.Column('cpe_kind', db.String(3)),
    db.Column('vo_user_id', db.String(40)),
    db.Column('vo_passwd', db.String(20)),
    db.Column('vo_telno', db.String(15)),
    db.Column('vo_server', db.String(50)),
    db.Column('vo_domain', db.String(50)),
    db.Column('isp_circuit_no', db.String(20)),
    db.Column('ntt_work_date', db.DateTime),
    db.Column('billing_date', db.DateTime),
    db.Column('change_date', db.DateTime),
    db.Column('cancel_date', db.DateTime),
    db.Column('agency_cd', db.String(12)),
    db.Column('create_date', db.DateTime),
    db.Column('renew_date', db.DateTime),
    db.Column('operate_cd', db.String(128)),
    db.Column('c_flag', db.String(1)),
    db.Column('remark', db.String(80))
)


t_v_voip_c_num_mst = db.Table(
    'v_voip_c_num_mst',
    db.Column('telno', db.String(13)),
    db.Column('sip_user_id', db.String(40)),
    db.Column('sip_password', db.String(20)),
    db.Column('sip_server', db.String(50)),
    db.Column('status', db.String(1)),
    db.Column('pr_order_line_date', db.DateTime),
    db.Column('start_date', db.DateTime),
    db.Column('end_date', db.DateTime),
    db.Column('create_date', db.DateTime),
    db.Column('renew_date', db.DateTime),
    db.Column('operate_cd', db.String(128))
)


t_v_voip_c_sip_mst = db.Table(
    'v_voip_c_sip_mst',
    db.Column('sip_user_id', db.String(40)),
    db.Column('sip_password', db.String(20)),
    db.Column('status', db.String(1)),
    db.Column('create_date', db.DateTime),
    db.Column('renew_date', db.DateTime),
    db.Column('operate_cd', db.String(128)),
    db.Column('isp_cd', db.String(5))
)


t_v_voip_f_dat = db.Table(
    'v_voip_f_dat',
    db.Column('ws_common_id', db.String(20)),
    db.Column('ws_common_renbn', db.String(2)),
    db.Column('contract_no', db.String(12)),
    db.Column('opt_contract_no', db.Numeric(10, 0)),
    db.Column('isp_portable_userid', db.String(12)),
    db.Column('isp_userid', db.String(15)),
    db.Column('isp_order_no', db.String(12)),
    db.Column('apply_date', db.DateTime),
    db.Column('send_plan_date', db.DateTime),
    db.Column('send_date', db.DateTime),
    db.Column('apply_kind', db.String(4)),
    db.Column('prog_status', db.String(2)),
    db.Column('master_status', db.String(2)),
    db.Column('business_cd', db.String(2)),
    db.Column('telno_050', db.String(32)),
    db.Column('telno_0abj', db.String(32)),
    db.Column('portable_tel', db.String(15)),
    db.Column('portable_cd', db.String(1)),
    db.Column('account_050', db.String(32)),
    db.Column('password_050', db.String(32)),
    db.Column('password_0abj', db.String(32)),
    db.Column('ppp_name', db.String(128)),
    db.Column('rental_cd', db.String(1)),
    db.Column('iad_type', db.String(1)),
    db.Column('plan_cd', db.String(8)),
    db.Column('use_change_date', db.DateTime),
    db.Column('ip_start_date', db.DateTime),
    db.Column('ip_end_date', db.DateTime),
    db.Column('suspend_date', db.DateTime),
    db.Column('re_suspend_date', db.DateTime),
    db.Column('iad_status', db.String(1)),
    db.Column('dl_start_date', db.DateTime),
    db.Column('dl_term_date', db.DateTime),
    db.Column('dl_comp_date', db.DateTime),
    db.Column('dl_remind_no', db.Numeric(1, 0)),
    db.Column('start_0abj', db.DateTime),
    db.Column('end_0abj', db.DateTime),
    db.Column('portable_work_date', db.DateTime),
    db.Column('ftth_start_date', db.DateTime),
    db.Column('portable_date', db.DateTime),
    db.Column('portable_ng_cd', db.String(80)),
    db.Column('portable_ng', db.String(256)),
    db.Column('portable_remind_no', db.Numeric(1, 0)),
    db.Column('portable_ng_date', db.DateTime),
    db.Column('bill_flag', db.String(8)),
    db.Column('unnotify_ref_status', db.String(1)),
    db.Column('refusal_number_status', db.String(1)),
    db.Column('catch_status', db.String(1)),
    db.Column('portable_status', db.String(1)),
    db.Column('status_104', db.String(1)),
    db.Column('user_name', db.String(40)),
    db.Column('user_kana', db.String(72)),
    db.Column('zip', db.String(8)),
    db.Column('todohuken', db.String(8)),
    db.Column('gun', db.String(50)),
    db.Column('ku', db.String(40)),
    db.Column('area', db.String(40)),
    db.Column('chome', db.String(10)),
    db.Column('banchi', db.String(40)),
    db.Column('build_name', db.String(126)),
    db.Column('ntt_name', db.String(90)),
    db.Column('ntt_kana', db.String(180)),
    db.Column('ntt_zip', db.String(8)),
    db.Column('ntt_todohuken', db.String(8)),
    db.Column('ntt_gun', db.String(40)),
    db.Column('ntt_ku', db.String(40)),
    db.Column('ntt_area', db.String(40)),
    db.Column('ntt_chome', db.String(10)),
    db.Column('ntt_banchi', db.String(40)),
    db.Column('ntt_build_name', db.String(80)),
    db.Column('toi_telno', db.String(13)),
    db.Column('direct_name', db.String(128)),
    db.Column('direct_kana', db.String(240)),
    db.Column('direct_zip', db.String(8)),
    db.Column('direct_todohuken', db.String(8)),
    db.Column('direct_gun', db.String(40)),
    db.Column('direct_ku', db.String(40)),
    db.Column('direct_area', db.String(40)),
    db.Column('direct_chome', db.String(10)),
    db.Column('direct_banchi', db.String(40)),
    db.Column('direct_build_name', db.String(80)),
    db.Column('build_kind', db.String(1)),
    db.Column('user_cd', db.String(1)),
    db.Column('note1', db.String(32)),
    db.Column('note2', db.String(256)),
    db.Column('campaign_cd', db.String(15)),
    db.Column('agency_cd', db.String(12)),
    db.Column('mansion_id', db.String(13)),
    db.Column('sip_server_address', db.String(50)),
    db.Column('create_date', db.DateTime),
    db.Column('renew_date', db.DateTime),
    db.Column('operate_cd', db.String(128)),
    db.Column('c_flag', db.String(1)),
    db.Column('no_return_kbn', db.String(1)),
    db.Column('entry_cd', db.String(13)),
    db.Column('remark', db.String(80))
)


t_v_voip_f_ref_telno_info = db.Table(
    'v_voip_f_ref_telno_info',
    db.Column('ip_telno', db.String(11)),
    db.Column('ref_telno_01', db.String(11)),
    db.Column('ref_telno_02', db.String(11)),
    db.Column('ref_telno_03', db.String(11)),
    db.Column('ref_telno_04', db.String(11)),
    db.Column('ref_telno_05', db.String(11)),
    db.Column('ref_telno_06', db.String(11)),
    db.Column('ref_telno_07', db.String(11)),
    db.Column('ref_telno_08', db.String(11)),
    db.Column('ref_telno_09', db.String(11)),
    db.Column('ref_telno_10', db.String(11)),
    db.Column('ref_telno_11', db.String(11)),
    db.Column('ref_telno_12', db.String(11)),
    db.Column('ref_telno_13', db.String(11)),
    db.Column('ref_telno_14', db.String(11)),
    db.Column('ref_telno_15', db.String(11)),
    db.Column('ref_telno_16', db.String(11)),
    db.Column('ref_telno_17', db.String(11)),
    db.Column('ref_telno_18', db.String(11)),
    db.Column('ref_telno_19', db.String(11)),
    db.Column('ref_telno_20', db.String(11)),
    db.Column('ref_telno_21', db.String(11)),
    db.Column('ref_telno_22', db.String(11)),
    db.Column('ref_telno_23', db.String(11)),
    db.Column('ref_telno_24', db.String(11)),
    db.Column('ref_telno_25', db.String(11)),
    db.Column('ref_telno_26', db.String(11)),
    db.Column('ref_telno_27', db.String(11)),
    db.Column('ref_telno_28', db.String(11)),
    db.Column('ref_telno_29', db.String(11)),
    db.Column('ref_telno_30', db.String(11)),
    db.Column('create_date', db.DateTime),
    db.Column('renew_date', db.DateTime),
    db.Column('operate_cd', db.String(128)),
    db.Column('c_flag', db.String(1))
)


t_v_voip_info = db.Table(
    'v_voip_info',
    db.Column('telno', db.String(13)),
    db.Column('bill_kbn_cd', db.String(2)),
    db.Column('used_month', db.Date),
    db.Column('enduser_id', db.String(32)),
    db.Column('bill_month', db.Date),
    db.Column('use_minute', db.Numeric(7, 0)),
    db.Column('cost', db.Numeric(16, 4)),
    db.Column('taxfree_kbn', db.String(1)),
    db.Column('create_date', db.DateTime),
    db.Column('renew_date', db.DateTime),
    db.Column('operate_cd', db.String(128)),
    db.Column('c_flag', db.String(1)),
    db.Column('use_count', db.Numeric(7, 0))
)


t_v_voip_p_dat = db.Table(
    'v_voip_p_dat',
    db.Column('ws_common_id', db.String(20)),
    db.Column('ws_common_renbn', db.String(2)),
    db.Column('contract_no', db.String(12)),
    db.Column('opt_contract_no', db.Numeric(10, 0)),
    db.Column('apply_date', db.DateTime),
    db.Column('send_plan_date', db.DateTime),
    db.Column('send_date', db.DateTime),
    db.Column('apply_kind', db.String(4)),
    db.Column('prog_status', db.String(2)),
    db.Column('oem_id', db.String(4)),
    db.Column('oem_key', db.String(32)),
    db.Column('phone_user_id', db.String(128)),
    db.Column('isp_num', db.String(3)),
    db.Column('telno', db.String(13)),
    db.Column('sip_user_id', db.String(40)),
    db.Column('sip_password', db.String(20)),
    db.Column('sip_server', db.String(50)),
    db.Column('remark', db.String(80)),
    db.Column('create_date', db.DateTime),
    db.Column('renew_date', db.DateTime),
    db.Column('operate_cd', db.String(128)),
    db.Column('c_flag', db.String(1))
)


t_v_volume_discount_daily = db.Table(
    'v_volume_discount_daily',
    db.Column('contract_no', db.String(12)),
    db.Column('renew_date', db.DateTime),
    db.Column('customer_id', db.String(8)),
    db.Column('plan_cd', db.String(8)),
    db.Column('volume_discount_cd', db.String(2)),
    db.Column('discounted', db.String(1)),
    db.Column('parent_children', db.String(1)),
    db.Column('parent_contract_no', db.String(12)),
    db.Column('discount_cost', db.Numeric(8, 0)),
    db.Column('taxfree_kbn', db.String(1)),
    db.Column('volume_discount_kind', db.String(1)),
    db.Column('discount_start_date', db.DateTime),
    db.Column('discount_end_date', db.DateTime),
    db.Column('tax_cost', db.Numeric(8, 0))
)


t_v_volume_discount_monthly = db.Table(
    'v_volume_discount_monthly',
    db.Column('bill_month', db.Date),
    db.Column('contract_no', db.String(12)),
    db.Column('renew_date', db.DateTime),
    db.Column('customer_id', db.String(8)),
    db.Column('plan_cd', db.String(8)),
    db.Column('volume_discount_cd', db.String(2)),
    db.Column('discounted', db.String(1)),
    db.Column('parent_children', db.String(1)),
    db.Column('parent_contract_no', db.String(12)),
    db.Column('discount_cost', db.Numeric(8, 0)),
    db.Column('taxfree_kbn', db.String(1)),
    db.Column('volume_discount_kind', db.String(1)),
    db.Column('discount_start_date', db.DateTime),
    db.Column('discount_end_date', db.DateTime),
    db.Column('tax_cost', db.Numeric(8, 0))
)


t_v_volume_discount_mst = db.Table(
    'v_volume_discount_mst',
    db.Column('volume_discount_cd', db.String(2)),
    db.Column('volume_discount_name', db.String(16)),
    db.Column('volume_discount_kind', db.String(1)),
    db.Column('parent_priority', db.Numeric(1, 0)),
    db.Column('discount_cost', db.Numeric(8, 0)),
    db.Column('taxfree_kbn', db.String(1)),
    db.Column('max_discount_quantity', db.Numeric(2, 0))
)


t_v_wimax_dat = db.Table(
    'v_wimax_dat',
    db.Column('ws_common_id', db.String(20)),
    db.Column('ws_common_renbn', db.String(2)),
    db.Column('contract_no', db.String(12)),
    db.Column('opt_contract_no', db.Numeric(10, 0)),
    db.Column('renew_date', db.DateTime),
    db.Column('create_date', db.DateTime),
    db.Column('operate_cd', db.String(128)),
    db.Column('c_flag', db.String(1)),
    db.Column('remark', db.String(80)),
    db.Column('apply_date', db.DateTime),
    db.Column('apply_kind', db.String(4)),
    db.Column('prog_status', db.String(2)),
    db.Column('send_plan_date', db.DateTime),
    db.Column('send_date', db.DateTime),
    db.Column('wimax_user_id', db.String(10)),
    db.Column('cui', db.String(20)),
    db.Column('uq_issue_date', db.DateTime),
    db.Column('uq_cont_start_date', db.DateTime),
    db.Column('mac_address', db.String(12)),
    db.Column('serial_no', db.String(25)),
    db.Column('send_name', db.String(100)),
    db.Column('send_name_kana', db.String(100)),
    db.Column('send_zip', db.String(7)),
    db.Column('send_todohuken', db.String(8)),
    db.Column('send_addr1', db.String(50)),
    db.Column('send_addr2', db.String(60)),
    db.Column('send_build_name', db.String(80)),
    db.Column('send_telno', db.String(13)),
    db.Column('arrival_plan_date', db.DateTime),
    db.Column('arrival_plan_time', db.String(1)),
    db.Column('ship_no', db.String(20)),
    db.Column('direct_date', db.DateTime),
    db.Column('ship_plan_date', db.DateTime),
    db.Column('ship_decision_date', db.DateTime),
    db.Column('id_renbn', db.Numeric(2, 0)),
    db.Column('equipment_info', db.String(8)),
    db.Column('send_status', db.String(2)),
    db.Column('ship_comp_date', db.DateTime),
    db.Column('iccid', db.String(19)),
    db.Column('ccode', db.String(11)),
    db.Column('uq_apply_no', db.String(9)),
    db.Column('uq_user_cd', db.String(8)),
    db.Column('user_birth', db.DateTime),
    db.Column('shop_accept_date', db.DateTime),
    db.Column('user_sex', db.String(1)),
    db.Column('policy_cd', db.String(40)),
    db.Column('uq_apply_date', db.DateTime),
    db.Column('mvno_plan_cd', db.String(3))
)


t_v_ws_bill_info = db.Table(
    'v_ws_bill_info',
    db.Column('ws_id', db.String(20)),
    db.Column('ws_kbn', db.String(2)),
    db.Column('bill_type', db.String(1)),
    db.Column('contract_no', db.String(12)),
    db.Column('opt_contract_no', db.Numeric(10, 0)),
    db.Column('plan_cd', db.String(8)),
    db.Column('used_month', db.Date),
    db.Column('bill_month', db.Date),
    db.Column('bill_kbn_cd', db.String(2)),
    db.Column('quantity', db.Numeric(19, 0)),
    db.Column('cost', db.Numeric(9, 0)),
    db.Column('unit', db.String(10)),
    db.Column('unit_cost', db.Numeric(10, 4)),
    db.Column('taxfree_kbn', db.String(1)),
    db.Column('kihon_tuika_kbn', db.String(1)),
    db.Column('creditor_cd', db.String(1)),
    db.Column('creditor_subcd', db.String(3)),
    db.Column('create_date', db.DateTime),
    db.Column('renew_date', db.DateTime),
    db.Column('c_flag', db.String(1)),
    db.Column('operate_cd', db.String(128)),
    db.Column('plan_name', db.String(128)),
    db.Column('account_id', db.String(64)),
    db.Column('tax_cost', db.Numeric(9, 0))
)


t_v_ws_call_log = db.Table(
    'v_ws_call_log',
    db.Column('bill_month', db.Date),
    db.Column('ws_kbn', db.String(2)),
    db.Column('data_renbn', db.Numeric(7, 0)),
    db.Column('telno', db.String(16)),
    db.Column('partner_telno', db.String(16)),
    db.Column('call_start_time', db.DateTime),
    db.Column('call_time', db.String(7)),
    db.Column('call_charge', db.Numeric(7, 1)),
    db.Column('ws_cont_id', db.String(64)),
    db.Column('note1', db.String(256)),
    db.Column('note2', db.String(256)),
    db.Column('note3', db.String(256)),
    db.Column('note4', db.String(256)),
    db.Column('note5', db.String(256)),
    db.Column('used_month', db.Date),
    db.Column('contract_no', db.String(12)),
    db.Column('opt_contract_no', db.Numeric(10, 0)),
    db.Column('user_charge', db.Numeric(7, 1)),
    db.Column('bill_kbn_cd', db.String(2)),
    db.Column('create_date', db.DateTime),
    db.Column('renew_date', db.DateTime),
    db.Column('operate_cd', db.String(128))
)


t_v_ws_updatelog = db.Table(
    'v_ws_updatelog',
    db.Column('ws_updatelog_id', db.Numeric(10, 0)),
    db.Column('contract_no', db.String(12)),
    db.Column('opt_contract_no', db.Numeric(10, 0)),
    db.Column('ws_type', db.String(5)),
    db.Column('update_status', db.String(2)),
    db.Column('ntt_result', db.String(2)),
    db.Column('customer_id', db.String(8)),
    db.Column('account_id', db.String(64)),
    db.Column('apply_kind', db.String(4)),
    db.Column('detail', db.String(256)),
    db.Column('prog_status', db.String(2)),
    db.Column('prog_status_ws', db.String(4)),
    db.Column('update_date', db.DateTime),
    db.Column('plan_cd', db.String(8)),
    db.Column('prev_plan_cd', db.String(8)),
    db.Column('pay_status', db.String(2)),
    db.Column('isp_order_no', db.String(20)),
    db.Column('appli_cd', db.String(50)),
    db.Column('acca_order_no', db.String(10)),
    db.Column('portable_apply', db.String(1)),
    db.Column('business_cd', db.String(2)),
    db.Column('enduser_id', db.String(20)),
    db.Column('ws_common_id', db.String(20)),
    db.Column('ws_common_renbn', db.String(2)),
    db.Column('notify_uss', db.String(1)),
    db.Column('notify_user', db.String(1)),
    db.Column('create_date', db.DateTime),
    db.Column('renew_date', db.DateTime),
    db.Column('operate_cd', db.String(128)),
    db.Column('c_flag', db.String(1)),
    db.Column('osm_entry_cd', db.String(10)),
    db.Column('send_status', db.String(2)),
    db.Column('imei', db.String(15)),
    db.Column('iccid', db.String(19)),
    db.Column('em_cont_cd', db.String(10))
)


t_v_xtyle_info = db.Table(
    'v_xtyle_info',
    db.Column('opt_contract_no', db.Numeric(10, 0)),
    db.Column('prog_status', db.String(2)),
    db.Column('send_date', db.DateTime),
    db.Column('form_no', db.String(20)),
    db.Column('serial_no', db.String(9)),
    db.Column('id', db.String(7)),
    db.Column('create_date', db.DateTime),
    db.Column('renew_date', db.DateTime),
    db.Column('operate_cd', db.String(128)),
    db.Column('c_flag', db.String(1))
)


class VoipCDat(db.Model):
    __tablename__ = 'voip_c_dat'

    ws_common_id = db.Column(db.String(20), primary_key=True)
    ws_common_renbn = db.Column(db.String(2))
    contract_no = db.Column(db.String(12), nullable=False)
    opt_contract_no = db.Column(db.Numeric(10, 0))
    isp_order_no = db.Column(db.String(20), nullable=False)
    isp_opt_order_no = db.Column(db.String(20))
    enduser_id = db.Column(db.String(20))
    apply_date = db.Column(db.DateTime)
    send_plan_date = db.Column(db.DateTime)
    send_date = db.Column(db.DateTime)
    apply_kind = db.Column(db.String(4))
    prog_status = db.Column(db.String(2))
    apply_brand = db.Column(db.String(2))
    order_no = db.Column(db.String(10))
    acca_no = db.Column(db.String(60))
    business_cd = db.Column(db.String(2))
    action = db.Column(db.String(2))
    option_kind = db.Column(db.String(2))
    line_name = db.Column(db.String(60))
    zip = db.Column(db.String(8))
    todohuken = db.Column(db.String(8))
    gun = db.Column(db.String(30))
    ku = db.Column(db.String(30))
    area = db.Column(db.String(30))
    banchi = db.Column(db.String(50))
    build_name = db.Column(db.String(120))
    telno = db.Column(db.String(13))
    toi_telno = db.Column(db.String(13))
    email = db.Column(db.String(90))
    cpe_provider = db.Column(db.String(1))
    cpe_installer = db.Column(db.String(1))
    cpe_kind = db.Column(db.String(3))
    vo_user_id = db.Column(db.String(40))
    vo_passwd = db.Column(db.String(20))
    vo_telno = db.Column(db.String(15), index=True)
    vo_server = db.Column(db.String(50))
    vo_domain = db.Column(db.String(50))
    isp_circuit_no = db.Column(db.String(20))
    ntt_work_date = db.Column(db.DateTime)
    billing_date = db.Column(db.DateTime)
    change_date = db.Column(db.DateTime)
    cancel_date = db.Column(db.DateTime)
    agency_cd = db.Column(db.String(12))
    create_date = db.Column(db.DateTime, nullable=False)
    renew_date = db.Column(db.DateTime, nullable=False)
    operate_cd = db.Column(db.String(128), nullable=False)
    c_flag = db.Column(db.String(1))
    remark = db.Column(db.String(80))


class VoipCNumMst(db.Model):
    __tablename__ = 'voip_c_num_mst'

    telno = db.Column(db.String(13), primary_key=True)
    sip_user_id = db.Column(db.String(40))
    sip_password = db.Column(db.String(20))
    sip_server = db.Column(db.String(50))
    status = db.Column(db.String(1), nullable=False)
    pr_order_line_date = db.Column(db.DateTime)
    start_date = db.Column(db.DateTime)
    end_date = db.Column(db.DateTime)
    create_date = db.Column(db.DateTime, nullable=False)
    renew_date = db.Column(db.DateTime, nullable=False)
    operate_cd = db.Column(db.String(128), nullable=False)


class VoipCSipMst(db.Model):
    __tablename__ = 'voip_c_sip_mst'

    sip_user_id = db.Column(db.String(40), primary_key=True, nullable=False)
    sip_password = db.Column(db.String(20), primary_key=True, nullable=False)
    status = db.Column(db.String(1), nullable=False)
    create_date = db.Column(db.DateTime, nullable=False)
    renew_date = db.Column(db.DateTime, nullable=False)
    operate_cd = db.Column(db.String(128), nullable=False)
    isp_cd = db.Column(db.String(5), nullable=False, server_default=db.FetchedValue())


class VoipFDat(db.Model):
    __tablename__ = 'voip_f_dat'

    ws_common_id = db.Column(db.String(20), primary_key=True)
    ws_common_renbn = db.Column(db.String(2))
    contract_no = db.Column(db.String(12), nullable=False, index=True)
    opt_contract_no = db.Column(db.Numeric(10, 0), index=True)
    isp_portable_userid = db.Column(db.String(12))
    isp_userid = db.Column(db.String(15))
    isp_order_no = db.Column(db.String(12), nullable=False)
    apply_date = db.Column(db.DateTime, nullable=False)
    send_plan_date = db.Column(db.DateTime)
    send_date = db.Column(db.DateTime)
    apply_kind = db.Column(db.String(4))
    prog_status = db.Column(db.String(2))
    master_status = db.Column(db.String(2))
    business_cd = db.Column(db.String(2))
    telno_050 = db.Column(db.String(32), index=True)
    telno_0abj = db.Column(db.String(32), index=True)
    portable_tel = db.Column(db.String(15))
    portable_cd = db.Column(db.String(1))
    account_050 = db.Column(db.String(32))
    password_050 = db.Column(db.String(32))
    password_0abj = db.Column(db.String(32))
    ppp_name = db.Column(db.String(128))
    rental_cd = db.Column(db.String(1))
    iad_type = db.Column(db.String(1))
    plan_cd = db.Column(db.String(8))
    use_change_date = db.Column(db.DateTime)
    ip_start_date = db.Column(db.DateTime)
    ip_end_date = db.Column(db.DateTime)
    suspend_date = db.Column(db.DateTime)
    re_suspend_date = db.Column(db.DateTime)
    iad_status = db.Column(db.String(1))
    dl_start_date = db.Column(db.DateTime)
    dl_term_date = db.Column(db.DateTime)
    dl_comp_date = db.Column(db.DateTime)
    dl_remind_no = db.Column(db.Numeric(1, 0))
    start_0abj = db.Column(db.DateTime)
    end_0abj = db.Column(db.DateTime)
    portable_work_date = db.Column(db.DateTime)
    ftth_start_date = db.Column(db.DateTime)
    portable_date = db.Column(db.DateTime)
    portable_ng_cd = db.Column(db.String(80))
    portable_ng = db.Column(db.String(256))
    portable_remind_no = db.Column(db.Numeric(1, 0))
    portable_ng_date = db.Column(db.DateTime)
    bill_flag = db.Column(db.String(8))
    unnotify_ref_status = db.Column(db.String(1))
    refusal_number_status = db.Column(db.String(1))
    catch_status = db.Column(db.String(1))
    portable_status = db.Column(db.String(1))
    status_104 = db.Column(db.String(1))
    user_name = db.Column(db.String(40))
    user_kana = db.Column(db.String(72))
    zip = db.Column(db.String(8))
    todohuken = db.Column(db.String(8))
    gun = db.Column(db.String(50))
    ku = db.Column(db.String(40))
    area = db.Column(db.String(40))
    chome = db.Column(db.String(10))
    banchi = db.Column(db.String(40))
    build_name = db.Column(db.String(126))
    ntt_name = db.Column(db.String(90))
    ntt_kana = db.Column(db.String(180))
    ntt_zip = db.Column(db.String(8))
    ntt_todohuken = db.Column(db.String(8))
    ntt_gun = db.Column(db.String(40))
    ntt_ku = db.Column(db.String(40))
    ntt_area = db.Column(db.String(40))
    ntt_chome = db.Column(db.String(10))
    ntt_banchi = db.Column(db.String(40))
    ntt_build_name = db.Column(db.String(80))
    toi_telno = db.Column(db.String(13))
    direct_name = db.Column(db.String(128))
    direct_kana = db.Column(db.String(240))
    direct_zip = db.Column(db.String(8))
    direct_todohuken = db.Column(db.String(8))
    direct_gun = db.Column(db.String(40))
    direct_ku = db.Column(db.String(40))
    direct_area = db.Column(db.String(40))
    direct_chome = db.Column(db.String(10))
    direct_banchi = db.Column(db.String(40))
    direct_build_name = db.Column(db.String(80))
    build_kind = db.Column(db.String(1))
    user_cd = db.Column(db.String(1))
    note1 = db.Column(db.String(32))
    note2 = db.Column(db.String(256))
    campaign_cd = db.Column(db.String(15))
    agency_cd = db.Column(db.String(12))
    mansion_id = db.Column(db.String(13))
    sip_server_address = db.Column(db.String(50))
    create_date = db.Column(db.DateTime, nullable=False)
    renew_date = db.Column(db.DateTime, nullable=False)
    operate_cd = db.Column(db.String(128), nullable=False)
    c_flag = db.Column(db.String(1))
    no_return_kbn = db.Column(db.String(1))
    entry_cd = db.Column(db.String(13))
    remark = db.Column(db.String(80))


class VoipFRefTelnoInfo(db.Model):
    __tablename__ = 'voip_f_ref_telno_info'

    ip_telno = db.Column(db.String(11), primary_key=True)
    ref_telno_01 = db.Column(db.String(11))
    ref_telno_02 = db.Column(db.String(11))
    ref_telno_03 = db.Column(db.String(11))
    ref_telno_04 = db.Column(db.String(11))
    ref_telno_05 = db.Column(db.String(11))
    ref_telno_06 = db.Column(db.String(11))
    ref_telno_07 = db.Column(db.String(11))
    ref_telno_08 = db.Column(db.String(11))
    ref_telno_09 = db.Column(db.String(11))
    ref_telno_10 = db.Column(db.String(11))
    ref_telno_11 = db.Column(db.String(11))
    ref_telno_12 = db.Column(db.String(11))
    ref_telno_13 = db.Column(db.String(11))
    ref_telno_14 = db.Column(db.String(11))
    ref_telno_15 = db.Column(db.String(11))
    ref_telno_16 = db.Column(db.String(11))
    ref_telno_17 = db.Column(db.String(11))
    ref_telno_18 = db.Column(db.String(11))
    ref_telno_19 = db.Column(db.String(11))
    ref_telno_20 = db.Column(db.String(11))
    ref_telno_21 = db.Column(db.String(11))
    ref_telno_22 = db.Column(db.String(11))
    ref_telno_23 = db.Column(db.String(11))
    ref_telno_24 = db.Column(db.String(11))
    ref_telno_25 = db.Column(db.String(11))
    ref_telno_26 = db.Column(db.String(11))
    ref_telno_27 = db.Column(db.String(11))
    ref_telno_28 = db.Column(db.String(11))
    ref_telno_29 = db.Column(db.String(11))
    ref_telno_30 = db.Column(db.String(11))
    create_date = db.Column(db.DateTime, nullable=False)
    renew_date = db.Column(db.DateTime, nullable=False)
    operate_cd = db.Column(db.String(128), nullable=False)
    c_flag = db.Column(db.String(1))


class VoipInfo(db.Model):
    __tablename__ = 'voip_info'

    telno = db.Column(db.String(13), primary_key=True, nullable=False)
    bill_kbn_cd = db.Column(db.String(2), primary_key=True, nullable=False)
    used_month = db.Column(db.Date, primary_key=True, nullable=False)
    enduser_id = db.Column(db.String(32))
    bill_month = db.Column(db.Date, nullable=False, index=True)
    use_minute = db.Column(db.Numeric(7, 0))
    cost = db.Column(db.Numeric(16, 4), nullable=False)
    taxfree_kbn = db.Column(db.String(1), nullable=False)
    create_date = db.Column(db.DateTime, nullable=False)
    renew_date = db.Column(db.DateTime, nullable=False)
    operate_cd = db.Column(db.String(128), nullable=False)
    c_flag = db.Column(db.String(1))
    use_count = db.Column(db.Numeric(7, 0))


class VoipPDat(db.Model):
    __tablename__ = 'voip_p_dat'

    ws_common_id = db.Column(db.String(20), primary_key=True)
    ws_common_renbn = db.Column(db.String(2))
    contract_no = db.Column(db.String(12))
    opt_contract_no = db.Column(db.Numeric(10, 0))
    apply_date = db.Column(db.DateTime, nullable=False)
    send_plan_date = db.Column(db.DateTime)
    send_date = db.Column(db.DateTime)
    apply_kind = db.Column(db.String(4))
    prog_status = db.Column(db.String(2))
    oem_id = db.Column(db.String(4), nullable=False)
    oem_key = db.Column(db.String(32))
    phone_user_id = db.Column(db.String(128))
    isp_num = db.Column(db.String(3))
    telno = db.Column(db.String(13), index=True)
    sip_user_id = db.Column(db.String(40))
    sip_password = db.Column(db.String(20))
    sip_server = db.Column(db.String(50))
    remark = db.Column(db.String(80))
    create_date = db.Column(db.DateTime, nullable=False)
    renew_date = db.Column(db.DateTime, nullable=False)
    operate_cd = db.Column(db.String(128), nullable=False)
    c_flag = db.Column(db.String(1))


class VolumeDiscountDaily(db.Model):
    __tablename__ = 'volume_discount_daily'

    contract_no = db.Column(db.String(12), primary_key=True)
    renew_date = db.Column(db.DateTime, nullable=False)
    customer_id = db.Column(db.String(8), nullable=False)
    plan_cd = db.Column(db.String(8), nullable=False)
    volume_discount_cd = db.Column(db.String(2), nullable=False)
    discounted = db.Column(db.String(1))
    parent_children = db.Column(db.String(1), nullable=False)
    parent_contract_no = db.Column(db.String(12))
    discount_cost = db.Column(db.Numeric(8, 0), nullable=False)
    taxfree_kbn = db.Column(db.String(1), nullable=False)
    volume_discount_kind = db.Column(db.String(1), nullable=False)
    discount_start_date = db.Column(db.DateTime)
    discount_end_date = db.Column(db.DateTime)
    tax_cost = db.Column(db.Numeric(8, 0), nullable=False)


class VolumeDiscountMonthly(db.Model):
    __tablename__ = 'volume_discount_monthly'

    bill_month = db.Column(db.Date, primary_key=True, nullable=False)
    contract_no = db.Column(db.String(12), primary_key=True, nullable=False)
    renew_date = db.Column(db.DateTime, nullable=False)
    customer_id = db.Column(db.String(8), nullable=False)
    plan_cd = db.Column(db.String(8), nullable=False)
    volume_discount_cd = db.Column(db.String(2), nullable=False)
    discounted = db.Column(db.String(1))
    parent_children = db.Column(db.String(1), nullable=False)
    parent_contract_no = db.Column(db.String(12))
    discount_cost = db.Column(db.Numeric(8, 0), nullable=False)
    taxfree_kbn = db.Column(db.String(1), nullable=False)
    volume_discount_kind = db.Column(db.String(1), nullable=False)
    discount_start_date = db.Column(db.DateTime)
    discount_end_date = db.Column(db.DateTime)
    tax_cost = db.Column(db.Numeric(8, 0), nullable=False)


class VolumeDiscountMst(db.Model):
    __tablename__ = 'volume_discount_mst'

    volume_discount_cd = db.Column(db.String(2), primary_key=True)
    volume_discount_name = db.Column(db.String(16))
    volume_discount_kind = db.Column(db.String(1), nullable=False)
    parent_priority = db.Column(db.Numeric(1, 0), nullable=False)
    discount_cost = db.Column(db.Numeric(8, 0), nullable=False)
    taxfree_kbn = db.Column(db.String(1), nullable=False)
    max_discount_quantity = db.Column(db.Numeric(2, 0))


class WimaxDat(db.Model):
    __tablename__ = 'wimax_dat'

    ws_common_id = db.Column(db.String(20), primary_key=True)
    ws_common_renbn = db.Column(db.String(2), nullable=False)
    contract_no = db.Column(db.String(12), nullable=False, index=True)
    opt_contract_no = db.Column(db.Numeric(10, 0))
    renew_date = db.Column(db.DateTime, nullable=False)
    create_date = db.Column(db.DateTime, nullable=False)
    operate_cd = db.Column(db.String(128), nullable=False)
    c_flag = db.Column(db.String(1))
    remark = db.Column(db.String(80))
    apply_date = db.Column(db.DateTime)
    apply_kind = db.Column(db.String(4), nullable=False)
    prog_status = db.Column(db.String(2), nullable=False)
    send_plan_date = db.Column(db.DateTime)
    send_date = db.Column(db.DateTime)
    wimax_user_id = db.Column(db.String(10), nullable=False)
    cui = db.Column(db.String(20))
    uq_issue_date = db.Column(db.DateTime)
    uq_cont_start_date = db.Column(db.DateTime)
    mac_address = db.Column(db.String(12))
    serial_no = db.Column(db.String(25))
    send_name = db.Column(db.String(100), nullable=False)
    send_name_kana = db.Column(db.String(100), nullable=False)
    send_zip = db.Column(db.String(7), nullable=False)
    send_todohuken = db.Column(db.String(8), nullable=False)
    send_addr1 = db.Column(db.String(50), nullable=False)
    send_addr2 = db.Column(db.String(60))
    send_build_name = db.Column(db.String(80))
    send_telno = db.Column(db.String(13))
    arrival_plan_date = db.Column(db.DateTime)
    arrival_plan_time = db.Column(db.String(1))
    ship_no = db.Column(db.String(20))
    direct_date = db.Column(db.DateTime)
    ship_plan_date = db.Column(db.DateTime)
    ship_decision_date = db.Column(db.DateTime)
    id_renbn = db.Column(db.Numeric(2, 0), nullable=False, server_default=db.FetchedValue())
    equipment_info = db.Column(db.String(8))
    send_status = db.Column(db.String(2))
    ship_comp_date = db.Column(db.DateTime)
    iccid = db.Column(db.String(19), index=True)
    ccode = db.Column(db.String(11))
    uq_apply_no = db.Column(db.String(9))
    uq_user_cd = db.Column(db.String(8))
    user_birth = db.Column(db.DateTime)
    shop_accept_date = db.Column(db.DateTime)
    user_sex = db.Column(db.String(1))
    policy_cd = db.Column(db.String(40), nullable=False)
    uq_apply_date = db.Column(db.DateTime)
    mvno_plan_cd = db.Column(db.String(3))


class WsBillInfo(db.Model):
    __tablename__ = 'ws_bill_info'

    ws_id = db.Column(db.String(20), primary_key=True, nullable=False)
    ws_kbn = db.Column(db.String(2), primary_key=True, nullable=False)
    bill_type = db.Column(db.String(1), primary_key=True, nullable=False)
    contract_no = db.Column(db.String(12))
    opt_contract_no = db.Column(db.Numeric(10, 0))
    plan_cd = db.Column(db.String(8))
    used_month = db.Column(db.Date, primary_key=True, nullable=False)
    bill_month = db.Column(db.Date, nullable=False)
    bill_kbn_cd = db.Column(db.String(2))
    quantity = db.Column(db.Numeric(19, 0))
    cost = db.Column(db.Numeric(9, 0))
    unit = db.Column(db.String(10))
    unit_cost = db.Column(db.Numeric(10, 4))
    taxfree_kbn = db.Column(db.String(1), nullable=False)
    kihon_tuika_kbn = db.Column(db.String(1))
    creditor_cd = db.Column(db.String(1), nullable=False)
    creditor_subcd = db.Column(db.String(3))
    create_date = db.Column(db.DateTime, nullable=False)
    renew_date = db.Column(db.DateTime, nullable=False)
    c_flag = db.Column(db.String(1))
    operate_cd = db.Column(db.String(128), nullable=False)
    plan_name = db.Column(db.String(128))
    account_id = db.Column(db.String(64))
    tax_cost = db.Column(db.Numeric(9, 0))


class WsCallLog(db.Model):
    __tablename__ = 'ws_call_log'

    bill_month = db.Column(db.Date, primary_key=True, nullable=False)
    ws_kbn = db.Column(db.String(2), primary_key=True, nullable=False)
    data_renbn = db.Column(db.Numeric(7, 0), primary_key=True, nullable=False)
    telno = db.Column(db.String(16))
    partner_telno = db.Column(db.String(16))
    call_start_time = db.Column(db.DateTime)
    call_time = db.Column(db.String(7))
    call_charge = db.Column(db.Numeric(7, 1))
    ws_cont_id = db.Column(db.String(64))
    note1 = db.Column(db.String(256))
    note2 = db.Column(db.String(256))
    note3 = db.Column(db.String(256))
    note4 = db.Column(db.String(256))
    note5 = db.Column(db.String(256))
    used_month = db.Column(db.Date, nullable=False)
    contract_no = db.Column(db.String(12))
    opt_contract_no = db.Column(db.Numeric(10, 0))
    user_charge = db.Column(db.Numeric(7, 1))
    bill_kbn_cd = db.Column(db.String(2))
    create_date = db.Column(db.DateTime, nullable=False)
    renew_date = db.Column(db.DateTime, nullable=False)
    operate_cd = db.Column(db.String(128), nullable=False)


class WsUpdatelog(db.Model):
    __tablename__ = 'ws_updatelog'

    ws_updatelog_id = db.Column(db.Numeric(10, 0), primary_key=True)
    contract_no = db.Column(db.String(12))
    opt_contract_no = db.Column(db.Numeric(10, 0))
    ws_type = db.Column(db.String(5), nullable=False)
    update_status = db.Column(db.String(2))
    ntt_result = db.Column(db.String(2))
    customer_id = db.Column(db.String(8))
    account_id = db.Column(db.String(64))
    apply_kind = db.Column(db.String(4))
    detail = db.Column(db.String(256))
    prog_status = db.Column(db.String(2))
    prog_status_ws = db.Column(db.String(4))
    update_date = db.Column(db.DateTime, nullable=False)
    plan_cd = db.Column(db.String(8))
    prev_plan_cd = db.Column(db.String(8))
    pay_status = db.Column(db.String(2))
    isp_order_no = db.Column(db.String(20))
    appli_cd = db.Column(db.String(50))
    acca_order_no = db.Column(db.String(10))
    portable_apply = db.Column(db.String(1))
    business_cd = db.Column(db.String(2))
    enduser_id = db.Column(db.String(20))
    ws_common_id = db.Column(db.String(20))
    ws_common_renbn = db.Column(db.String(2))
    notify_uss = db.Column(db.String(1))
    notify_user = db.Column(db.String(1))
    create_date = db.Column(db.DateTime, nullable=False)
    renew_date = db.Column(db.DateTime, nullable=False)
    operate_cd = db.Column(db.String(128), nullable=False)
    c_flag = db.Column(db.String(1))
    osm_entry_cd = db.Column(db.String(10))
    send_status = db.Column(db.String(2))
    imei = db.Column(db.String(15))
    iccid = db.Column(db.String(19))
    em_cont_cd = db.Column(db.String(10))


class XtyleInfo(db.Model):
    __tablename__ = 'xtyle_info'

    opt_contract_no = db.Column(db.Numeric(10, 0), primary_key=True)
    prog_status = db.Column(db.String(2), nullable=False)
    send_date = db.Column(db.DateTime)
    form_no = db.Column(db.String(20))
    serial_no = db.Column(db.String(9))
    id = db.Column(db.String(7))
    create_date = db.Column(db.DateTime, nullable=False)
    renew_date = db.Column(db.DateTime, nullable=False)
    operate_cd = db.Column(db.String(128), nullable=False)
    c_flag = db.Column(db.String(1))
