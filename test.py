
from bs4 import BeautifulSoup
ITEM_HTML = """
<div class="dcf496a7b9">
    <div class="ce5e4bd105 be8ae5a5d7 c3cc25fa7b"><span class="cb5ebe3ffb e1c4f27c1b"><button aria-expanded="false"
                type="button"
                class="fc63351294 a822bdf511 e2b4ffd73d fa565176a8 f7db01295e f95c50be27 a9a04704ee eab67e87eb"><span
                    class="e57ffa4eb5">All types of places</span><span class="b9def0936d aff03b959f"><span
                        class="b6dc9a9e69 e25355d3ee" aria-hidden="true"><svg xmlns="http://www.w3.org/2000/svg"
                            viewBox="0 0 24 24">
                            <path
                                d="M12 20.09a1.24 1.24 0 0 1-.88-.36L6 14.61a.75.75 0 1 1 1.06-1.06L12 18.49l4.94-4.94A.75.75 0 0 1 18 14.61l-5.12 5.12a1.24 1.24 0 0 1-.88.36zm6-9.46a.75.75 0 0 0 0-1.06l-5.12-5.11a1.24 1.24 0 0 0-1.754-.006l-.006.006L6 9.57a.75.75 0 0 0 0 1.06.74.74 0 0 0 1.06 0L12 5.7l4.94 4.93a.73.73 0 0 0 .53.22c.2 0 .39-.078.53-.22z">
                            </path>
                        </svg></span></span></button></span><span>
            <div><span class="cb5ebe3ffb"><button aria-expanded="false" data-testid="sorters-dropdown-trigger"
                        data-selected-sorter="popularity" type="button"
                        class="fc63351294 a822bdf511 e2b4ffd73d fa565176a8 f7db01295e f95c50be27 a9a04704ee"><span
                            class="e57ffa4eb5">Sort by:
                            <!-- -->
                            <!-- -->Our Top Picks</span><span class="b9def0936d aff03b959f"><span
                                class="b6dc9a9e69 e25355d3ee" aria-hidden="true"><svg xmlns="http://www.w3.org/2000/svg"
                                    viewBox="0 0 24 24">
                                    <path
                                        d="M12 20.09a1.24 1.24 0 0 1-.88-.36L6 14.61a.75.75 0 1 1 1.06-1.06L12 18.49l4.94-4.94A.75.75 0 0 1 18 14.61l-5.12 5.12a1.24 1.24 0 0 1-.88.36zm6-9.46a.75.75 0 0 0 0-1.06l-5.12-5.11a1.24 1.24 0 0 0-1.754-.006l-.006.006L6 9.57a.75.75 0 0 0 0 1.06.74.74 0 0 0 1.06 0L12 5.7l4.94 4.93a.73.73 0 0 0 .53.22c.2 0 .39-.078.53-.22z">
                                    </path>
                                </svg></span></span></button></span></div>
        </span></div>
    <div>
        <div></div>
    </div>
    <div class="d4924c9e74">
        <h2 class="e6e585da68">Browse the results for Cardiff Center</h2>
        <div class="bea018f16c">
            <div></div>dcf496a7b9
        </div>
        <div data-testid="property-card"
            class="a826ba81c4 fe821aea6c fa2f36ad22 afd256fc79 d08f526e0d ed11e24d01 ef9845d4b3 da89aeb942">
            <div class="d20f4628d0">
                <div class="f9d4f2568d">
                    <div class="c90a25d457"><a
                            href="https://www.booking.com/hotel/gb/leonardo-hotel-cardiff.html?aid=355028&amp;ucfs=1&amp;arphpl=1&amp;checkin=2023-02-10&amp;checkout=2023-02-11&amp;dest_id=1233&amp;dest_type=district&amp;group_adults=2&amp;req_adults=2&amp;no_rooms=1&amp;group_children=0&amp;req_children=0&amp;hpos=1&amp;hapos=1&amp;sr_order=popularity&amp;srpvid=146973a8d2f403fd&amp;srepoch=1675182669&amp;all_sr_blocks=3633712_355309240_0_2_0&amp;highlighted_blocks=3633712_355309240_0_2_0&amp;matching_block_id=3633712_355309240_0_2_0&amp;sr_pri_blocks=3633712_355309240_0_2_0__12510&amp;tpi_r=2&amp;from_sustainable_property_sr=1&amp;from=searchresults&amp;map_fdco=1#hotelTmpl"
                            target="_blank" rel="noopener noreferrer" tabindex="-1" aria-hidden="true"><img
                                src="https://cf.bstatic.com/xdata/images/hotel/square200/126218438.webp?k=838d4881679bcc661cbb7f23e40d54efd11379d4fec191fb454c2502472fab60&amp;o=&amp;s=1"
                                alt="Leonardo Hotel Cardiff - Formerly Jurys Inn" width="200" height="200"
                                class="b8b0793b0e" data-testid="image"></a>
                        <div class="d226e2f1b9"><span class="cb5ebe3ffb"><button class="f41101cd39"
                                    aria-expanded="false" data-testid="wishlist-button"><span
                                        data-testid="wishlist-icon" class="b6dc9a9e69 c422d77911 ec1b6253a6"
                                        aria-hidden="true"><svg viewBox="0 0 128 128" width="1em" height="1em">
                                            <path
                                                d="M64 112a3.6 3.6 0 0 1-2-.5 138.8 138.8 0 0 1-44.2-38c-10-14.4-10.6-26-9.4-33.2a29 29 0 0 1 22.9-23.7c11.9-2.4 24 2.5 32.7 13a33.7 33.7 0 0 1 32.7-13 29 29 0 0 1 22.8 23.7c1.3 7.2.6 18.8-9.3 33.3-9.1 13.1-24 25.9-44.2 37.9a3.6 3.6 0 0 1-2 .5z">
                                            </path>
                                        </svg></span></button></span></div>
                    </div>
                </div>
                <div class="b978843432">
                    <div class="a1b3f50dcd f7c6687c3d a1f3ecff04 f996d8c258">
                        <div class="a1b3f50dcd b2fe1a41c3 a7c67ebfe5 d19ba76520 d14b211b4f">
                            <div class="b1e6dd8416 aacd9d0b0a">
                                <div class="a1b3f50dcd f7c6687c3d ef8295f3e6">
                                    <div>
                                        <div class="dd023375f5">
                                            <h3 class="a4225678b2"><a
                                                    href="https://www.booking.com/hotel/gb/leonardo-hotel-cardiff.html?aid=355028&amp;ucfs=1&amp;arphpl=1&amp;checkin=2023-02-10&amp;checkout=2023-02-11&amp;dest_id=1233&amp;dest_type=district&amp;group_adults=2&amp;req_adults=2&amp;no_rooms=1&amp;group_children=0&amp;req_children=0&amp;hpos=1&amp;hapos=1&amp;sr_order=popularity&amp;srpvid=146973a8d2f403fd&amp;srepoch=1675182669&amp;all_sr_blocks=3633712_355309240_0_2_0&amp;highlighted_blocks=3633712_355309240_0_2_0&amp;matching_block_id=3633712_355309240_0_2_0&amp;sr_pri_blocks=3633712_355309240_0_2_0__12510&amp;tpi_r=2&amp;from_sustainable_property_sr=1&amp;from=searchresults&amp;map_fdco=1#hotelTmpl"
                                                    class="e13098a59f" target="_blank" rel="noopener noreferrer"
                                                    data-testid="title-link">
                                                    <div data-testid="title" class="fcab3ed991 a23c043802">Leonardo
                                                        Hotel Cardiff - Formerly Jurys Inn</div>
                                                    <div class="e6e585da68">Opens in new window</div>
                                                </a></h3>
                                            <div class="f919b8b3d5"><span class="cb5ebe3ffb">
                                                    <div class="e4755bbd60" tabindex="0" aria-label="4 out of 5"
                                                        aria-expanded="false">
                                                        <div data-testid="rating-stars" aria-hidden="true"
                                                            class="fbb11b26f5" role="img"><span aria-hidden="true"
                                                                class="b6dc9a9e69 adc357e4f1 fe621d6382"><svg
                                                                    xmlns="http://www.w3.org/2000/svg"
                                                                    viewBox="0 0 24 24">
                                                                    <path
                                                                        d="M23.555 8.729a1.505 1.505 0 0 0-1.406-.98h-6.087a.5.5 0 0 1-.472-.334l-2.185-6.193a1.5 1.5 0 0 0-2.81 0l-.005.016-2.18 6.177a.5.5 0 0 1-.471.334H1.85A1.5 1.5 0 0 0 .887 10.4l5.184 4.3a.5.5 0 0 1 .155.543l-2.178 6.531a1.5 1.5 0 0 0 2.31 1.684l5.346-3.92a.5.5 0 0 1 .591 0l5.344 3.919a1.5 1.5 0 0 0 2.312-1.683l-2.178-6.535a.5.5 0 0 1 .155-.543l5.194-4.306a1.5 1.5 0 0 0 .433-1.661z">
                                                                    </path>
                                                                </svg></span><span aria-hidden="true"
                                                                class="b6dc9a9e69 adc357e4f1 fe621d6382"><svg
                                                                    xmlns="http://www.w3.org/2000/svg"
                                                                    viewBox="0 0 24 24">
                                                                    <path
                                                                        d="M23.555 8.729a1.505 1.505 0 0 0-1.406-.98h-6.087a.5.5 0 0 1-.472-.334l-2.185-6.193a1.5 1.5 0 0 0-2.81 0l-.005.016-2.18 6.177a.5.5 0 0 1-.471.334H1.85A1.5 1.5 0 0 0 .887 10.4l5.184 4.3a.5.5 0 0 1 .155.543l-2.178 6.531a1.5 1.5 0 0 0 2.31 1.684l5.346-3.92a.5.5 0 0 1 .591 0l5.344 3.919a1.5 1.5 0 0 0 2.312-1.683l-2.178-6.535a.5.5 0 0 1 .155-.543l5.194-4.306a1.5 1.5 0 0 0 .433-1.661z">
                                                                    </path>
                                                                </svg></span><span aria-hidden="true"
                                                                class="b6dc9a9e69 adc357e4f1 fe621d6382"><svg
                                                                    xmlns="http://www.w3.org/2000/svg"
                                                                    viewBox="0 0 24 24">
                                                                    <path
                                                                        d="M23.555 8.729a1.505 1.505 0 0 0-1.406-.98h-6.087a.5.5 0 0 1-.472-.334l-2.185-6.193a1.5 1.5 0 0 0-2.81 0l-.005.016-2.18 6.177a.5.5 0 0 1-.471.334H1.85A1.5 1.5 0 0 0 .887 10.4l5.184 4.3a.5.5 0 0 1 .155.543l-2.178 6.531a1.5 1.5 0 0 0 2.31 1.684l5.346-3.92a.5.5 0 0 1 .591 0l5.344 3.919a1.5 1.5 0 0 0 2.312-1.683l-2.178-6.535a.5.5 0 0 1 .155-.543l5.194-4.306a1.5 1.5 0 0 0 .433-1.661z">
                                                                    </path>
                                                                </svg></span><span aria-hidden="true"
                                                                class="b6dc9a9e69 adc357e4f1 fe621d6382"><svg
                                                                    xmlns="http://www.w3.org/2000/svg"
                                                                    viewBox="0 0 24 24">
                                                                    <path
                                                                        d="M23.555 8.729a1.505 1.505 0 0 0-1.406-.98h-6.087a.5.5 0 0 1-.472-.334l-2.185-6.193a1.5 1.5 0 0 0-2.81 0l-.005.016-2.18 6.177a.5.5 0 0 1-.471.334H1.85A1.5 1.5 0 0 0 .887 10.4l5.184 4.3a.5.5 0 0 1 .155.543l-2.178 6.531a1.5 1.5 0 0 0 2.31 1.684l5.346-3.92a.5.5 0 0 1 .591 0l5.344 3.919a1.5 1.5 0 0 0 2.312-1.683l-2.178-6.535a.5.5 0 0 1 .155-.543l5.194-4.306a1.5 1.5 0 0 0 .433-1.661z">
                                                                    </path>
                                                                </svg></span></div>
                                                    </div>
                                                </span></div><span class="cb5ebe3ffb"><span aria-expanded="false"
                                                    tabindex="0" role="button" data-testid="preferred-badge"><span
                                                        class="b6dc9a9e69 c79b3cbed2 e6c50852bd fe3639fe67"
                                                        aria-hidden="true"><svg viewBox="0 0 128 128" width="1em"
                                                            height="1em">
                                                            <path
                                                                d="M112 8H16a8 8 0 0 0-8 8v96a8 8 0 0 0 8 8h96a8 8 0 0 0 8-8V16a8 8 0 0 0-8-8zM48 96H24V58h24zm56-25a8.7 8.7 0 0 1-2 6 8.9 8.9 0 0 1 1 4 6.9 6.9 0 0 1-5 7c-.5 4-4.8 8-9 8H56V58l10.3-23.3a5.4 5.4 0 0 1 10.1 2.7 10.3 10.3 0 0 1-.6 2.7L72 52h23c4.5 0 9 3.5 9 8a9.2 9.2 0 0 1-2 5.3 7.5 7.5 0 0 1 2 5.7z">
                                                            </path>
                                                        </svg></span></span></span><span class="cb5ebe3ffb"><span
                                                    aria-expanded="false" data-testid="genius-badge" tabindex="0"
                                                    role="img" class="b6dc9a9e69 bc0ef76f96 e6c50852bd"
                                                    aria-label="Genius discounts available at this property."><svg
                                                        xmlns="http://www.w3.org/2000/svg" viewBox="0 0 80 32">
                                                        <g fill="none">
                                                            <rect width="80" height="32.049" fill="#004cb8" rx="4">
                                                            </rect>
                                                            <path fill="#fff"
                                                                d="m44.9668352 5.5533056c.216944 0 .339024.090062.3661543.269157l.0058137.082203v6.00384c0 .598784.15488 1.081728.468224 1.446784.311552.365184.752384.546944 1.318784.546944.8360411 0 1.5222034-.3462224 2.0583844-1.0386671l.1210716-.1659409v-6.79296c0-.204512.088396-.320138.2661313-.345849l.0816447-.005511h2.201984c.203392 0 .318388.090062.343959.269157l.005481.082203v9.97056c0 .204512-.089572.318864-.267687.3442565l-.081753.0054395h-1.787008c-.2109806 0-.3651605-.0750446-.4590737-.2251337l-.0419183-.0812983-.26176-.635136c-.290944.26304-.542208.467328-.752256.612736-.210048.147072-.507904.282112-.893568.406656-.385664.12288-.81088.185216-1.275648.185216-1.220608 0-2.186496-.375552-2.8992-1.128448-.6602514-.6974537-1.0146749-1.6397022-1.0619382-2.8224411l-.0054538-.2772069v-6.3552c0-.204512.094864-.320138.283563-.345849l.086613-.005511zm12.803968-.35456c1.773184 0 3.117824.562432 4.033664 1.687424.140112.165088.140476.320866.0022925.4651045l-.0677005.0611035-1.1776 1.095552c-.173824.131456-.34944.108928-.523392-.065792-.624896-.657664-1.358336-.986496-2.201856-.986496-.521728 0-.940032.07616-1.253376.230144-.311552.15232-.468224.361728-.468224.624768 0 .306304.19968.559104.59904.756352.401152.195584 1.057152.375552 1.972992.536576 2.49984.422272 3.749632 1.5264 3.749632 3.309056 0 1.079936-.42176 1.934976-1.263616 2.5632-.843648.628224-1.874816.941568-3.095424.941568-1.265408 0-2.306944-.266624-3.128192-.799616-.821248-.53312-1.39968-1.208064-1.733632-2.026752-.088928-.192304-.049966-.338254.116886-.44128l.079338-.041536 1.656192-.744192c.218624-.102144.37184-.043264.457984.174848.175616.453376.480256.825472.91584 1.117952s.958976.437888 1.570176.437888c.507776 0 .919296-.095232 1.230848-.283776.313344-.190464.468352-.446592.468352-.768512 0-.365184-.203136-.655872-.609408-.875776-.408064-.219776-1.119104-.423936-2.136576-.612608-1.031168-.190336-1.84896-.558976-2.451584-1.107712-.604288-.546816-.9056-1.230464-.9056-2.049152 0-.977792.37888-1.756672 1.134592-2.332928.754048-.576384 1.764608-.865408 3.028352-.865408zm-36.68096 0c1.642496 0 2.928512.507136 3.858176 1.523072.929664 1.014144 1.394432 2.289664 1.394432 3.823104v.700928c0 .233728-.115328.35136-.347648.35136h-7.499392c.160128.671488.476928 1.21152.948608 1.621632.47168.408448 1.07264.612736 1.79904.612736.988288 0 1.742336-.408448 2.265728-1.227136.087808-.131456.225536-.15232.414848-.065664l1.874816.78912c.21696.072704.268544.204288.151552.394624-1.06048 1.79648-2.628864 2.694784-4.706944 2.694784-1.570048 0-2.902528-.526208-4.000896-1.576704-1.096704-1.052288-1.645952-2.397056-1.645952-4.03264 0-1.635456.545792-2.980224 1.635584-4.032512 1.089792-1.050624 2.375808-1.576704 3.858048-1.576704zm-12.376576-5.1987456c2.16 0 4.13952.7363072 5.660544 1.9553792.07296.0590464.118144.1424.125056.232704.010368.0937728-.017408.1840768-.076416.2570112-.388992.4688768-1.19808 1.4448384-1.59744 1.9241344-.059008.0729344-.14592.11808-.239616.1250304-.093824.0069504-.184064-.0243072-.253568-.0833536-.958464-.8127232-2.226048-1.3059072-3.61856-1.3059072-2.976256 0-5.389824 2.3757312-5.389824 5.1542272s2.413568 5.036032 5.389824 5.036032c1.156352 0 2.226048-.340352 3.10464-.92032v-2.250624h-2.54912c-.09024 0-.18048-.034688-.246528-.100736-.062464-.06592-.100736-.152832-.100736-.246528v-2.181248c0-.093696.038272-.180608.100736-.246528.066048-.062592.156288-.100736.246528-.100736h5.025152c.190976 0 .347264.156288.347264.347264v6.307328c0 .208384-.09024.402816-.25344.538368-1.524608 1.219072-3.51104 1.955328-5.674496 1.955328-4.8098688 0-8.7132672-3.646848-8.7132672-8.1376 0-4.4942592 3.9033984-8.2592256 8.7132672-8.2592256zm24.552448 5.1987456c1.220608 0 2.162304.332288 2.823424.996864.6138971.61710629.9427154 1.47006759.9865573 2.56011373l.0050587.25575827v6.793088c0 .2044-.08967.318738-.2677238.3441288l-.0817162.0054392h-2.200192c-.203392 0-.318486-.088788-.3440815-.2674788l-.0054865-.0820892v-6.026368c0-1.315328-.602496-1.972992-1.809408-1.972992-.406272 0-.814336.124672-1.220608.373888-.33856.20618667-.6125867.42801778-.82008.66556741l-.116496.14441659v6.815488c0 .2044-.094864.318738-.2846778.3441288l-.0871622.0054392h-2.179584c-.215376 0-.337162-.088788-.3642433-.2674788l-.0058047-.0820892v-9.970688c0-.2044.094864-.320012.2834773-.34572125l.0865707-.00551075h1.7888c.2109806 0 .3587657.08134531.4422269.24194015l.0363651.08689185.284032.6144c.929664-.818688 1.947136-1.227136 3.050752-1.227136zm7.523712.265216c.216832 0 .337526.090062.3643115.26907125l.0057365.08216075v9.970688c0 .204512-.09359.318766-.2829995.344134l-.0870485.005434h-2.179584c-.216944 0-.337652-.08869-.3644393-.267442l-.0057367-.082126v-9.970688c0-.2044.09359-.320012.2830852-.34572125l.0870908-.00551075zm-19.699584 2.211456c-.63872 0-1.174144.162688-1.602816.49152s-.736896.756352-.926208 1.282432h5.013248c-.101504-.49664-.383872-.917248-.848768-1.259904-.46656-.342656-1.01056-.514048-1.635456-.514048z"
                                                                transform="translate(9 7)"></path>
                                                            <path fill="#febb02"
                                                                d="m37.6090112 2.1196288c0 .5691264.204288 1.058944.614656 1.4694272.410496.4084992.900224.6147328 1.469312.6147328s1.058816-.2062336 1.469312-.6147328c.408448-.4104832.614656-.9003008.614656-1.4694272s-.206208-1.0589312-.614656-1.4694272c-.410496-.4104832-.900224-.6147328-1.469312-.6147328s-1.058816.2042496-1.469312.6147328c-.410368.410496-.614656.9003008-.614656 1.4694272z"
                                                                transform="translate(9 7)"></path>
                                                        </g>
                                                    </svg></span></span>
                                        </div>
                                    </div>
                                    <div>
                                        <div class="a1fbd102d9" data-testid="location"><a target="_blank"
                                                rel="noopener noreferrer"
                                                href="https://www.booking.com/hotel/gb/leonardo-hotel-cardiff.html?aid=355028&amp;ucfs=1&amp;arphpl=1&amp;checkin=2023-02-10&amp;checkout=2023-02-11&amp;dest_id=1233&amp;dest_type=district&amp;group_adults=2&amp;req_adults=2&amp;no_rooms=1&amp;group_children=0&amp;req_children=0&amp;hpos=1&amp;hapos=1&amp;sr_order=popularity&amp;srpvid=146973a8d2f403fd&amp;srepoch=1675182669&amp;all_sr_blocks=3633712_355309240_0_2_0&amp;highlighted_blocks=3633712_355309240_0_2_0&amp;matching_block_id=3633712_355309240_0_2_0&amp;sr_pri_blocks=3633712_355309240_0_2_0__12510&amp;tpi_r=2&amp;from_sustainable_property_sr=1&amp;from=searchresults&amp;map_fdco=1&amp;map=1"
                                                class="fc63351294 a168c6f285 e0e11a8307 a25b1d9e47"><span><span
                                                        class="f4bd0794db b4273d69aa" data-testid=" ">Cardiff
                                                        Center, Cardiff</span><span class="f4bd0794db b4273d69aa">Show
                                                        on map</span></span></a></div>
                                    </div>
                                    <div class="d8eab2cf7f f0d4d6a2f5 ff07fc41e3"><span
                                            data-testid="icon-with-text-icon" class="b6dc9a9e69 e492382468 e25355d3ee"
                                            aria-hidden="true"><svg xmlns="http://www.w3.org/2000/svg"
                                                viewBox="0 0 24 24">
                                                <path
                                                    d="M21.22 3.37a.75.75 0 0 0-.6-.59c-4.85-.9-10.6.55-13.37 3.36S3.1 14.39 3.88 19.05L2 21a.75.75 0 0 0 0 1 .74.74 0 0 0 .53.22A.71.71 0 0 0 3 22l2-1.9a16.94 16.94 0 0 0 2.76.23c4.09 0 8.19-1.33 10.35-3.52 2.71-2.81 4.07-8.59 3.11-13.44zM17 15.75c-2.11 2.14-6.59 3.36-10.7 3L16.59 8.47a.75.75 0 0 0 0 -1.06.77.77 0 0 0-1.07 0l-10.3 10.3c-.33-3.91.91-8.31 3.1-10.52s7.29-3.63 11.52-3c.67 4.22-.54 9.22-2.84 11.56z">
                                                </path>
                                            </svg></span><span class="a51f4b5adb">Travel Sustainable property</span>
                                    </div>
                                </div>
                            </div>
                            <div class="a1b3f50dcd f7c6687c3d bdf0df2d01 f920833fe5">
                                <div class="a1b3f50dcd f7c6687c3d ef8295f3e6"><a target="_blank"
                                        rel="noopener noreferrer" data-testid="review-score-link"
                                        href="https://www.booking.com/hotel/gb/leonardo-hotel-cardiff.html?aid=355028&amp;ucfs=1&amp;arphpl=1&amp;checkin=2023-02-10&amp;checkout=2023-02-11&amp;dest_id=1233&amp;dest_type=district&amp;group_adults=2&amp;req_adults=2&amp;no_rooms=1&amp;group_children=0&amp;req_children=0&amp;hpos=1&amp;hapos=1&amp;sr_order=popularity&amp;srpvid=146973a8d2f403fd&amp;srepoch=1675182669&amp;all_sr_blocks=3633712_355309240_0_2_0&amp;highlighted_blocks=3633712_355309240_0_2_0&amp;matching_block_id=3633712_355309240_0_2_0&amp;sr_pri_blocks=3633712_355309240_0_2_0__12510&amp;tpi_r=2&amp;from_sustainable_property_sr=1&amp;from=searchresults&amp;map_fdco=1#hotelTmpl"
                                        class="fc63351294 a168c6f285 aeccf0d865 a25b1d9e47"><span>
                                            <div data-testid="review-score"
                                                class="a1b3f50dcd cbb2d85c33 a1f3ecff04 db7f07f643 d19ba76520 d02f1578ba d17b3fe5e2">
                                                <div aria-label="Scored 7.9 " class="b5cd09854e d10a6220b4">7.9</div>
                                                <div class="b1e6dd8416 aacd9d0b0a b48795b3df">
                                                    <div aria-label="Good" class="b5cd09854e f0d4d6a2f5 e46e88563a">
                                                        Good
                                                        <!-- -->
                                                    </div>
                                                    <div class="d8eab2cf7f c90c0a70d3 db63693c62">5,195 reviews</div>
                                                </div>
                                            </div>
                                        </span></a>
                                    <div><a target="_blank" rel="noopener noreferrer"
                                            data-testid="secondary-review-score-link" aria-label="Location: Scored 9.3 "
                                            href="https://www.booking.com/hotel/gb/leonardo-hotel-cardiff.html?aid=355028&amp;ucfs=1&amp;arphpl=1&amp;checkin=2023-02-10&amp;checkout=2023-02-11&amp;dest_id=1233&amp;dest_type=district&amp;group_adults=2&amp;req_adults=2&amp;no_rooms=1&amp;group_children=0&amp;req_children=0&amp;hpos=1&amp;hapos=1&amp;sr_order=popularity&amp;srpvid=146973a8d2f403fd&amp;srepoch=1675182669&amp;all_sr_blocks=3633712_355309240_0_2_0&amp;highlighted_blocks=3633712_355309240_0_2_0&amp;matching_block_id=3633712_355309240_0_2_0&amp;sr_pri_blocks=3633712_355309240_0_2_0__12510&amp;tpi_r=2&amp;from_sustainable_property_sr=1&amp;from=searchresults&amp;map_fdco=1#hotelTmpl"
                                            class="fc63351294 a168c6f285 a25b1d9e47"><span><span
                                                    class="f9afbb0024">Location
                                                    <!-- -->
                                                    <!-- -->9.3</span></span></a>
                                    </div>
                                </div>
                            </div>
                        </div>
                        <div>
                            <div class="adf603f27d"><span class="cb5ebe3ffb"><span aria-expanded="false"
                                        data-testid="property-card-deal" tabindex="0"
                                        aria-label="10% off. You’re getting a reduced rate because this property is offering a discount.."
                                        class="d8eab2cf7f c9fccc9041 d226e198ab"><span class="e2f34d59b1">10%
                                            off</span></span></span></div>
                        </div>
                        <div class="d7449d770c a081c98c6f" tabindex="0" data-testid="availability-single">
                            <div class="b9fb1fc689">
                                <div data-testid="recommended-units" class="b762360cf2">
                                    <div class="e6706895d8 c25da3b967" role="none">
                                        <div class="d22a7c133b">
                                            <div role="link" tabindex="0" class="d8eab2cf7f"><span
                                                    class="df597226dd">Standard Twin Room</span></div>
                                            <div class="cb5b4b68a4">
                                                <div class="d8eab2cf7f">2 twin beds</div>
                                            </div>
                                            <div class="f06e87f720">
                                                <div class="d506630cf3">FREE cancellation
                                                    <!-- --> •
                                                    <!-- -->No
                                                    prepayment needed</div>
                                                <div>You can cancel later, so lock in this great price today!</div>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                            <div class="e41894cca1">
                                <div data-testid="availability-rate-wrapper"
                                    class="a1b3f50dcd f7c6687c3d a1f3ecff04 e62c1da9f5">
                                    <div class="fd1924b122 d4741ba240" data-testid="availability-rate-information">
                                        <div data-testid="price-for-x-nights" class="d8eab2cf7f c90c0a70d3">1
                                            night
                                            <!-- -->,
                                            <!-- -->2 adults</div><span class="cb5ebe3ffb">
                                            <div aria-expanded="false"><span class="c5888af24f e729ed5ab6"
                                                    aria-hidden="true">NGN&nbsp;79,293</span><span
                                                    data-testid="price-and-discounted-price" aria-hidden="true"
                                                    class="fcab3ed991 fbd1d3018c e729ed5ab6">NGN&nbsp;71,364</span><span
                                                    class="b6dc9a9e69 ab800a8b9d e25355d3ee b8c9de5937"
                                                    aria-hidden="true"><svg xmlns="http://www.w3.org/2000/svg"
                                                        viewBox="0 0 24 24">
                                                        <path
                                                            d="M14.25 15.75h-.75a.75.75 0 0 1-.75-.75v-3.75a1.5 1.5 0 0 0-1.5-1.5h-.75a.75.75 0 0 0 0 1.5h.75V15a2.25 2.25 0 0 0 2.25 2.25h.75a.75.75 0 0 0 0-1.5zM11.625 6a1.125 1.125 0 1 0 0 2.25 1.125 1.125 0 0 0 0-2.25.75.75 0 0 0 0 1.5.375.375 0 1 1 0-.75.375.375 0 0 1 0 .75.75.75 0 0 0 0-1.5zM22.5 12c0 5.799-4.701 10.5-10.5 10.5S1.5 17.799 1.5 12 6.201 1.5 12 1.5 22.5 6.201 22.5 12zm1.5 0c0-6.627-5.373-12-12-12S0 5.373 0 12s5.373 12 12 12 12-5.373 12-12z">
                                                        </path>
                                                    </svg></span></div>
                                        </span>
                                        <div class="e6e585da68">Original price NGN&nbsp;79,293. Current price
                                            NGN&nbsp;71,364.</div>
                                        <div data-testid="taxes-and-charges" class="d8eab2cf7f c90c0a70d3">Includes
                                            taxes and fees</div>
                                    </div>
                                    <div class="a68bfa09c2" data-testid="availability-cta"><a target="_blank"
                                            href="https://www.booking.com/hotel/gb/leonardo-hotel-cardiff.html?aid=355028&amp;ucfs=1&amp;arphpl=1&amp;checkin=2023-02-10&amp;checkout=2023-02-11&amp;dest_id=1233&amp;dest_type=district&amp;group_adults=2&amp;req_adults=2&amp;no_rooms=1&amp;group_children=0&amp;req_children=0&amp;hpos=1&amp;hapos=1&amp;sr_order=popularity&amp;srpvid=146973a8d2f403fd&amp;srepoch=1675182669&amp;all_sr_blocks=3633712_355309240_0_2_0&amp;highlighted_blocks=3633712_355309240_0_2_0&amp;matching_block_id=3633712_355309240_0_2_0&amp;sr_pri_blocks=3633712_355309240_0_2_0__12510&amp;tpi_r=2&amp;from_sustainable_property_sr=1&amp;from=searchresults&amp;map_fdco=1#hotelTmpl"
                                            class="fc63351294 a822bdf511 d4b6b7a9e7 fa565176a8 f7db01295e f4605622ad b2f0d6a80e"><span
                                                class="e57ffa4eb5">See availability</span><span
                                                class="b9def0936d aff03b959f"><span class="b6dc9a9e69 e25355d3ee"
                                                    aria-hidden="true"><span data-testid="availability-cta-icon"
                                                        class="b6dc9a9e69 e25355d3ee" aria-hidden="true"><svg
                                                            xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"
                                                            data-rtl-flip="true">
                                                            <path
                                                                d="M9.45 6c.2 0 .39.078.53.22l5 5c.208.206.323.487.32.78a1.1 1.1 0 0 1-.32.78l-5 5a.75.75 0 0 1-1.06 0 .74.74 0 0 1 0-1.06L13.64 12 8.92 7.28a.74.74 0 0 1 0-1.06.73.73 0 0 1 .53-.22zm4.47 5.72zm0 .57z">
                                                            </path>
                                                        </svg></span></span></span></a></div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            <div class="ea6e492f88"></div>
        </div>
    </div>
    <div></div>
</div>
"""


class ParsedItemLocator:
    """
    This allows us to easily change/enhance our page/parser locators
    """
    HOTEL_NAME = 'div.d4924c9e74 div.a826ba81c4 div.b978843432 h3.a4225678b2 a.e13098a59f div.a23c043802'
    HOTEL_IMAGE = 'div.d4924c9e74 div.c90a25d457 a img'
    HOTEL_REVIEW = 'a.fc63351294.a168c6f285.aeccf0d865.a25b1d9e47'
    HOTEL_LOCATION_RATE = "span.f9afbb0024"
    HOTEL_DESCRIPTION = "div.d8eab2cf7f"


class ParsedItem:
    
    def __init__(self, page):
        self.soup = BeautifulSoup(page, 'html.parser')
        
    @property
    def find_hotel_name(self):
        locator = ParsedItemLocator.HOTEL_NAME
        
        return self.soup.select_one(locator)
        
    
    @property
    def find_hotel_image(self):
        locator = ParsedItemLocator.HOTEL_IMAGE
          
        return self.soup.select_one(locator)  
        
    
    @property
    def find_hotel_review(self):
        locator = ParsedItemLocator.HOTEL_REVIEW
         
        return self.soup.select_one(locator)   
        
    
    @property
    def find_hotel_location_rate(self):
        locator = ParsedItemLocator.HOTEL_LOCATION_RATE
           
        return self.soup.select_one(locator) 
        
        
        
    @property
    def find_hotel_description(self):
        locator = ParsedItemLocator.HOTEL_DESCRIPTION
        
        return self.soup.select_one(locator)
    
    

page = ParsedItem(ITEM_HTML)
print(page.find_hotel_image)
